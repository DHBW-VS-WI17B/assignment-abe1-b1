from peewee import CharField, AutoField, FloatField
from app.models.base_model import BaseModel


class Customer(BaseModel):
    id = AutoField()
    name = CharField()
    budget = FloatField()
    address = CharField()
