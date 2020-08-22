from enum import Enum, unique


@unique
class ActorName(Enum):
    """Global actor names."""
    DB_ACTOR = 'DB_ACTOR'
