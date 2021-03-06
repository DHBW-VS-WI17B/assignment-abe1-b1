from dataclasses import dataclass


@dataclass
class Arguments:
    def __init__(self, args):
        """Convert args dictionary to args object."""
        self.address = args.get('--address')
        self.budget = args.get('--budget')
        self.year = args.get('--year')
        self.date = args.get('--date')
        self.event_date = args.get('--event-date')
        self.help = args.get('--help')
        self.ip = args.get('--ip')
        self.location = args.get('--location')
        self.max_tickets = args.get('--max-tickets')
        self.max_tickets_per_customer = args.get('--max-tickets-per-customer')
        self.name = args.get('--name')
        self.order_date = args.get('--order-date')
        self.port = args.get('--port')
        self.quantity = args.get('--quantity')
        self.sale_period = args.get('--sale-period')
        self.sale_start_date = args.get('--sale-start-date')
        self.ticket_price = args.get('--ticket-price')
        self.version = args.get('--version')
        self.customer_id = args.get('<customer-id>')
        if args.get('<event-id>') is None:
            self.event_id = args.get('--event-id')
        else:
            self.event_id = args.get('<event-id>')
        self.add = args.get('add')
        self.admin = args.get('admin')
        self.get_budget = args.get('budget')
        self.customer = args.get('customer')
        self.event = args.get('event')
        self.info = args.get('info')
        self.list = args.get('list')
        self.purchase = args.get('purchase')
        self.sales = args.get('sales')
        self.ticket = args.get('ticket')
