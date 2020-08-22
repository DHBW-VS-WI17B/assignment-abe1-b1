from thespian.actors import Actor
from app.enums.events_action import EventsActorAction


class EventsActor(Actor):

    def receiveMessage(self, msg, sender):
        action = msg.action
        payload = msg.payload
        customer_id = msg.customer_id
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
