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

        self.update_grid_values(snakes_list.body, foods_positions_list, hazards_positions_list)

    def update_grid_values(self, snakes_positions_list: [], foods_positions_list: [],
                           hazards_positions_list: []):

        self.grid_matrix = [[PointsEnum.EMPTY.value for _ in range(self.columns)] for _ in range(self.rows)]

        for i in range(max(len(snakes_positions_list), len(foods_positions_list), len(hazards_positions_list))):
            if 0 < len(foods_positions_list) > i:
                food_pos = foods_positions_list[i]
                self.grid_matrix[food_pos['x']][food_pos['y']] = PointsEnum.FOOD.value

            if 0 < len(hazards_positions_list) > i:
                hazard_pos = hazards_positions_list[i]
                self.grid_matrix[hazard_pos['x']][hazard_pos['y']] = PointsEnum.HAZARD.value

            if 0 < len(snakes_positions_list) > i:
                snake_pos = snakes_positions_list[i]
                self.grid_matrix[snake_pos['x']][snake_pos['y']] = PointsEnum.SNAKE.value
