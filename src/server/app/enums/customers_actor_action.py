from enum import Enum, unique


@unique
class CustomersActorAction(Enum):
    CUSTOMERS_ADD = 1
    CUSTOMERS_BUDGET = 2
    CUSTOMERS_TICKETS = 3