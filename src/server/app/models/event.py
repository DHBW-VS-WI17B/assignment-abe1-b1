from peewee import CharField, IntegerField, DateField, AutoField
from app.models.base_model import BaseModel


class Event(BaseModel):
    id = AutoField()
    name = CharField()
    date = DateField()
    location = CharField()
    ticket_price = IntegerField()
    max_tickets = IntegerField()
    max_tickets_per_customer = IntegerField()
    sale_start_date = DateField()
    sale_period = IntegerField()
