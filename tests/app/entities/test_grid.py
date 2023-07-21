from src.app.entities.grid import GridEntity
from src.app.entities.pontuation_enum import PointsEnum
from src.app.entities.snake import SnakeEntity


class Test_Grid:
    def test_grid_entity_must_be_initialized_with_zeros(self):
        grid = GridEntity(3, 3, [], [], [])

        assert grid.rows == 3
        assert grid.columns == 3

        for i in range(len(grid.grid_matrix)):
            for j in range(len(grid.grid_matrix[i])):
                assert grid.grid_matrix[i][j] == 0

    def test_grid_0_0_and_1_2_positions_must_be_snake_value(self):
        grid = GridEntity(3, 3,
                          snakes_list=[SnakeEntity(100, [{'x': 0, 'y': 0}, {'x': 1, 'y': 2}],[{'x': 0, 'y': 0}])],
                          foods_positions_list=[],
                          hazards_positions_list=[])

        assert grid.rows == 3
        assert grid.columns == 3
        assert grid.grid_matrix[0][0] == PointsEnum.SNAKE.value
        assert grid.grid_matrix[1][2] == PointsEnum.SNAKE.value

    def test_grid_0_0_and_1_2_positions_must_be_food_value(self):
        grid = GridEntity(3, 3,
                          foods_positions_list=[{"x": 0, "y": 0}, {'x': 1, 'y': 2}],
                          snakes_list=[SnakeEntity(100, [],[])],
                          hazards_positions_list=[])

        assert grid.rows == 3
        assert grid.columns == 3
        assert grid.grid_matrix[0][0] == PointsEnum.FOOD.value
        assert grid.grid_matrix[1][2] == PointsEnum.FOOD.value

    def test_grid_0_0_and_1_2_positions_must_be_hazard_value(self):
        grid = GridEntity(3, 3,
                          hazards_positions_list=[{"x": 0, "y": 0}, {'x': 1, 'y': 2}],
                          snakes_list=[SnakeEntity(100, [],[])],
                          foods_positions_list=[])

        assert grid.rows == 3
        assert grid.columns == 3
        assert grid.grid_matrix[0][0] == PointsEnum.HAZARD.value
        assert grid.grid_matrix[1][2] == PointsEnum.HAZARD.value
