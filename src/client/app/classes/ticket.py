from dataclasses import dataclass
from tabulate import tabulate
from app.utils.date import DateHelper


@dataclass
class Ticket:
    @staticmethod
    def print_table(data):
        table = []
        for item in data:
            table.append([
                item['id'],
                DateHelper.timestamp_to_date(item['order_date']),
                item['customer_id'],
                item['event_id']
            ])
        headers = ["Ticket ID", "Order date", "Customer ID", "Event ID"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))
