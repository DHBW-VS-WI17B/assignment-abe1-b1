from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Sales:
    @staticmethod
    def print_table(data):
        table = []
        for item in data:
            table.append([
                item['event_id'],
                item['event_name'], 
                item['sales'] 
            ])
        headers = ["ID", "Name", "Sales"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))