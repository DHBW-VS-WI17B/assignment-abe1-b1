from thespian.actors import Actor
from peewee import SqliteDatabase, DoesNotExist
from app.config.config import Config
from app.enums.customers_action import CustomersActorAction
from app.enums.events_action import EventsActorAction
from app.models.customer import Customer as CustomerModel
from app.models.event import Event as EventModel
from app.models.ticket import Ticket as TicketModel
from app.classes.event import Event
from app.classes.ticket import Ticket
from app.classes.actor_message import ActorMessage
from datetime import datetime


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
        if customer_id:
            # TODO: check if customer exists
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
        if action == EventsActorAction.EVENTS_ADD:
            event = msg.payload.get('event')
            event_model = Event.to_model(event)
            event_model.save()
        if action == EventsActorAction.EVENTS_GET:
            event_id = msg.payload.get('event_id')
            try:
                event_model = EventModel.get(EventModel.id == event_id)
                event = Event.from_model(event_model)
                message = ActorMessage(payload={'event': event})
                self.send(response_to, message)
            except DoesNotExist:
                message = ActorMessage(error="Event not found.")
                self.send(response_to, message)
        if action == EventsActorAction.EVENTS_LIST:
            events = []
            event_models = EventModel.select()
            for event_model in event_models:
                event = Event.from_model(event_model)
                events.append(event)
            message = ActorMessage(payload={'events': events})
            self.send(response_to, message)
        if action == EventsActorAction.EVENTS_PURCHASE:
            # TODO: check customer budget + try catch
            event_id = msg.payload.get('event_id')
            quantity = msg.payload.get('quantity')
            # try:
            tickets = []
            event_model = EventModel.get(EventModel.id == event_id)
            ticket = Ticket(id=None, order_date=datetime.now(),
                            customer_id=customer_id, event_id=event_model.id)
            for i in range(quantity):
                ticket_model = Ticket.to_model(ticket)
                ticket_model.save()
            # except DoesNotExist:
            #     message = ActorMessage(error="Event not found.")
            #     self.send(response_to, message)
        if action == EventsActorAction.EVENTS_TICKETS:
            event_id = msg.payload.get('event_id')
            try:
                tickets = []
                event_model = EventModel.get(EventModel.id == event_id)
                ticket_models = EventModel.select().where(
                    TicketModel.event_id == event_model.id)
                for ticket_model in ticket_models:
                    ticket = Ticket.from_model(ticket_model)
                    tickets.append(ticket)
                message = ActorMessage(payload={'tickets': tickets})
                self.send(response_to, message)
            except DoesNotExist:
                message = ActorMessage(error="Event not found.")
                self.send(response_to, message)
        if not self.globalName:
            self.db.close()
