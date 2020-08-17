"""ActorName
"""
from enum import Enum, unique


@unique
class ActorName(Enum):
    """Names of actors as Enum

    Args:
        Enum ([Enum])
    """
    EVENT_ACTOR = 1
    CUSTOMER_ACTOR = 2
