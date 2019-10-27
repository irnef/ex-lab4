# Реализация задания 1
    @ -0,0 +1,69 @@
from __future__ import print_function

from librip.gens import field
from librip.gens import gen_random


# Тест генератора gen_random
def test_gen_random():
    print('TEST GENERATOR gen_random()', end='\n')

    print('Rand begin:', end=' ')
    begin = int(input())

    print('Rand end:', end=' ')
    end = int(input())

    print('Rand num count:', end=' ')
    num_count = int(input())

    print('Results:', end=' ')
    for i in gen_random(begin, end, num_count):
        print(i, end=' '),


# Тест генератора field
def test_field_with_goods():
    print('TEST GENERATOR field()', end='\n')

    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
        {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
    ]

    print('Available keys:', end=' ')
    for key in goods[0].keys():
        print(key, end=' ')

    print('(enter some of these arguments or none)', end='\n')

    arguments = str(input())
    arguments = arguments.split(' ')

    for a in arguments:
        if a not in goods[0].keys():
            print('No such key(-s)')
            return

    if len(arguments) == 0:
        for g in field(goods):
            print (g, end=' ')
    elif len(arguments) == 1:
        for g in field(goods, arguments[0]):
            print (g, end=' ')
    elif len(arguments) == 2:
        for g in field(goods, arguments[0], arguments[1]):
            print (g, end=' ')
    else:
        for g in field(goods, arguments[0], arguments[1], arguments[2]):
            print (g, end=' ')


if __name__ == "__main__":
    test_gen_random()

    print('\n')

    test_field_with_goods()
