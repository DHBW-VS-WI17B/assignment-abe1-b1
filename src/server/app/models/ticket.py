from peewee import DateField, ForeignKeyField, AutoField
from app.models.base_model import BaseModel
from app.models.customer import Customer
from app.models.event import Event


class Ticket(BaseModel):
    id = AutoField()
    order_date = DateField()
    customer = ForeignKeyField(Customer)
    event = ForeignKeyField(Event)
