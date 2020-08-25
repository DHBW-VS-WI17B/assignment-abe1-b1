from enum import Enum, unique


@unique
class ActorName(Enum):
    """Names of actors as Enum

    Args:
        Enum ([Enum])
    """
    EVENTS_ACTOR = 1
    CUSTOMERS_ACTOR = 2
