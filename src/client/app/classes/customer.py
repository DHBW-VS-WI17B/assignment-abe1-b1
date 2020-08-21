from dataclasses import dataclass

@dataclass
class Customer:
    def __init__(self, args):
        self.name = args.name
        self.budget = args.budget
        self.address = args.address
        