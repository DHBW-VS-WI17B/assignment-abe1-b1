from thespian.actors import Actor
from app.enums.customers_actor_action import CustomersActorAction


class CustomersActor(Actor):
    """Customers Actor

    Args:
        Actor (Actor)
    """
    customers = []

    def receiveMessage(self, msg, sender):
        """ Message handler

        Args:
            msg (ActorMessage): message from client
            sender (): sender
        """
        if msg.action == CustomersActorAction.CUSTOMERS_GET:
            ret_value = None
            for customer in self.customers:
                if customer.id == msg.payload.get('customer_id'):
                    ret_value = customer
                    break
            self.send(sender, ret_value)
        if msg.action == CustomersActorAction.CUSTOMERS_ADD:
            customer = msg.get('customer')
            self.customers.append(customer)
        if msg.get("action") == CustomersActorAction.CUSTOMERS_BUDGET:
            ret_value = None
            for customer in self.customers:
                if customer.id == msg.payload.get('customer_id'):
                    ret_value = customer.budget
                    break
            self.send(sender, ret_value)
        if msg.get("action") == CustomersActorAction.CUSTOMERS_TICKETS:
            ret_value = None
            for customer in self.customers:
                if customer.id == msg.payload.get('customer_id'):
                    print('TODO')
