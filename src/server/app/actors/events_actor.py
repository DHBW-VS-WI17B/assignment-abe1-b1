from thespian.actors import Actor
from app.enums.events_actor_action import EventsActorAction


class EventsActor(Actor):
    events = []

    def receiveMessage(self, msg, sender):
        if msg.action == EventsActorAction.EVENTS_LIST:
            self.send(sender, self.events)
        if msg.action == EventsActorAction.EVENTS_ADD:
            event = msg.payload.get('event')
            self.events.append(event)
        if msg.action == EventsActorAction.EVENTS_GET:
            ret_value = None
            for event in self.events:
                if event.id == msg.payload.get('event_id'):
                    ret_value = event
                    break
            self.send(sender, ret_value)
        if msg.action == EventsActorAction.EVENTS_TICKETS:
            print('TODO')
        if msg.action == EventsActorAction.EVENTS_PURCHASE:
            print('TODO')
