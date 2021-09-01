
def cells_count(count: int) -> str:
    """
    Красивое строковое представление количества клеток
    """
    if count == 1:
        return 'одну клетку'
    elif count == 2:
        return 'две клетки'
    elif count == 3:
        return 'три клетки'
    elif count == 4:
        return 'четыре клетки'
    elif count == 5:
        return 'пять клеток'
    elif count == 6:
        return 'шесть клеток'
    elif count == 7:
        return 'семь клеток'
    elif count == 8:
        return 'восемь клеток'
    elif count == 9:
        return 'девять клеток'
    elif count == 10:
        return 'десять клеток'
    elif count == 11:
        return 'одиннадцать клеток'
    elif count == 12:
        return 'двенадцать клеток'
    elif count == 13:
        return 'тринадцать клеток'
    elif count == 14:
        return 'четырнадцать клеток'
    elif count == 15:
        return 'пятнадцать клеток'
    else:
        return str(count) + ' клеток'
