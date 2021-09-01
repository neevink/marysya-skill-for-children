from collections import defaultdict
from typing import Union


class NumberMapper:
    """
    По строковому представлению возвращает число
    """
    def __init__(self):
        self._values = defaultdict()

        self._values['1'] = 1
        self._values['один'] = 1
        self._values['первый'] = 1
        self._values['раз'] = 1

        self._values['2'] = 2
        self._values['два'] = 2
        self._values['второй'] = 2

        self._values['3'] = 3
        self._values['три'] = 3
        self._values['третий'] = 3

        self._values['4'] = 4
        self._values['четыре'] = 4
        self._values['четвертый'] = 4
        self._values['четвёртый'] = 4

        self._values['5'] = 5
        self._values['пять'] = 5
        self._values['пятый'] = 5

        self._values['6'] = 6
        self._values['шесть'] = 6
        self._values['шестой'] = 6

        self._values['7'] = 7
        self._values['семь'] = 7
        self._values['седьмой'] = 7

        self._values['8'] = 8
        self._values['восемь'] = 8
        self._values['восьмой'] = 8

        self._values['9'] = 9
        self._values['девять'] = 9
        self._values['девятый'] = 9

        self._values['10'] = 10
        self._values['десять'] = 10
        self._values['десятый'] = 10

    def __getitem__(self, item: str) -> Union[int, None]:
        try:
            return self._values[item]
        except KeyError:
            return None
