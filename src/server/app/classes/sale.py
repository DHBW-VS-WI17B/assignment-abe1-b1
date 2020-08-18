import itertools
from dataclasses import dataclass


@dataclass
class Sale:
    id_iter = itertools.count()

    def __init__(self, start_date, period):
        self.id = next(self.id_iter)
        self.start_date = start_date
        self.period = period
