from thespian.actors import Actor
from app.enums.events_actor_action import EventsActorAction


class EventsActor(Actor):
    events = []

    def receiveMessage(self, message, sender):
        if message.get("action") == EventsActorAction.EVENTS_LIST:
            self.send(sender, self.events)
        if message.get("action") == EventsActorAction.EVENTS_ADD:
            event = message.get("payload")
            self.events.append(event)
        if message.get("action") == EventsActorAction.EVENTS_GET:
            ret_value = None
            id = int(message.get("payload"))
            for event in self.events:
                if event.get('id') == id:
                    ret_value = event
                    break
            self.send(sender, ret_value)
