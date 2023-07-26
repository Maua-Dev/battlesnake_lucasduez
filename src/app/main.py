from fastapi import FastAPI
from mangum import Mangum

from src.app.adapters.input_adapter_battle_snake import InputAdapterBattleSnake
from src.app.usecases.find_best_move_usecase import FindBestMoveUsecase
# from .adapters.input_adapter_battle_snake import InputAdapterBattleSnake
# from .usecases.find_best_move_usecase import FindBestMoveUsecase
from ..app.adapters.input_adapter_interface import IInputAdapter

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
    input_adapter = InputAdapterBattleSnake(request)
    find_move_usecase = FindBestMoveUsecase(input_adapter, 9)
    next_move = find_move_usecase.calculate_best_move()

    return {
        "move": next_move.value,
        "shout": "only right"
        }


handler = Mangum(app, lifespan="off")
