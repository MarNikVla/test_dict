from collections import defaultdict


# получение словаря из исходного по ключу
def get_dict_by_key(initial_dict, key=None):
    result = {}
    for item in initial_dict.keys():
        if key in initial_dict.keys():
            result = initial_dict[key]
            return result
        elif result != {}:
            return result
        else:
            result = get_dict_by_key(initial_dict[item], key)
    return result


# рекурсивное получение элементов словаря
def create_dict_from_sourse(source, key=None):
    result = {}
    d = defaultdict(dict, {})
    for item1, item2 in source:
        if item1 == key:
            try:
                d[key].update(create_dict_from_sourse(source, item2))
            except KeyError:
                d[key] = (create_dict_from_sourse(source, item2))
    # каждый раз сохраняем результат итераций
    result[key] = d[key]
    return result


def to_tree(source, key=None):
    # Формируем исходный словарь из списка кортежей
    initial_dict = create_dict_from_sourse(source)
    # Получаем словарь из исходного по ключу (в нашем случае key = None)
    result = get_dict_by_key(initial_dict, key)
    return result


if __name__ == '__main__':
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }

    assert to_tree(source) == expected
    print('All tests are done!')
