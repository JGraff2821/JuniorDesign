from fastapi import FastAPI

app = FastAPI(title="Junior Design Project")


@app.get("/hello_world")
def hello_world_ep():
    return {"msg": "hello world"}
