from peewee import DateField, AutoField, ForeignKeyField
from app.models.base_model import BaseModel
from app.models.customer import Customer
from app.models.event import Event


class Ticket(BaseModel):
    id = AutoField()
    order_date = DateField()
    customer = ForeignKeyField(Customer, backref='tickets')
    event = ForeignKeyField(Event, backref='tickets')
