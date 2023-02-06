from peewee import *


db = PostgresqlDatabase('bookmarks', user='justinozkan',
                        password='justin30', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Mark(BaseModel):
    url =  TextField()
    description = TextField()

db.drop_tables([Mark])
db.create_tables([Mark])


nyt = Mark(url='https://www.nytimes.com/', description='New York Times')
nyt.save()