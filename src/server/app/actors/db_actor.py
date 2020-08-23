from thespian.actors import Actor
from peewee import SqliteDatabase
from app.config.config import Config
from app.enums.customers_action import CustomersActorAction
from app.enums.events_action import EventsActorAction
from app.models.customer import Customer as CustomerModel
from app.models.event import Event as EventModel
from app.models.ticket import Ticket as TicketModel
from app.classes.event import Event
from app.classes.actor_message import ActorMessage


class DbActor(Actor):
    db = SqliteDatabase(Config.get('SQLITE_DATABASE'))

    def receiveMessage(self, msg, sender):
        if not isinstance(msg, ActorMessage):
            return
        self.db.connect(reuse_if_open=True)
        action = msg.action
        payload = msg.payload
        customer_id = msg.customer_id
        response_to = msg.response_to
        if msg.action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
            self.db.close()
        if msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
            self.db.close()
        if msg.action == EventsActorAction.EVENTS_ADD:
            event = payload.get('event')
            event_model = EventModel(name=event.name, date=event.date, location=event.location,
                                     ticket_price=event.ticket_price, max_tickets=event.max_tickets,
                                     max_tickets_per_customer=event.max_tickets_per_customer,
                                     sale_start_date=event.sale_start_date, sale_period=event.sale_period)
            event_model.save()
            print(event_model)
        if msg.action == EventsActorAction.EVENTS_GET:
            try:
                print(payload.get('event_id'))
                event_model = EventModel.get(
                    EventModel.id == payload.get('event_id'))
                event = Event.from_model(event_model)
                print(event_model)
            except Exception as ex:
                print('error')
                print(ex)
            self.send(response_to, None)
            self.db.close()
        if msg.action == EventsActorAction.EVENTS_LIST:
            events = []
            event_models = EventModel.select()
            print(event_models)
            for event_model in event_models:
                print(event_model)
                event = Event.from_model(event_model)
                events.append(event)
            self.send(response_to, events)
            self.db.close()
        if msg.action == EventsActorAction.EVENTS_PURCHASE:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_TICKETS:
            print('TODO')
            self.db.close()