from dataclasses import dataclass
from datetime import datetime
from app.models.ticket import Ticket as TicketModel


@dataclass
class Ticket:
    def __init__(self, id, order_date, customer_id, event_id):
        self.id = id
        self.order_date = order_date
        self.customer_id = customer_id
        self.event_id = event_id

    @staticmethod
    def to_dict(ticket):
        id = ticket.id
        order_date = datetime.timestamp(datetime(
            ticket.order_date.year, ticket.order_date.month, ticket.order_date.day))
        customer_id = ticket.customer_id
        event_id = ticket.event_id
        ticket_dict = {'id': id, 'order_date': order_date,
                       'customer_id': customer_id, 'event_id': event_id}
        return ticket_dict

    @staticmethod
    def from_model(model):
        id = model.id
        order_date = model.order_date
        customer_id = model.customer_id
        event_id = model.event_id
        ticket = Ticket(id=id, order_date=order_date,
                        customer_id=customer_id, event_id=event_id)
        return ticket

    @staticmethod
    def to_model(ticket):
        id = ticket.id
        order_date = ticket.order_date
        customer_id = ticket.customer_id
        event_id = ticket.event_id
        ticket_model = TicketModel(id=id, order_date=order_date,
                                   customer_id=customer_id, event_id=event_id)
        return ticket_model
