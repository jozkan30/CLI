from peewee import *
from playhouse.shortcuts import model_to_dict


db = PostgresqlDatabase('bookmarks', user='justinozkan',
                        password='justin30', host='localhost', port=5432)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Mark(BaseModel):
    url = TextField()
    description = TextField()


db.drop_tables([Mark])
db.create_tables([Mark])


nyt = Mark(url='https://www.nytimes.com/', description='New York Times')
nyt.save()

github = Mark(url='https://github.com/', description='GitHub')
github.save()

amazon = Mark(url='https://www.amazon.com/', description='Amazon ')
amazon.save()

# Add a Bookmark(CREATE)
def add_bookmark():
    add_url = input("Please enter a valid URl")
    add_description = input("Please enter a description")
    add_new_mark = Mark(url=add_url, description=add_description)
    add_new_mark.save()
    print("Bookmark Added!")


def exit():
    print("Thanks for stopping by!")


def intro():
    print("Pleae try again!")

def delete(id):
    req_id = input("What is ID of the bookmark you would like to delete? ")
    find = Mark.get(Mark.id == id)
    remove = Mark.delete_instance(find) 
    print(f' Bookmark {id} eliminated!')


print("Would you like to add a URl Please type 'yes' , 'no' or 'list, to view all entries' or 'del ")

make = str(input()).lower()
if make == 'yes':
    add_bookmark()
elif make == 'no':
    exit()
 # View All Entries (READ)   
elif make == 'list':
    mark_list = []
    for mark in Mark.select():
        mark_list.append(model_to_dict(mark))
        print(mark_list)
