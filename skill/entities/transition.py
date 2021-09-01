from typing import List
from state import State

class Transition:
    """
    Переход из одного состояния в другое
    """

    def __init__(self, transition_to_state: State, triggers_list: List[str]):
        # transition_to_state - TODO мб заменить на число?
        # triggers_list - список фраз, которые спровоцируют переход в это состояние
        self.transition_to_state = transition_to_state
        self.triggers_list = triggers_list


