from src.app.entities.movements_enum import Movements
from src.app.entities.snake import SnakeEntity


class Test_SnakeEntity:
    def test_snake_should_move_right(self):
        body = [
            {'x': 5, 'y': 5},
            {'x': 4, 'y': 5},
            {'x': 4, 'y': 4},
            {'x': 4, 'y': 3},
        ]

        snake = SnakeEntity(100, body, body[0], 11, 11)

        snake.move_snake(Movements.RIGHT)

        assert snake.body[0] == {'x': 6, 'y': 5}
        assert snake.body[1] == {'x': 5, 'y': 5}
        assert snake.body[2] == {'x': 4, 'y': 5}
        assert snake.body[3] == {'x': 4, 'y': 4}
        assert snake.health == 99

    def test_snake_should_not_move_through_the_edge(self):
        body = [
            {'x': 0, 'y': 5},
            {'x': 1, 'y': 5},
        ]

        snake = SnakeEntity(100, body, body[0], 11, 11)

        snake.move_snake(Movements.LEFT)

        assert snake.head_pos == {'x': 0, 'y': 5}
        assert snake.body[1] == {'x': 1, 'y': 5}

    def test_is_movement_valid_should_return_true(self):
        body = [
            {'x': 0, 'y': 5},
            {'x': 1, 'y': 5},
        ]

        snake = SnakeEntity(100, body, body[0], 11, 11)

        assert snake.is_movement_valid(Movements.RIGHT) is True

    def test_is_movement_valid_should_return_false(self):
        body = [
            {'x': 0, 'y': 5},
            {'x': 1, 'y': 5},
        ]

        snake = SnakeEntity(100, body, body[0], 11, 11)

        assert snake.is_movement_valid(Movements.LEFT) is False
