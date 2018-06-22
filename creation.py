from mongoengine import *

connect("phonebook")

class User(Document):
    name = StringField(required=True)
    phone = IntField(required=True)
