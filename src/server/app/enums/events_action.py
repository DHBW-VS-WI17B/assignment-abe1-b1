from enum import Enum, unique


@unique
class EventsActorAction(Enum):
    EVENTS_LIST = 'EVENTS_LIST'
    EVENTS_ADD = 'EVENTS_ADD'
    EVENTS_GET = 'EVENTS_GET'
    EVENTS_TICKETS = 'EVENTS_TICKETS'
    EVENTS_PURCHASE = 'EVENTS_PURCHASE'
