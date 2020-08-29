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


class DbActorError(Exception):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.http_code = http_code


class DbActor(Actor):
    db = SqliteDatabase(Config.get('SQLITE_DATABASE'))

    def receiveMessage(self, msg, sender):
        """Handle incoming actor messages."""
        if not isinstance(msg, ActorMessage):
            return
        self.db.connect(reuse_if_open=True)
        try:
            if msg.customer_id:
                self.__check_customer_id(msg.customer_id)
            if msg.action == CustomersActorAction.CUSTOMERS_ADD:
                customer_id = self.__add_customer(msg.payload.get('customer'))
                message = ActorMessage(payload={'id': customer_id})
                self.send(msg.response_to, message)
            elif msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
                budget = self.__get_customer_budget(msg.customer_id,
                                                    msg.payload.get('year'))
                message = ActorMessage(payload={'budget': budget})
                self.send(msg.response_to, message)
            elif msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
                tickets = self.__get_customer_tickets(msg.customer_id,
                                                      msg.payload)
                message = ActorMessage(payload={'tickets': tickets})
                self.send(msg.response_to, message)
            elif msg.action == EventsActorAction.EVENTS_ADD:
                self.__add_event(msg.payload.get('event'))
                self.send(msg.response_to, ActorMessage())
            elif msg.action == EventsActorAction.EVENTS_GET:
                event = self.__get_event_by_id(msg.payload.get('event_id'))
                message = ActorMessage(payload={'event': event})
                self.send(msg.response_to, message)
            elif msg.action == EventsActorAction.EVENTS_LIST:
                events = self.__get_events()
                message = ActorMessage(payload={'events': events})
                self.send(msg.response_to, message)
            elif msg.action == EventsActorAction.EVENTS_PURCHASE:
                self.__purchase_event_ticket(msg.customer_id,
                                             msg.payload.get('event_id'),
                                             msg.payload.get('quantity'))
                self.send(msg.response_to, ActorMessage())
            elif msg.action == EventsActorAction.EVENTS_SALES:
                sales_dict = self.__get_sales_per_event()
                message = ActorMessage(payload={'sales_dict': sales_dict})
                self.send(msg.response_to, message)
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

    def __check_customer_id(self, customer_id):
        """Check if customer exists."""
        try:
            CustomerModel.get(CustomerModel.id == customer_id)
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404) from DoesNotExist

    def __add_customer(self, customer):
        """Add customer to database."""
        customer_model = Customer.to_model(customer)
        customer_model.save()
        return customer_model.id

    def __get_customer_budget(self, customer_id, year):
        """Get customer budget for a specific year."""
        try:
            customer_model = CustomerModel.get(
                CustomerModel.id == customer_id)
            events = (EventModel
                      .select(EventModel.id,
                              EventModel.ticket_price,
                              (fn.COUNT(TicketModel.id)*EventModel.ticket_price)
                              .alias('total_costs'))
                      .join(TicketModel)
                      .join(CustomerModel)
                      .where(CustomerModel.id == customer_id, EventModel.date.year == year)
                      .group_by(EventModel.id))
            costs = 0
            for event in events:
                costs = costs + event.total_costs
            return customer_model.budget - costs
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404) from DoesNotExist

    def __get_customer_tickets(self, customer_id, filter_opt):
        """Get customer tickets filtered by order date or event date."""
        try:
            tickets = []
            order_date = filter_opt.get('order_date')
            event_date = filter_opt.get('event_date')
            if order_date:
                ticket_models = (TicketModel
                                 .select()
                                 .join(CustomerModel)
                                 .where(CustomerModel.id == customer_id,
                                        TicketModel.order_date == order_date))
            elif event_date:
                ticket_models = (TicketModel
                                 .select()
                                 .join(CustomerModel)
                                 .switch(TicketModel)
                                 .join(EventModel)
                                 .where(CustomerModel.id == customer_id,
                                        EventModel.date == event_date))
            else:
                ticket_models = (TicketModel
                                 .select()
                                 .join(CustomerModel)
                                 .where(CustomerModel.id == customer_id))
            for ticket_model in ticket_models:
                ticket = Ticket.from_model(ticket_model)
                tickets.append(ticket)
            return tickets
        except DoesNotExist:
            raise DbActorError("Customer not found.", 404) from DoesNotExist

    def __add_event(self, event):
        """Add event to database."""
        event_model = Event.to_model(event)
        event_model.save()
        return event_model.id

    def __get_event_by_id(self, event_id):
        """Get event by event ID."""
        try:
            event_model = EventModel.get(EventModel.id == event_id)
            event = Event.from_model(event_model)
            return event
        except DoesNotExist:
            raise DbActorError("Event not found.", 404) from DoesNotExist

    def __get_events(self):
        """Get all available events."""
        events = []
        event_models = EventModel.select()
        for event_model in event_models:
            event = Event.from_model(event_model)
            events.append(event)
        return events

    def __purchase_event_ticket(self, customer_id, event_id, quantity):
        """Purchase of a certain number of tickets for a specific event."""
        try:
            event_model = EventModel.get(EventModel.id == event_id)
        except DoesNotExist:
            raise DbActorError("Event not found.", 404) from DoesNotExist
        customer_model = CustomerModel.get(CustomerModel.id == customer_id)
        event_customer_ticket_models = (TicketModel
                                        .select()
                                        .join(CustomerModel)
                                        .switch(TicketModel)
                                        .join(EventModel)
                                        .where(CustomerModel.id == customer_id,
                                               EventModel.id == event_id))
        event_ticket_models = (TicketModel
                               .select()
                               .join(EventModel)
                               .where(EventModel.id == event_id))
        total_price = event_model.ticket_price * quantity
        available_budget = self.__get_customer_budget(customer_model.id,
                                                      event_model.date.year)
        if available_budget - total_price < 0:
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
        for _ in range(quantity):
            ticket_model = TicketModel(order_date=date.today(),
                                       customer=customer_model, event=event_model)
            ticket_model.save()

    def __get_sales_per_event(self):
        """Get number of sales of all events."""
        sales_dict = []
        events = (EventModel
                  .select(EventModel.id, EventModel.name, fn.COUNT(TicketModel.id).alias('sales'))
                  .join(TicketModel, JOIN.LEFT_OUTER)
                  .group_by(EventModel.id))
        for event in events:
            sales_dict.append({'event_id': event.id,
                               'event_name': event.name,
                               'sales': event.sales})
        return sales_dict
