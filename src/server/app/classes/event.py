import itertools


class Event:
    id_iter = itertools.count()

    def __init__(self, name, date, location, price, max_tickets, max_tickets_per_customer, sale_start_date, sale_period):
        self.id = next(self.id_iter)
        self.name = name
        self.date = date
        self.location = location
        self.price = price
        self.max_tickets = max_tickets
        self.max_tickets_per_customer = max_tickets_per_customer
        self.sale_start_date = sale_start_date
        self.sale_period = sale_period

    @staticmethod
    def from_json(json):
        name = json.get('name')
        date = json.get('date')
        location = json.get('location')
        price = json.get('price')
        max_tickets = json.get('maxTickets')
        max_tickets_per_customer = json.get('maxTicketsPerCustomer')
        sale_start_date = json.get('saleStartDate')
        sale_period = json.get('salePeriod')
        event = Event(name, date, location, price, max_tickets,
                      max_tickets_per_customer, sale_start_date, sale_period)
        return event
