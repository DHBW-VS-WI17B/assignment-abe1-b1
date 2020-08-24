from dataclasses import dataclass
from app.models.customer import Customer as CustomerModel


@dataclass
class Customer:

    def __init__(self, id, name, budget, address):
        self.id = id
        self.name = name
        self.budget = budget
        self.address = address

    @staticmethod
    def from_json(json):
        id = json.get('id')
        name = json.get('name')
        budget = json.get('budget')
        address = json.get('address')
        customer = Customer(id=id, name=name, budget=budget, address=address)
        return customer

    @staticmethod
    def to_dict(customer):
        id = customer.id
        name = customer.name
        budget = customer.budget
        address = customer.address
        customer_dict = {'id': id, 'name': name,
                         'budget': budget, 'address': address}
        return customer_dict

    @staticmethod
    def from_model(model):
        id = model.id
        name = model.name
        budget = model.budget
        address = model.address
        customer = Customer(id=id, name=name, budget=budget, address=address)
        return customer

    @staticmethod
    def to_model(customer):
        id = customer.id
        name = customer.name
        budget = customer.budget
        address = customer.address
        customer_model = CustomerModel(id=id, name=name,
                                       budget=budget, address=address)
        return customer_model
