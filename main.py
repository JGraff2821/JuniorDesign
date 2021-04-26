import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from model_user import User
from model_medbottle import Medicine_Bottle
from mongoengine import *


if __name__ == '__main__':
    User.objects.delete()  # Take this out in presentation?

    uvicorn.run("app:app", port=8001, reload=True, host="0.0.0.0")
