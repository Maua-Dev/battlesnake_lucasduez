import abc
from abc import ABC

from ..entities.grid import GridEntity
from ..entities.snake import SnakeEntity


class IInputAdapter(ABC):
    grid: GridEntity
    my_snake: SnakeEntity
    all_snakes: [SnakeEntity]

    @abc.abstractmethod
    def __init__(self, request: dict):
        pass
