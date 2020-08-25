from enum import Enum, unique


@unique
class ActorGlobalName(Enum):
    """Global actor names."""
    DB_ACTOR = 'DB_ACTOR'
