import MedicineBottle
import datetime


class User:
    username = ""
    password = ""
    email = ""
    dictionary_medicine_bottles = {}
    list_of_timers = []
    list_of_alarms = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    # Function to add medicine bottles to the User's dictionary
    def add_medicine_bottle(self, bottle_name: str, drug_name: str, drug_dosage: str):
        self.dictionary_medicine_bottles.update(MedicineBottle(bottle_name, drug_name, drug_dosage))

    def add_timer(self, time_of_timer: int):
        pass

    def notify_user(self):  # No Idea here, may eventually be its own class
        pass

    def add_alarm(self, time_of_timer: datetime):
        pass
