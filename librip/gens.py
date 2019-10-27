@@ -0,0 +1,23 @@
import random


# Генератор вычленения полей из массива словарей
def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            yield (item.get(args[0]))
    else:
        for item in items:
            yield {arg: item.get(arg) for arg in args}


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    assert num_count != 0

    if begin > end:
        begin, end = end, begin

    return (random.randint(begin, end) for _ in range(num_count))
