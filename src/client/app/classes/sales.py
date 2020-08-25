from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Sales:
    @staticmethod
    def print_table(data):
        table = []
        for item in data:
            table.append([
                item['id'],
                item['name'], 
                item['sales'] 
            ])
        headers = ["ID", "Name", "Sales"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))