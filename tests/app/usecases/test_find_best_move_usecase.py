from src.app.adapters.input_adapter_mock import InputAdapterMock
from src.app.entities.grid import GridEntity
from src.app.entities.movements_enum import Movements
from src.app.entities.snake import SnakeEntity
from src.app.usecases.find_best_move_usecase import FindBestMoveUsecase

input_adapter = InputAdapterMock({})
grid = GridEntity(11, 11,
                  snakes_list=[
                      SnakeEntity(100, [{'x': 0, 'y': 0}], {'x': 0, 'y': 0}, 11, 11),
                      SnakeEntity(100, [{'x': 10, 'y': 10}, {'x': 9, 'y': 10}], {'x': 10, 'y': 10}, 11, 11),
                      # SnakeEntity(100, [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}], {'x': 10, 'y': 0}, 11, 11)
                  ],
                  foods_positions_list=[],
                  hazards_positions_list=[])

input_adapter.grid = grid
input_adapter.all_snakes = grid.snakes_list
usecase = FindBestMoveUsecase(input_adapter, 2)


class Test_FindBestMoveUsecase:

    # def test_kappa(self):
    #     score = usecase.minimax(grid.snakes_list[-1], Movements.LEFT)
    #
    #
    #     assert score == 0
    pass
