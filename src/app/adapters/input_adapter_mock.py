from .input_adapter_interface import IInputAdapter
from ..entities.grid import GridEntity
from ..entities.snake import SnakeEntity


class InputAdapterMock(IInputAdapter):
    def __init__(self, request: dict):
        self.all_snakes = [
            SnakeEntity(100, [{'x': 0, 'y': 0}, {'x': 1, 'y': 2}], {'x': 0, 'y': 0}, 11, 11),
            SnakeEntity(100, [{'x': 3, 'y': 3}, {'x': 3, 'y': 2}], {'x': 3, 'y': 3}, 11, 11),
            SnakeEntity(100, [{'x': 1, 'y': 1}, {'x': 1, 'y': 1}], {'x': 1, 'y': 1}, 11, 11)
        ]
        self.grid = GridEntity(11, 11, self.all_snakes, [], [])
        self.my_snake = self.all_snakes[0]
