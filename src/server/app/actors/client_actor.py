from thespian.actors import Actor
from app.enums.customers_action import CustomersActorAction
from app.enums.events_action import EventsActorAction


class ClientActor(Actor):

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
        if action == EventsActorAction.EVENTS_ADD:
            print('TODO')
        if action == EventsActorAction.EVENTS_GET:
            print('TODO')
        if action == EventsActorAction.EVENTS_LIST:
            print('TODO')
        if action == EventsActorAction.EVENTS_PURCHASE:
            print('TODO')
        if action == EventsActorAction.EVENTS_TICKETS:
            print('TODO')
