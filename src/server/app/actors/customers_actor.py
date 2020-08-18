"""CustomerActor
"""
from thespian.actors import Actor
from app.enums.customers_actor_action import CustomersActorAction


class CustomersActor(Actor):
    """Customers Actor

    Args:
        Actor (Actor)
    """
    customers = []

    def receiveMessage(self, message, sender):
        """ Message handler

        Args:
            message (ActorMessage): message from client
            sender (): sender
        """
        if message.action == CustomersActorAction.CUSTOMERS_GET:
            ret_value = None
            for customer in self.customers:
                if customer.id == message.payload.get('customer_id'):
                    ret_value = customer
                    break
            self.send(sender, ret_value)
        if message.action == CustomersActorAction.CUSTOMERS_ADD:
            customer = message.get('customer')
            self.customers.append(customer)
        if message.get("action") == CustomersActorAction.CUSTOMERS_BUDGET:
            ret_value = None
            for customer in self.customers:
                if customer.id == message.payload.get('customer_id'):
                    ret_value = customer.budget
                    break
            self.send(sender, ret_value)
        if message.get("action") == CustomersActorAction.CUSTOMERS_TICKETS:
            ret_value = None
            for customer in self.customers:
                if customer.id == message.payload.get('customer_id'):
                    print('TODO')
