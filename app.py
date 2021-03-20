from fastapi import FastAPI

app2 = FastAPI(title="Junior Design Project")


@app2.get("/hello_world")
def hello_world_ep(name: str):
    return {"msg": "hello "+name}
