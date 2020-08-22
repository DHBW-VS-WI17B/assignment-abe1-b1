from thespian.actors import Actor
from app.enums.customers_action import CustomersActorAction


class CustomersActor(Actor):

    def receiveMessage(self, msg, sender):
        action = msg.action
        payload = msg.payload
        customer_id = msg.customer_id
        if action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
        if action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
