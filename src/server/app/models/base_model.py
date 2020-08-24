from peewee import SqliteDatabase, Model
from app.config.config import Config

db = SqliteDatabase('server.db')


class BaseModel(Model):
    class Meta:
        database = db
