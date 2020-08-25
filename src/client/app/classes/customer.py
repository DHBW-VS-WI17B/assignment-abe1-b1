from dataclasses import dataclass
from tabulate import tabulate
from app.utils.date  import DateHelper

@dataclass
class Customer:
    def __init__(self, args):
        self.name = args.name
        self.budget = args.budget
        self.address = args.address
    
    @staticmethod
    def print_table_budget(data):
        table = []
        for item in data:
            table.append([
                item['budget']
            ])
        headers = ["Budget"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))
        