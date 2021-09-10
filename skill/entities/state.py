from enum import Enum


class State(Enum):
    START = 1
    SELECT_FIGURE = 2
    PREPARING = 3  # Типо отступи n клеток и поставь точку
    DRAWING = 4
    FINISH = 5  # Рисунок нарисован
