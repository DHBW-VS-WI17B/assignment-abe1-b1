from thespian.actors import Actor
from app.enums.customers_action import CustomersActorAction
from app.enums.events_action import EventsActorAction


class DbActor(Actor):

    def receiveMessage(self, msg, sender):
        if msg.action == CustomersActorAction.CUSTOMERS_ADD:
            print('TODO')
        if msg.action == CustomersActorAction.CUSTOMERS_BUDGET:
            print('TODO')
        if msg.action == CustomersActorAction.CUSTOMERS_TICKETS:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_ADD:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_GET:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_LIST:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_PURCHASE:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_TICKETS:
            print('TODO')
