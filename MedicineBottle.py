import datetime


class MedicineBottle:
    bottle_name = ""
    list_of_times = []

    drug_information = {}  # Plan here is name :information

    def __init__(self, bottle_name: str, drug_name: str, drug_dosage: str):
        self.bottle_name = bottle_name
        self.drug_information.update({"Name": drug_name})
        self.drug_information.update({"Dosage": drug_dosage})

    def catalog_time(self, time_of_access: datetime):
        pass








