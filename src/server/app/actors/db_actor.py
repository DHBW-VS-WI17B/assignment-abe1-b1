from thespian.actors import Actor
from peewee import SqliteDatabase, DoesNotExist
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
from datetime import date, timedelta

# TODO: transactions
# TODO: Custom exception class


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
            elif msg.action == EventsActorAction.EVENTS_TICKETS:
                self.__get_event_tickets(msg)
        except Exception as ex:
            self.send(msg.response_to, ActorMessage(error=str(ex)))
        if not self.globalName:
            self.db.close()

    def __check_customer_id(self, msg):
        try:
            CustomerModel.get(CustomerModel.id == msg.customer_id)
        except DoesNotExist:
            # TODO: http status code
            raise Exception("Customer not found.")

    def __add_customer(self, msg):
        customer = msg.payload.get('customer')
        customer_model = Customer.to_model(customer)
        customer_model.save()
        self.send(msg.response_to, ActorMessage())

    def __get_customer_budget(self, msg):
        customer_id = msg.payload.get('customer_id')
        try:
            customer_model = CustomerModel.get(CustomerModel.id == customer_id)
            customer = Customer.from_model(customer_model)
            message = ActorMessage(payload={'budget': customer.budget})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise Exception("Customer not found.")

    def __get_customer_tickets(self, msg):
        try:
            tickets = []
            customer_model = CustomerModel.get(
                CustomerModel.id == msg.customer_id)
            order_date = msg.payload.get('order_date')
            event_date = msg.payload.get('event_date')
            if order_date:
                ticket_models = TicketModel.select().where(
                    TicketModel.customer_id == customer_model.id, TicketModel.order_date == order_date)
            elif event_date:
                # TODO
                ticket_models = TicketModel.select().where(
                    TicketModel.customer_id == customer_model.id)
            else:
                ticket_models = TicketModel.select().where(
                    TicketModel.customer_id == customer_model.id)
            for ticket_model in ticket_models:
                ticket = Ticket.from_model(ticket_model)
                tickets.append(ticket)
            message = ActorMessage(payload={'tickets': tickets})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise Exception("Customer not found.")

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
            raise Exception("Event not found.")

    def __list_event(self, msg):
        events = []
        event_models = EventModel.select()
        for event_model in event_models:
            event = Event.from_model(event_model)
            events.append(event)
        message = ActorMessage(payload={'events': events})
        self.send(msg.response_to, message)

    def __purchase_event_ticket(self, msg):
        # TODO: check customer budget + try catch
        event_id = msg.payload.get('event_id')
        quantity = msg.payload.get('quantity')
        # try:
        event_model = EventModel.get(EventModel.id == event_id)
        customer_model = CustomerModel.get(CustomerModel.id == msg.customer_id)
        event_customer_ticket_models = TicketModel.select().where(
            TicketModel.customer_id == customer_model.id, TicketModel.event_id == event_model.id)
        event_ticket_models = TicketModel.select().where(
            TicketModel.event_id == event_model.id)
        total_price = event_model.ticket_price * quantity
        budget_after_purchase = customer_model.budget - total_price
        if budget_after_purchase < 0:
            raise Exception("The budget of the customer is not sufficient.")
        if event_model.max_tickets_per_customer < len(event_customer_ticket_models) + quantity:
            raise Exception(("With this purchase the maximum number of tickets per "
                             "customer for this event would be exceeded."))
        if event_model.max_tickets < len(event_ticket_models) + quantity:
            raise Exception(("With this purchase the maximum number of "
                             "tickets for this event would be exceeded."))
        sale_not_started = event_model.sale_start_date > date.today()
        sale_end_date = event_model.sale_start_date + \
            timedelta(days=event_model.sale_period)
        sale_over = sale_end_date < date.today()
        if sale_not_started or sale_over:
            raise Exception(
                "Currently no tickets can be purchased for this event.")
        customer_model.budget = budget_after_purchase
        customer_model.save()
        ticket = Ticket(id=None, order_date=date.today(),
                        customer_id=customer_model.id, event_id=event_model.id)
        for _ in range(quantity):
            ticket_model = Ticket.to_model(ticket)
            ticket_model.save()
        self.send(msg.response_to, ActorMessage())
        # except DoesNotExist:
        #     raise Exception("Event not found.")

    def __get_event_tickets(self, msg):
        event_id = msg.payload.get('event_id')
        try:
            tickets = []
            event_model = EventModel.get(EventModel.id == event_id)
            ticket_models = TicketModel.select().where(
                TicketModel.event_id == event_model.id)
            for ticket_model in ticket_models:
                ticket = Ticket.from_model(ticket_model)
                tickets.append(ticket)
            message = ActorMessage(payload={'tickets': tickets})
            self.send(msg.response_to, message)
        except DoesNotExist:
            raise Exception("Event not found.")
