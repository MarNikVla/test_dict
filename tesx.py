def to_tree(source, res = None):
    d = {}
    for i in source:
        item1, item2 = i
        if item1 == res:
            print('df')


    return d

if __name__=='__main__':
    # a= {3:'sdf'}
    # a.update({None:'asdas'})
    # print(a)


    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        # ('a', 'a2'),
        # ('a2', 'a21'),
        # ('a2', 'a22'),
        # ('b', 'b1'),
        # ('b1', 'b11'),
        # ('b11', 'b111'),
        # ('b', 'b2'),
        # ('c', 'c1'),
    ]
    to_tree(source)

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
