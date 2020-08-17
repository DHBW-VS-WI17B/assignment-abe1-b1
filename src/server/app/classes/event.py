class Event:
    def __init__(self, id, name, date, location, price, max_tickets, max_tickets_per_customer, sale_id, address_id):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.price = price
        self.max_tickets = max_tickets
        self.max_tickets_per_customer = max_tickets_per_customer
        self.sale_id = sale_id
        self.address_id = address_id
