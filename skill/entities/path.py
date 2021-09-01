from enum import Enum, EnumMeta
from typing import List


class DirectionMeta(EnumMeta):
    def __getitem__(self, item):
        if item == 'UP':
            return Direction.UP
        elif item == 'RIGHT':
            return Direction.RIGHT
        elif item == 'DOWN':
            return Direction.DOWN
        elif item == 'LEFT':
            return Direction.LEFT


class Direction(Enum, metaclass=DirectionMeta):
    UP = 'вверх'
    RIGHT = 'вправо'
    DOWN = 'вниз'
    LEFT = 'влево'


class Step:
    """
    Один шаг пути, по которому рисуется фигура
    """
    def __init__(self, direction: Direction, count: int):
        self.direction = direction
        self.count = count


class Path:
    """
    Путь, который показывает, как рисуется фигура
    """
    def __init__(self, path: List[Step]):
        self.path = path
