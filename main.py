from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

    # class MedicineBottle(BaseModel):
    #     bottle_name: str
    #     drug_name: str
    #     drug_dosage: str
    #     list_of_times: list
    #     drug_information: dict
    #
    # app = FastAPI()
    #
    #
    # @app.get("/")
    # async def root():
    #     return {"message": "Hello World"}
    #
    #
    # @app.post("/NewMedicineBottle/")
    # async def create_medicine_bottle(new_med : MedicineBottle):
    #     return new_med
    #
    # uvicorn.run("app:app", reload=True)
