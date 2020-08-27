from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Sales:
    @staticmethod
    def print_table(data):
        """Displays the sales of all events as table."""
        table = []
        for item in data:
            table.append([
                item['event_id'],
                item['event_name'],
                item['sales']
            ])
        headers = ["Event ID", "Event name", "Number of sales"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))
