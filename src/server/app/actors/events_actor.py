from thespian.actors import Actor
from app.enums.events_action import EventsActorAction


class EventsActor(Actor):
    events = []

    def receiveMessage(self, msg, sender):
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
