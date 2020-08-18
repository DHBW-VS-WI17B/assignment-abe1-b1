from enum import Enum, unique


@unique
class CustomersActorAction(Enum):
    """ Action of Customer Actor

    Args:
        Enum ([Enum])
    """
    CUSTOMERS_GET = 1
    CUSTOMERS_ADD = 2
    CUSTOMERS_BUDGET = 3
    CUSTOMERS_TICKETS = 4
