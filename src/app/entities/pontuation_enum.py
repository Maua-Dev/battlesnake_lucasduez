from enum import Enum


class PointsEnum(Enum):
    FOOD = 2
    SNAKE = -2
    HAZARD = -1
    EMPTY = 0

    def get_highest_score(self):
        return max(self.SNAKE.value, self.EMPTY.value, self.HAZARD.value, self.FOOD.value)

    def get_lowest_score(self):
        return min(self.SNAKE.value, self.EMPTY.value, self.HAZARD.value, self.FOOD.value)
