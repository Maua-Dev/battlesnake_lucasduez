import dataclasses

from ..entities.movements_enum import Movements


@dataclasses.dataclass
class SnakeEntity:
    health: int
    body: []
    head_pos: dict
    grid_rows_number: int
    grid_columns_number: int

    def move_snake(self, direction: Movements):

        if self.health <= 0 or not self.is_movement_valid(direction):
            return None

        for i in range(1, len(self.body)):
            self.body[-i] = self.body[-i - 1]

        self.body[0] = self.get_new_head_pos(direction)
        self.health -= 1

    def get_new_head_pos(self, direction: Movements):
        current_pos = self.head_pos
        new_pos = {}

        if direction == Movements.UP:
            new_pos = {"x": current_pos['x'], "y": current_pos['y'] + 1}

        elif direction == Movements.DOWN:
            new_pos = {"x": current_pos['x'], "y": current_pos['y'] - 1}

        elif direction == Movements.RIGHT:
            new_pos = {"x": current_pos['x'] + 1, "y": current_pos['y']}

        elif direction == Movements.LEFT:
            new_pos = {"x": current_pos['x'] - 1, "y": current_pos['y']}

        return new_pos

    def is_movement_valid(self, direction: Movements):
        current_pos = self.head_pos

        if current_pos['x'] == 0 and direction == Movements.LEFT:
            return False

        if current_pos['x'] == self.grid_columns_number - 1 and direction == Movements.RIGHT:
            return False

        if current_pos['y'] == 0 and direction == Movements.DOWN:
            return False

        if current_pos['y'] == self.grid_rows_number - 1 and direction == Movements.UP:
            return False

        return True

