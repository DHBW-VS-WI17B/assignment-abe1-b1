"""Customer
"""
import itertools

class Customer:
    """Customer
    """
    id_iter = itertools.count()

    def __init__(self, name, budget, address):
        """ initialize object

        Args:
            name ([string]): name of the customer
            budget ([int]): budget of the customer for tickets
            address ([string]): address of the customer
        """
        self.customer_id = next(self.id_iter)
        self.name = name
        self.budget = budget
        self.address = address

    @staticmethod
    def from_json(json):
        """ deserialize customer from json

        Args:
            json ([json]): customer json
        Returns:
            [Customer]: deserialized customer object
        """
        customer_id = json.get('customer_id')
        budget = json.get('budget')
        name = json.get('name')
        address = json.get('address')
        customer = Customer(customer_id, name, budget, address)
        return customer
