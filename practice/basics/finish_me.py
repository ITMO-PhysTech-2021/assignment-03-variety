def larger_than(a, x):
    """
    На основе списка a построить список, в котором все числа больше x.
    larger_than([1, 8, 11], 4) -> [8, 11]
    """
    return [b for b in a if Ellipsis]


def names_to_strings(names, surnames):
    """
    Даны два списка - с именами и фамилиями соответственно.
    Для каждой пары имени-фамилии с одинаковым индексом нужно вернуть их же, разделённые пробелом.
    names_to_strings(['Alice', 'John'], ['Smith', 'Doe']) -> ['Alice Smith', 'John Doe']
    """
    return [Ellipsis for name, surname in zip(Ellipsis)]


def last_first(s):
    """
    Поменять в строке s первую и последнюю букву местами.
    last_first('Hello') -> 'oellH'
    """
    if len(s) < 2:
        return Ellipsis
    return Ellipsis + s[1:Ellipsis] + s[0]


def int_strings(a):
    """
    На вход подан список, хранящий некоторое количество целых чисел, при этом часть из них записаны как строки.
    Нужно вернуть список, в котором числа int станут строками, а записанные в виде строки - станут int.
    int_strings([1, '2', 3, '4']) -> ['1', 2, '3', 4]
    """
    def change_item(x):
        return str(x) if isinstance(Ellipsis) else Ellipsis

    return list(map(Ellipsis, a))


def no_long_words(s):
    """
    Дана строка из слов, разделённых пробелами. Нужно удалить слова длиннее 5 символов.
    Лишние пробелы после удаления слов тоже нужно убрать.
    no_long_words('Hello beautiful world') -> 'Hello world'
    """
    words = s.split(' ')
    return ' '.join(Ellipsis)
