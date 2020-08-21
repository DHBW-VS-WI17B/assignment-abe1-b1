from dataclasses import dataclass

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
        