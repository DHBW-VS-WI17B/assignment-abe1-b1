from enum import Enum, unique


@unique
class EventsActorAction(Enum):
    EVENTS_LIST = 'EVENTS_LIST'
    EVENTS_ADD = 'EVENTS_ADD'
    EVENTS_GET = 'EVENTS_GET'
    EVENTS_SALES = 'EVENTS_SALES'
    EVENTS_PURCHASE_TICKET = 'EVENTS_PURCHASE_TICKET'
