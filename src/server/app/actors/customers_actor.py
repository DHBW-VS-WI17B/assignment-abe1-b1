from thespian.actors import Actor
from app.enums.customers_action import CustomersActorAction
from app.classes.actor_message import ActorMessage


class CustomersActor(Actor):

    def receiveMessage(self, msg, sender):
        if not isinstance(msg, ActorMessage):
            return
        action = msg.action
        payload = msg.payload
        customer_id = msg.customer_id
        if action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
