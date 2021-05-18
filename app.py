from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from auth import (
    app,
    Token,
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user,
)
from model_medbottle import Medicine_Bottle
from model_user import *
from model_medbottle import *


app = FastAPI(title="Junior Design Project")
app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Medi-Cap Base Root"}


@app.post("/User/ListAll")
def list_all_accounts():

    for user in User.objects:
        yield user.dump_account_information()



@app.post("/User/Create")
async def create_user(name: str, email: str, password: str):
    NewUserRequest(email=email, name=name, hashed_password=password)
    new_user = User(email=email, name=name, hashed_password=password)
    new_user.save()

    return "User Created"


@app.post("/User/ReadAccount")
async def read_user(email: str, password: str):
    user = User.login_user(email, password)
    return user.dump_account_information()


@app.post("/User/UpdateAccount")
async def update_user(
    email: str, current_password: str, new_password: str = None, new_name: str = None
):
    user: User = User.login_user(email, current_password)
    if user is not None:
        # This request will only update one attribute at a time.
        if new_password is not None:
            return user.update_password(new_password)
        if new_name is not None:
            return user.update_name(new_name)
    return "No account Changed"


@app.post("/User/DeleteAccount")
def delete_user(email: str, password: str):
    user: User = User.login_user(email, password)
    user.delete()
    return "User Deleted"


@app.post("/User/CreateMedicineBottle")
async def add_med_bottle(req: NewMedBottleRequest, user=Depends(get_current_user)):
    if user is not None:
        response = user.add_medicine_bottle(
            req.bottle_name, req.drug_name, req.drug_dosage
        )
        return f"Account Found:{response}"
    else:
        return "Account Not Found."


# If the request is able to login, it will return the User's Account.
@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
