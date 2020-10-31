from collections import defaultdict

def to_tree(source, res = None):
    d = defaultdict(dict, {})
    for i in source:
        item1, item2 = i
        if item1 == res:
            try:
                d[res].update(to_tree(source, item2))
            except KeyError:
                d[res]=(to_tree(source, item2))

    d[res]=d[res]
    print(dict(d)[res])

    return dict(d)


if __name__=='__main__':
    # a= {3:'sdf'}
    # a.update({None:'asdas'})
    # print(a)


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
    to_tree(source)

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }


    # assert to_tree(source) == expected
