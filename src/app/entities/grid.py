import dataclasses

from .pontuation_enum import PointsEnum
from .snake import SnakeEntity


@dataclasses.dataclass(init=False)
class GridEntity:
    rows: int
    columns: int
    grid_matrix: [[]]

    def __init__(self, rows: int, columns: int, snakes_list: [SnakeEntity], foods_positions_list: [],
                 hazards_positions_list: []):

        self.rows = rows
        self.columns = columns

        self.update_grid_values(snakes_list, foods_positions_list, hazards_positions_list)

    def update_grid_values(self, snakes_list: [SnakeEntity], foods_positions_list: [],
                           hazards_positions_list: []):

        self.grid_matrix = [[PointsEnum.EMPTY.value for _ in range(self.columns)] for _ in range(self.rows)]

        snakes_positions = []

        for snake in snakes_list:
            snakes_positions += snake.body

        for i in range(max(len(snakes_positions), len(foods_positions_list), len(hazards_positions_list))):
            if 0 < len(foods_positions_list) > i:
                food_pos = foods_positions_list[i]
                self.grid_matrix[food_pos['x']][food_pos['y']] = PointsEnum.FOOD.value

            if 0 < len(hazards_positions_list) > i:
                hazard_pos = hazards_positions_list[i]
                self.grid_matrix[hazard_pos['x']][hazard_pos['y']] = PointsEnum.HAZARD.value

            if 0 < len(snakes_positions) > i:
                snake_pos = snakes_positions[i]
                self.grid_matrix[snake_pos['x']][snake_pos['y']] = PointsEnum.SNAKE.value
