def median(a, b, c):
    """
    Вернуть медиану из трех элементов
    median(2, 5, 3) -> 3
    """
    if ...:
        return a
    elif ...:
        return b
    else:
        return c


def get_or_none(a, index):
    """
    Вернуть a[index], если он существует, иначе None
    get_or_none([1, 2, 3], 2) -> 2
    get_or_none([1, 2], 2)    -> None
    """
    if ... <= ... < ...:
        return a[index]
    return None


def is_power_of_two(x):
    """
    Вернуть, является ли x степенью двойки
    is_power_of_two(8) -> True
    is_power_of_two(0) -> False
    """
    s = bin(x)
    return ... and ...


def is_monotonic(a, b, c):
    """
    Проверить, является ли [a, b, c] строго монотонной последовательностью
    is_monotonic(1, 2, 3) -> True
    is_monotonic(9, 5, 4) -> True
    is_monotonic(6, 7, 6) -> False
    """
    return ... > ... > ... or ...


def inline_if(a, b, condition):
    """
    Вернуть a, если condition == True, и b иначе.
    inline_if(1, 2, False) -> 2
    """
    return ...
