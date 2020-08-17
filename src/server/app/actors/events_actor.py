from thespian.actors import Actor
from app.enums.events_actor_action import EventsActorAction


class EventsActor(Actor):
    events = []

    def receiveMessage(self, message, sender):
        if message.action == EventsActorAction.EVENTS_LIST:
            self.send(sender, self.events)
        if message.action == EventsActorAction.EVENTS_ADD:
            event = message.payload.get('event')
            self.events.append(event)
        if message.action == EventsActorAction.EVENTS_GET:
            ret_value = None
            for event in self.events:
                if event.id == message.payload.get('event_id'):
                    ret_value = event
                    break
            self.send(sender, ret_value)
        if message.action == EventsActorAction.EVENTS_TICKETS:
            # TODO
            print('TODO')
        if message.action == EventsActorAction.EVENTS_PURCHASE:
            # TODO
            print('TODO')
