from thespian.actors import Actor
from app.enums.customers_actor_action import CustomersActorAction


class CustomersActor(Actor):
    customers = []

    def receiveMessage(self, message, sender):
        if message.get("action") == CustomersActorAction.CUSTOMERS_ADD:
            customer = message.get("payload")
            self.customers.append(customer)
        if message.get("action") == CustomersActorAction.CUSTOMERS_BUDGET:
            ret_value = None
            id = int(message.get("payload"))
            for customer in self.customers:
                if customer.get('id') == id:
                    ret_value = customer.budget
                    break
            self.send(sender, ret_value)
        if message.get("action") == CustomersActorAction.CUSTOMERS_TICKETS:
            ret_value = None
            #Create specific object instead of int
            payload = int(message.get("payload"))
            tickets = []
            for customer in self.customers:
                if customer.get('id') == payload_id:
                    for ticket in customer.tickets:
                        if ticket.get('order_date') == payload.order_date 
                            if ticket.get('event_date') == payload.event_date
                                tickets.append(ticket) 
                    break
            self.send(sender, tickets)
