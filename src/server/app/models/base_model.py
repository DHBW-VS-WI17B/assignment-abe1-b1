from peewee import SqliteDatabase, Model


db = SqliteDatabase('file::memory:?cache=shared')


class BaseModel(Model):
    class Meta:
        database = db
