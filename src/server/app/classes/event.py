import itertools
from dataclasses import dataclass


@dataclass
class Event:
    id_iter = itertools.count()

    def __init__(self, name, date, location, price, max_tickets, max_tickets_per_customer, sale_id, address_id):
        self.id = next(self.id_iter)
        self.name = name
        self.date = date
        self.location = location
        self.price = price
        self.max_tickets = max_tickets
        self.max_tickets_per_customer = max_tickets_per_customer
        self.sale_id = sale_id
        self.address_id = address_id
