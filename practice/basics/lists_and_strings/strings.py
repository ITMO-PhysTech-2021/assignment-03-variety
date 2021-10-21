def reverse(s):
    """Вернуть исходную строку, записанную наоборот ('abc' -> 'bca')"""
    pass


def swap_case(s):
    """
    Вернуть исходную строку, но нижний регистр заменён на верхний, а верхний на нижний.
    Не использовать стандартную функцию str.swapcase()
    ('Hello world' -> 'hELLO WORLD')
    """
    pass


def censor_words(s, blacklist):
    """
    Вернуть исходную строку, но подстроки из списка blacklist заменить на звёздочки (*) такой же длины.
    censor_words('hello world', ['hello']) -> '***** world')
    """
    pass


def remove_duplicates(s):
    """
    Нужно удалить идущие подряд повторы слов в строке. Строка состоит только из букв нижнего регистра и пробелов.
    'hello nice nice world hello' -> 'hello nice world hello'
    """
    pass


def parentheses(s):
    """
    Проверить, закрыты ли все пары круглых скобок в строке.
    '(abc(1+2))' -> True
    '(lalala' -> False -- скобка не закрыта
    '(hello)world)' -> False -- слишком много закрывающих скобок
    """
    pass
