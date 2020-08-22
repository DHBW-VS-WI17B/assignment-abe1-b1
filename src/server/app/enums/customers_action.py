from enum import Enum, unique


@unique
class CustomersActorAction(Enum):
    CUSTOMERS_ADD = 'CUSTOMERS_ADD'
    CUSTOMERS_BUDGET = 'CUSTOMERS_BUDGET'
    CUSTOMERS_TICKETS = 'CUSTOMERS_TICKETS'
