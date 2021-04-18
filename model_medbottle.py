
from mongoengine import *
from pydantic import validator
from pydantic.main import BaseModel


class Medicine_Bottle(Document):
    bottle_name = StringField(required=True)
    drug_name = StringField(required=True)
    drug_dosage = IntField(required=True)
    # list_of_times = ListField(default=list)
    # drug_information = DictField(default=dict)

class NewMedBottleRequest(BaseModel):
    bottle_name:str
    drug_name:str
    drug_dosage:int

    @validator("drug_dosage")
    def validate_bottle_name(cls, v):
        if v<0:
            raise ValueError("Interger describing dosage must be positive.")
        print(f"validated dosage amount {v}")
        return v




