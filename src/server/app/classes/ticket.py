import itertools
from dataclasses import dataclass


@dataclass
class Ticket:
    id_iter = itertools.count()
    
    def __init__(self, order_date, customer_id, event_id):
        self.id = next(self.id_iter)
        self.order_date = order_date
        self.customer_id = customer_id
        self.event_id = event_id
