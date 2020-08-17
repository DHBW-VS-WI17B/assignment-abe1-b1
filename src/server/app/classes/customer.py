import itertools

class Customer:
    id_iter = itertools.count()

    def __init__(self, id, name, budget, address):
        self.id = id
        self.name = name
        self.budget = budget
        self.address = address

    @staticmethod
    def from_json(json):
        id = json.get('id')
        budget = json.get('budget')
        name = json.get('name')
        address = json.get('address')
        customer = Customer(id, name, budget, address)
        return customer

