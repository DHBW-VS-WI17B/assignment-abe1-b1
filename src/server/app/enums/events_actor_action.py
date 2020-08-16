from enum import Enum, unique


@unique
class EventsActorAction(Enum):
    EVENTS_LIST = 1
    EVENTS_ADD = 2
    EVENTS_GET = 3
    EVENTS_GET_TICKETS = 4
    EVENTS_PURCHASE = 5
