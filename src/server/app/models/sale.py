from peewee import DateField, IntegerField, AutoField
from app.models.base_model import BaseModel


class Sale(BaseModel):
    # TODO
    id = AutoField()
    start_date = DateField()
    period = IntegerField()
