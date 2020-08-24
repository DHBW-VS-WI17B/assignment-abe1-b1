from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Event:
    def __init__(self, args):
        self.name = args.name
        self.date = args.date
        self.location = args.location
        self.max_tickets = args.max_tickets
        self.max_tickets_per_customer = args.max_tickets_per_customer
        self.sale_period = args.sale_period
        self.sale_start_date = args.sale_start_date
        self.price = args.ticket_price
        
    def get_table(self, data):
        headers = ["Name","Date0", "Location", "Price", "Max Tickets", "Max Tickets per Customer", "Sales Period", "Sale Startdate"]
        print(tabulate(data.items(), headers=headers, floatfmt=".4f"))