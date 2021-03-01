from umongo.fields import StringField, ListField, DictField

from db import instance
from umongo import Document


@instance.register
class User(Document):
    username: str = StringField(required=True)
    hashed_password = StringField(required=True)
    email = StringField(required=True)
    dictionary_medicine_bottles = DictField(default=dict)
    list_of_timers = ListField(default=list)
    list_of_alarms = ListField(default=list)
