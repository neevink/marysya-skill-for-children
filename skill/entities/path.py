from enum import Enum, EnumMeta


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
