def is_increasing(a):
    """
    Вернуть True, если элементы массива строго возрастают, и False иначе
    is_increasing([1, 2, 6, 10]) -> True
    """
    for _ in ...:
        if ...:
            return False
    return True


def twice_as_much(a):
    """
    Вернуть массив, каждый элемент которого в два раза больше соответствующего элемента из a
    twice_as_much([1, 'ab']) -> [2, 'abab']
    """
    return [... for _ in ...]


def count_oddity(a):
    """
    Вернуть пару из двух элементов - количество четных и количество нечетных элементов a
    count_oddity([1, 2, 3, 5]) -> (1, 3)
    """
    even, odd = 0, 0
    ...
    return even, odd


def pick_until(a, stop):
    """
    Вернуть начало массива a, взятое до момента, когда в a встречается stop
    pick_until([1, 2, 7, 1, 4, 3], 4) -> [1, 2, 7, 1]
    """
    b = []
    for x in a:
        if x == stop:
            ...
        ...
    return b


def sum_until(a, stop):
    """
    Вернуть максимальную сумму первых элементов массива a, не превосходящую stop
    sum_until([1, 2, 7, 1, 4, 3], 13) -> 11 = (1+2+7+1)
    """
    s, i = 0, 0
    while ...:
        s += ...
        ...
    return s
