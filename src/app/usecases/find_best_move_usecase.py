from ..adapters.input_adapter_interface import IInputAdapter
from ..entities.movements_enum import Movements


class FindBestMoveUsecase:
    input_adapter: IInputAdapter

    def __init__(self, input_adapter: IInputAdapter):
        self.grid = input_adapter.grid
        self.my_snake = input_adapter.my_snake

    def calculate_best_move(self) -> Movements:
        scores_dict = {
            Movements.UP: self.minimax(Movements.UP),
            Movements.DOWN: self.minimax(Movements.DOWN),
            Movements.RIGHT: self.minimax(Movements.RIGHT),
            Movements.LEFT: self.minimax(Movements.LEFT)
        }

        return max(scores_dict, scores_dict.get)

    # def minimax(self, movement: Movements, turn: int = 1):
    #     return 10
