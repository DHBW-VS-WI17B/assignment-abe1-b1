from thespian.actors import Actor
from app.enums.events_action import EventsActorAction
from app.actors.db_actor import DbActor
from app.enums.actor_name import ActorName
from app.classes.actor_message import ActorMessage
from app.models.event import Event
from app.config.config import Config


class EventsActor(Actor):

    def receiveMessage(self, msg, sender):
        if not isinstance(msg, ActorMessage):
            return
        action = msg.action
        payload = msg.payload
        customer_id = msg.customer_id
        response_to = msg.response_to
        if action == EventsActorAction.EVENTS_ADD:
            db_actor = self.createActor(
                actorClass=DbActor, globalName=ActorName.DB_ACTOR)
            message = ActorMessage(
                action=action, payload=payload, customer_id=customer_id)
            self.send(db_actor, message)
        if action == EventsActorAction.EVENTS_GET:
            db_actor = self.createActor(actorClass=DbActor)
            message = ActorMessage(
                action=action, payload=payload, customer_id=customer_id, response_to=sender)
            self.send(db_actor, message)
        if action == EventsActorAction.EVENTS_LIST:
            db_actor = self.createActor(actorClass=DbActor)
            message = ActorMessage(
                action=action, payload=payload, customer_id=customer_id, response_to=sender)
            self.send(db_actor, message)
        if action == EventsActorAction.EVENTS_PURCHASE:
            db_actor = self.createActor(
                actorClass=DbActor, globalName=ActorName.DB_ACTOR)
            message = ActorMessage(
                action=action, payload=payload, customer_id=customer_id)
            self.send(db_actor, message)
        if action == EventsActorAction.EVENTS_TICKETS:
            db_actor = self.createActor(actorClass=DbActor)
            message = ActorMessage(
                action=action, payload=payload, customer_id=customer_id, response_to=sender)
            self.send(db_actor, message)
