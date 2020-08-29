from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Customer:
    def __init__(self, args):
        self.name = args.name
        self.budget = args.budget
        self.address = args.address

    @staticmethod
    def print_table_budget(data):
        """Displays the budget of a specific year as table."""
        table = []
        for item in data:
            table.append([
                item['budget']
            ])
        headers = ["Budget (€)"]
        print(tabulate(table, headers=headers, floatfmt=".2f"))
