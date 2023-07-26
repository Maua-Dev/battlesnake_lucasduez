from .input_adapter_interface import IInputAdapter
from ..entities.grid import GridEntity
from ..entities.snake import SnakeEntity


class InputAdapterBattleSnake(IInputAdapter):
    grid: GridEntity
    my_snake: SnakeEntity
    all_snakes: [SnakeEntity]

    def __init__(self, request: dict):
        board_viewmodel = request["board"]
        all_snakes_viewmodels = request['snakes']

        for i in range(len(all_snakes_viewmodels)):
            current_viewmodel = all_snakes_viewmodels[i]
            self.all_snakes[i] = SnakeEntity(
                health=current_viewmodel['health'],
                body=current_viewmodel['body'],
                head_pos=current_viewmodel['body'][0],
                grid_rows_number=board_viewmodel['width'],
                grid_columns_number=board_viewmodel['height'],
            )

        self.my_snake = self.all_snakes[0]

        self.grid = GridEntity(
            rows=board_viewmodel['width'],
            columns=board_viewmodel['height'],
            foods_positions_list=board_viewmodel['food'],
            hazards_positions_list=board_viewmodel['hazards'],
            snakes_list=self.all_snakes
        )
