from thespian.actors import Actor
from app.actors.db_actor import DbActor
from app.enums.actor_global_name import ActorGlobalName
from app.enums.customers_action import CustomersActorAction
from app.classes.actor_message import ActorMessage


class CustomersActor(Actor):

    def receiveMessage(self, msg, sender):
        """handle actor messages and call db actor"""
        if not isinstance(msg, ActorMessage):
            return
        if msg.action == CustomersActorAction.CUSTOMERS_ADD:
            db_actor = self.createActor(actorClass=DbActor,
                                        globalName=ActorGlobalName.DB_ACTOR)
            message = ActorMessage(action=msg.action, payload=msg.payload,
                                   customer_id=msg.customer_id, response_to=sender)
            self.send(db_actor, message)
        if msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
            db_actor = self.createActor(actorClass=DbActor)
            message = ActorMessage(action=msg.action, payload=msg.payload,
                                   customer_id=msg.customer_id, response_to=sender)
            self.send(db_actor, message)
        if msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
            db_actor = self.createActor(actorClass=DbActor)
            message = ActorMessage(action=msg.action, payload=msg.payload,
                                   customer_id=msg.customer_id, response_to=sender)
            self.send(db_actor, message)
