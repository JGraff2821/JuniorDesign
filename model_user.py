# Packages
from mongoengine import *
from datetime import datetime
from pydantic import validator
from pydantic.main import BaseModel

# OtherDirectoryFiles
from model_medbottle import Medicine_Bottle

connect("juniordesign")


class User(Document):
    name = StringField(required=True, unique=True)
    hashed_password = StringField(required=True)
    email = StringField(required=True)
    medicine_bottles = ListField()  # What is the data type inside here?
    alarms = ListField(DateField)

    @classmethod
    def request_user_from_email(cls, email: str):
        return User.objects(email=email).first()

    @classmethod
    def login_user(cls, email: str, password: str):
        user_found = False
        user = cls.request_user_from_email(email)
        if user is not None:
            if user.hashed_password == password:
                user_found = True
        if user_found:
            return user
        return None

    def dump_account_information(self):
        return {
            "name": self.name,
            "hashed_password": self.hashed_password,
            "email": self.email,
            "medicine_bottles": self.medicine_bottles,
            "alarms": self.alarms,
        }

    def update_name(self, name: str):
        NewUserRequest.validate_name(name)
        self.name = name
        self.save()
        return f"Name Updated, {self.name}"

    def update_password(self, password: str):
        NewUserRequest.validate_hashed_password(password)
        self.hashed_password = password
        self.save()
        return f"Password Updated, {self.hashed_password}"

    def add_medicine_bottle(self, bottle_name: str, drug_name: str, drug_dosage: str):
        meds_to_add = {
            "bottle_name":bottle_name,
            "drug_name":drug_name,
            "drug_dosage":drug_dosage
        }
        for bottle in self.medicine_bottles:
            if bottle.bottle_name == meds_to_add["bottle_name"]:
                return "Bottle not added, must have unique name."
        self.medicine_bottles.append(meds_to_add)
        self.save()
        print("Added Medicine Bottle To:", self.name)
        return f"Added Medicine Bottle To: {self.name}"

    def add_alarm(self, time_of_alarm: datetime):
        self.alarms.append(time_of_alarm)

    def notify_user(self):  # No Idea here, may eventually be its own class
        pass


class NewUserRequest(BaseModel):
    email: str
    name: str
    hashed_password: str

    @validator("email")
    def validate_email(cls, v):
        u = User.objects(email=v).first()
        if u is not None:
            raise ValueError("Cannot have duplicate email")
        print(f"Validated email, argument: {v}")
        return v

    @validator("name")
    def validate_name(cls, v):
        if len(str(v)) > 15:
            raise ValueError("Name may not be longer than 15 char")
        print(f"Validated Name, argument {v}")
        return v

    @validator("hashed_password")
    def validate_hashed_password(cls, v):
        if len(str(v)) < 5:
            raise ValueError("Password must be at least 5 char")
        print(f"Validated password, argument {v}")
        return v


# if __name__ == '__main__':
#     # connect("juniordesign")
#     User.objects.delete() #Take this out in presentation?
#
#
#     NewUserRequest(email="graffJ@jbu.edu", username = "Josh G", hashed_password = "123456")
#     Josh = User(username="Josh", hashed_password="Graff", email="graffJ@jbu.edu")
#     Josh.save()
# # NewUserRequest(email="graffJ@jbu.edu", username="Josh G", hashed_password="123456")
# Josh.add_medicine_bottle(bottle_name="Allergy Medicine",drug_name="fsadfw1213",drug_dosage="2mg")
