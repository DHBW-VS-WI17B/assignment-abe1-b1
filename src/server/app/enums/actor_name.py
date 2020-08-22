from enum import Enum, unique


@unique
class ActorName(Enum):
    """Global actor names."""
    EVENTS_ACTOR = 'EVENTS_ACTOR'
    CUSTOMERS_ACTOR = 'CUSTOMERS_ACTOR'
    DB_ACTOR = 'DB_ACTOR'
