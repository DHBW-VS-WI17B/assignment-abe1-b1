from enum import Enum, unique


@unique
class ActorName(Enum):
    EVENT_ACTOR = 1
    CUSTOMER_ACTOR = 2
