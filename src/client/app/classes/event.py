from dataclasses import dataclass
from tabulate import tabulate
from app.utils.date import DateHelper

@dataclass
class Event:
    def __init__(self, args):
        self.name = args.name
        self.date = DateHelper.date_to_timestamp(args.date)
        self.location = args.location
        self.max_tickets = args.max_tickets
        self.max_tickets_per_customer = args.max_tickets_per_customer
        self.sale_period = args.sale_period
        self.sale_start_date = DateHelper.date_to_timestamp(args.sale_start_date)
        self.ticket_price = args.ticket_price

    @staticmethod
    def print_table_admin(data):
        """Displays all information to the given events as table."""
        table = []
        for item in data:
            table.append([
                item['id'],
                item['name'], 
                DateHelper.timestamp_to_date(item['date']), 
                item['location'], 
                item['ticket_price'], 
                item['max_tickets'], 
                item['max_tickets_per_customer'], 
                DateHelper.timestamp_to_date(item['sale_start_date']), 
                item['ticket_price']
            ])
        headers = ["ID", "Name", "Date", "Location", "Price in €", "Max Tickets", "Max Tickets per Customer", "Sales Startdate", "Sales Period in Days"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))
    
    @staticmethod
    def print_table_customer(data):
        """Displays parts of the information to the given events as table."""
        table = []
        for item in data:
            table.append([
                item['id'],
                item['name'],
                DateHelper.timestamp_to_date(item['date']), 
                item['location'], 
                item['ticket_price']
            ])
        headers = ["ID", "Name", "Date", "Location", "Price in €"]
        print(tabulate(table, headers=headers, floatfmt=".4f"))
