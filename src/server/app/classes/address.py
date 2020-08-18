from dataclasses import dataclass


@dataclass
class Address:
    def __init__(self, name, street, zip_code, city, street_number):
        self.name = name
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.street_number = street_number
