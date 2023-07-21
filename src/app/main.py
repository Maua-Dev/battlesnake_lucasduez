from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "apiversion": "1",
        "author": "Lucas-Duez",
        "color": "#888888",
        "head": "default",
        "tail": "default",
        "version": "0.0.1-pre-alpha"
    }

@app.post("/move")
def move_snake(request: dict):
    return {
        "move": "right",
        "shout": "only right"
        }


handler = Mangum(app, lifespan="off")
