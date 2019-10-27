@@ -0,0 +1,43 @@
#!/usr/bin/env python3
import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import gen_random
from librip.iterators import Unique as unique

path = None

# путь до файла, который был передан при запуске
path = 'data_light.json'
with open(path) as f:
    data = json.load(f)


# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list([x for x in unique([i['job-name'] for i in arg], ignore_case=True)])


@print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    sal_list = list(gen_random(100000, 200000, len(arg)))
    work_list = iter(map(lambda x: x + ", зарплата", arg))
    return ["{} {} {}".format(work, sal, 'руб.') for (work, sal) in zip(work_list, sal_list)]


with timer():
    f4(f3(f2(f1(data))))
