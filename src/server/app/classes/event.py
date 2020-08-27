from dataclasses import dataclass
from datetime import datetime
from app.models.event import Event as EventModel


@dataclass
class Event:

    def __init__(self, id, name, date, location, ticket_price, max_tickets,
                 max_tickets_per_customer, sale_start_date, sale_period):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.ticket_price = ticket_price
        self.max_tickets = max_tickets
        self.max_tickets_per_customer = max_tickets_per_customer
        self.sale_start_date = sale_start_date
        self.sale_period = sale_period

    @staticmethod
    def from_json(json):
        """Create event object from JSON dictionary."""
        id = json.get('id')
        name = json.get('name')
        date = datetime.fromtimestamp(json.get('date')).date()
        location = json.get('location')
        ticket_price = json.get('ticket_price')
        max_tickets = json.get('max_tickets')
        max_tickets_per_customer = json.get('max_tickets_per_customer')
        sale_start_date = datetime.fromtimestamp(
            json.get('sale_start_date')).date()
        sale_period = json.get('sale_period')
        event = Event(id=id, name=name, date=date, location=location, ticket_price=ticket_price,
                      max_tickets=max_tickets, max_tickets_per_customer=max_tickets_per_customer,
                      sale_start_date=sale_start_date, sale_period=sale_period)
        return event

    @staticmethod
    def to_dict(event):
        """Create dictionary from event object."""
        id = event.id
        name = event.name
        date = datetime.timestamp(datetime(
            event.date.year, event.date.month, event.date.day))
        location = event.location
        ticket_price = event.ticket_price
        max_tickets = event.max_tickets
        max_tickets_per_customer = event.max_tickets_per_customer
        sale_start_date = datetime.timestamp(datetime(
            event.sale_start_date.year, event.sale_start_date.month, event.sale_start_date.day))
        sale_period = event.sale_period
        event_dict = {'id': id, 'name': name, 'date': date, 'location': location,
                      'ticket_price': ticket_price, 'max_tickets': max_tickets,
                      'max_tickets_per_customer': max_tickets_per_customer,
                      'sale_start_date': sale_start_date, 'sale_period': sale_period}
        return event_dict

    @staticmethod
    def from_model(model):
        """Create event object from database model."""
        id = model.id
        name = model.name
        date = model.date
        location = model.location
        ticket_price = model.ticket_price
        max_tickets = model.max_tickets
        max_tickets_per_customer = model.max_tickets_per_customer
        sale_start_date = model.sale_start_date
        sale_period = model.sale_period
        event = Event(id=id, name=name, date=date, location=location,
                      ticket_price=ticket_price, max_tickets=max_tickets,
                      max_tickets_per_customer=max_tickets_per_customer,
                      sale_start_date=sale_start_date, sale_period=sale_period)
        return event

    @staticmethod
    def to_model(event):
        """Create database model from event object."""
        id = event.id
        name = event.name
        date = event.date
        location = event.location
        ticket_price = event.ticket_price
        max_tickets = event.max_tickets
        max_tickets_per_customer = event.max_tickets_per_customer
        sale_start_date = event.sale_start_date
        sale_period = event.sale_period
        event_model = EventModel(id=id, name=name, date=date, location=location,
                                 ticket_price=ticket_price, max_tickets=max_tickets,
                                 max_tickets_per_customer=max_tickets_per_customer,
                                 sale_start_date=sale_start_date, sale_period=sale_period)
        return event_model
