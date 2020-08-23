from peewee import DateField, AutoField, IntegerField
from app.models.base_model import BaseModel
from app.models.customer import Customer
from app.models.event import Event


class Ticket(BaseModel):
    id = AutoField()
    order_date = DateField()
    customer_id = IntegerField()
    event_id = IntegerField()
