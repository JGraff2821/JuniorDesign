from fastapi import FastAPI
from model_medbottle import Medicine_Bottle
from model_user import *
from model_medbottle import *



app = FastAPI(title="Junior Design Project")

@app.get("/")
async def root():
    return {"message": "Medi-Cap Base Root"}

@app.get("/User/ListAll")
async def list_all_accounts():
    return_string = "["
    for user in User.objects:
        return_string+= str(user.dump_account_information())+","
    return_string +="]"
    return return_string


@app.get("/User/Create")
async def create_user(name: str, email: str, password: str):
    NewUserRequest(email=email, name=name, hashed_password=password)
    new_user = User(email=email,name=name, hashed_password=password)
    new_user.save()

    return "User Created"


@app.get("/User/ReadAccount")
async  def read_user(email: str, password:str):
    user = User.login_user(email,password)
    return user.dump_account_information()


@app.get("/User/UpdateAccount")
async def update_user(email:str, current_password:str, new_password:str = None, new_name:str = None):
    user:User = User.login_user(email, current_password)
    if user is not None:
        #This request will only update one attribute at a time.
        if new_password is not None:
            return user.update_password(new_password)
        if new_name is not None:
            return user.update_name(new_name)
    return "No account Changed"

@app.get("/User/DeleteAccount")
async  def delete_user(email:str, password:str):
    user:User =User.login_user(email, password)
    user.delete()
    return "User Deleted"




@app.get("/User/CreateMedicineBottle")
async def add_med_bottle(email: str, password: str, bottle_name: str, drug_name: str, drug_dosage: str):
    NewMedBottleRequest(bottle_name=bottle_name, drug_name=drug_name, drug_dosage=drug_dosage)
    user = User.login_user(email, password)
    if user is not None:
        response =user.add_medicine_bottle(bottle_name,drug_name,drug_dosage)
        return f"Account Found:{response}"
    else:
        return "Account Not Found."

#If the request is able to login, it will return the User's Account.
































