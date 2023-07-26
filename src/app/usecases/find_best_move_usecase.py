
from ..adapters.input_adapter_interface import IInputAdapter
from ..entities.movements_enum import Movements
from ..entities.pontuation_enum import PointsEnum
from ..entities.snake import SnakeEntity


class FindBestMoveUsecase:
    input_adapter: IInputAdapter
    maximum_turns_prediction: int

    def __init__(self, input_adapter: IInputAdapter, max_turns_prediction: int):
        self.grid = input_adapter.grid
        self.my_snake = input_adapter.my_snake
        self.maximum_turns_prediction = max_turns_prediction
        self.all_snakes_list: [SnakeEntity] = input_adapter.all_snakes

    def calculate_best_move(self) -> Movements:
        scores = {
            Movements.UP: self.minimax(self.my_snake, Movements.UP),
            Movements.DOWN: self.minimax(self.my_snake, Movements.DOWN),
            Movements.RIGHT: self.minimax(self.my_snake, Movements.RIGHT),
            Movements.LEFT: self.minimax(self.my_snake, Movements.LEFT)
        }

        return max(scores, key=scores.get)

    def minimax(self,snake: SnakeEntity, direction: Movements, turn: int = 1):
        snake.move_snake(direction)

        head_position = snake.head_pos
        pos_value = self.grid.grid_matrix[head_position["x"]][head_position['y']]

        if pos_value == PointsEnum.SNAKE.value:
            return pos_value

        if turn > self.maximum_turns_prediction:
            return pos_value

        self.grid.update_grid_values(self.all_snakes_list, self.grid.foods_positions_list, []) #Todo: estou ignorando a lista de comidas e de hazard
        is_maximizing = turn % len(self.all_snakes_list) == 0
        current_snake: SnakeEntity = self.all_snakes_list[(turn-1) % len(self.all_snakes_list)]

        if not is_maximizing:
            score_up = self.minimax(current_snake, Movements.UP, turn+1)
            score_down = self.minimax(current_snake, Movements.DOWN, turn+1)
            score_right = self.minimax(current_snake, Movements.RIGHT, turn+1)
            score_left = self.minimax(current_snake, Movements.LEFT, turn+1)

            return min(score_up, score_down, score_right, score_left)

        if is_maximizing:
            score_up = self.minimax(current_snake, Movements.UP, turn+1)
            score_down = self.minimax(current_snake, Movements.DOWN, turn+1)
            score_right = self.minimax(current_snake, Movements.RIGHT, turn+1)
            score_left = self.minimax(current_snake, Movements.LEFT, turn+1)

            return max(score_up, score_down, score_right, score_left)
