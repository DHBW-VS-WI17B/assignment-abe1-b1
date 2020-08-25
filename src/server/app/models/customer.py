from peewee import CharField, IntegerField, AutoField
from app.models.base_model import BaseModel


class Customer(BaseModel):
    id = AutoField()
    name = CharField()
    budget = IntegerField()
    address = CharField()
