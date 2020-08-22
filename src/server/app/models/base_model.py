from peewee import SqliteDatabase, Model
from app.config.config import Config


db = SqliteDatabase(Config.get('SQLITE_DATABASE'))


class BaseModel(Model):
    class Meta:
        database = db
