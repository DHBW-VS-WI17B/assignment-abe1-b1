from datetime import date, timedelta
from thespian.actors import Actor
from peewee import SqliteDatabase, DoesNotExist, fn, JOIN
from app.config.config import Config
from app.enums.customers_action import CustomersActorAction
from app.enums.events_action import EventsActorAction
from app.models.event import Event as EventModel
from app.models.ticket import Ticket as TicketModel
from app.models.customer import Customer as CustomerModel
from app.classes.event import Event
from app.classes.ticket import Ticket
from app.classes.customer import Customer
from app.classes.actor_message import ActorMessage
from app.classes.actor_message_error import ActorMessageError

# TODO: transactions
# TODO: Custom exception class


class DbActorError(Exception):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.http_code = http_code


class DbActor(Actor):
    db = SqliteDatabase(Config.get('SQLITE_DATABASE'))

    def receiveMessage(self, msg, sender):
        if not isinstance(msg, ActorMessage):
            return
        self.db.connect(reuse_if_open=True)
        try:
            if msg.customer_id:
                self.__check_customer_id(msg)
            if msg.action == CustomersActorAction.CUSTOMERS_ADD:
                self.__add_customer(msg)
            elif msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
                self.__get_customer_budget(msg)
            elif msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
                self.__get_customer_tickets(msg)
            elif msg.action == EventsActorAction.EVENTS_ADD:
                self.__add_event(msg)
            elif msg.action == EventsActorAction.EVENTS_GET:
                self.__get_event(msg)
            elif msg.action == EventsActorAction.EVENTS_LIST:
                self.__list_event(msg)
            elif msg.action == EventsActorAction.EVENTS_PURCHASE:
                self.__purchase_event_ticket(msg)
            elif msg.action == EventsActorAction.EVENTS_SALES:
                self.__get_sales_per_event(msg)
        except DbActorError as ex:
            err = ActorMessageError(message=str(ex), http_code=ex.http_code)
            self.send(msg.response_to,
                      ActorMessage(error=err))
        except Exception as ex:
            print(ex)
            error = ActorMessageError(message=str(ex), http_code=500)
            self.send(msg.response_to, ActorMessage(error=error))
        finally:
            if not self.globalName:
                self.db.close()

    def __check_customer_id(self, msg):
        try:
            CustomerModel.get(CustomerModel.id == msg.customer_id)
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404)

    def __add_customer(self, msg):
        customer = msg.payload.get('customer')
        customer_model = Customer.to_model(customer)
        customer_model.save()
        self.send(msg.response_to, ActorMessage())

    def __get_customer_budget(self, msg):
        customer_id = msg.payload.get('customer_id')
        year = msg.payload.get('year')
        try:
            customer_model = CustomerModel.get(
                CustomerModel.id == msg.customer_id)
            events = (EventModel
                      .select(EventModel.id, EventModel.ticket_price, (fn.COUNT(TicketModel.id)*EventModel.ticket_price).alias('total_costs'))
                      .join(TicketModel)
                      .join(CustomerModel)
                      .where(CustomerModel.id == customer_id, EventModel.date.year == year)
                      .group_by(EventModel.id))
            costs = 0
            for event in events:
                costs = costs + event.total_costs
            message = ActorMessage(
                payload={'budget': customer_model.budget - costs})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404)

    def __get_customer_tickets(self, msg):
        try:
            tickets = []
            order_date = msg.payload.get('order_date')
            event_date = msg.payload.get('event_date')
            if order_date:
                ticket_models = (TicketModel
                                 .select()
                                 .join(CustomerModel)
                                 .where(CustomerModel.id == msg.customer_id,
                                        TicketModel.order_date == order_date))
            elif event_date:
                ticket_models = (TicketModel
                                 .select()
                                 .join(CustomerModel)
                                 .switch(TicketModel)
                                 .join(EventModel)
                                 .where(CustomerModel.id == msg.customer_id,
                                        EventModel.date == event_date))
            else:
                ticket_models = TicketModel.select().join(CustomerModel)
            for ticket_model in ticket_models:
                ticket = Ticket.from_model(ticket_model)
                tickets.append(ticket)
            message = ActorMessage(payload={'tickets': tickets})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404)

    def __add_event(self, msg):
        event = msg.payload.get('event')
        event_model = Event.to_model(event)
        event_model.save()
        self.send(msg.response_to, ActorMessage())

    def __get_event(self, msg):
        event_id = msg.payload.get('event_id')
        try:
            event_model = EventModel.get(EventModel.id == event_id)
            event = Event.from_model(event_model)
            message = ActorMessage(payload={'event': event})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise DbActorError("Event not found.", 404)

    def __list_event(self, msg):
        events = []
        event_models = EventModel.select()
        for event_model in event_models:
            event = Event.from_model(event_model)
            events.append(event)
        message = ActorMessage(payload={'events': events})
        self.send(msg.response_to, message)

    def __purchase_event_ticket(self, msg):
        event_id = msg.payload.get('event_id')
        quantity = msg.payload.get('quantity')
        # TODO
        try:
            event_model = EventModel.get(EventModel.id == event_id)
        except DoesNotExist:
            raise DbActorError("Event not found.", 404)
        customer_model = CustomerModel.get(CustomerModel.id == msg.customer_id)
        event_customer_ticket_models = (TicketModel
                                        .select()
                                        .join(CustomerModel)
                                        .switch(TicketModel)
                                        .join(EventModel)
                                        .where(CustomerModel.id == msg.customer_id, EventModel.id == event_id))
        event_ticket_models = (TicketModel
                               .select()
                               .join(EventModel)
                               .where(EventModel.id == event_id))
        total_price = event_model.ticket_price * quantity
        if customer_model.budget - total_price < 0:
            raise DbActorError("The budget of the customer is not sufficient.",
                               400)
        if event_model.max_tickets_per_customer < len(event_customer_ticket_models) + quantity:
            raise DbActorError(("With this purchase the maximum number of tickets per "
                                "customer for this event would be exceeded."), 400)
        if event_model.max_tickets < len(event_ticket_models) + quantity:
            raise DbActorError(("With this purchase the maximum number of "
                                "tickets for this event would be exceeded."), 400)
        sale_not_started = event_model.sale_start_date > date.today()
        sale_end_date = event_model.sale_start_date + \
            timedelta(days=event_model.sale_period)
        sale_over = sale_end_date < date.today()
        if sale_not_started or sale_over:
            raise DbActorError("Currently no tickets can be purchased for this event.",
                               400)
        date_today = date.today()
        for _ in range(quantity):
            ticket_model = TicketModel(order_date=date_today,
                                       customer=customer_model, event=event_model)
            ticket_model.save()
        self.send(msg.response_to, ActorMessage())

    def __get_sales_per_event(self, msg):
        sales_dict = []
        events = (EventModel
                  .select(EventModel.id, fn.COUNT(TicketModel.id).alias('sales'))
                  .join(TicketModel, JOIN.LEFT_OUTER)
                  .group_by(EventModel.id))
        for event in events:
            sales_dict.append({'event_id': event.id,
                               'sales': event.sales})
        message = ActorMessage(payload={'sales_dict': sales_dict})
        self.send(msg.response_to, message)
