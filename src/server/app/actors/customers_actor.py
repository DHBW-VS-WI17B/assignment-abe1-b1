from thespian.actors import Actor
from app.enums.customers_action import CustomersActorAction


class CustomersActor(Actor):

    def receiveMessage(self, msg, sender):
        if msg.action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
        if msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
