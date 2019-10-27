@@ -0,0 +1,35 @@
from __future__ import print_function

from librip.gens import gen_random
from librip.iterators import Unique


def test_unique_iterator():
    print('TEST WITH LIST OF INTS')
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(data1)
    for i in Unique(data1, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH GENERATOR OF INTS\ngen_random(1, 3, 10)')
    data2 = gen_random(1, 3, 10)
    for i in Unique(data2, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH LIST OF STR (ignore_case=False)')
    data3 = ['a', 'A', 'b', 'B']
    print(data3)
    for i in Unique(data3, ignore_case=False):
        print(i, end=' ')
    print('\n')

    print('TEST WITH LIST OF STR (ignore_case=True)')
    print(data3)
    for i in Unique(data3, ignore_case=True):
        print(i, end=' ')


if __name__ == "__main__":
    test_unique_iterator()
