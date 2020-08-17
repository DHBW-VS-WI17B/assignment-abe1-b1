import itertools
from dataclasses import dataclass


@dataclass
class Customer:
    id_iter = itertools.count()

    def __init__(self, id, name, budget, address_id):
        self.id = next(self.id_iter)
        self.name = name
        self.budget = budget
        self.address_id = address_id
