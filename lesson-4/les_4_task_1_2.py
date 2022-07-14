# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Выбрано задание #6 из урока 3
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
# Вторая версия кода
import random
import cProfile
from functools import reduce


def generate_random_list(length):
    return [random.randint(0, 100) for i in range(length)]


def sum_between_min_max(items):
    min_idx, max_idx = items.index(min(items)), items.index(max(items))
    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx
    try:
        return reduce(lambda x, y: x + y, items[min_idx + 1:max_idx])
    except TypeError:
        return 0


def main(length):
    return sum_between_min_max(generate_random_list(length))


# print(main(10))

# python -m timeit "import les_4_task_1_2" "les_4_task_1_2.main(10)"
# 50000 loops, best of 5: 7.65 usec per loop

# python -m timeit "import les_4_task_1_2" "les_4_task_1_2.main(1000)"
# 500 loops, best of 5: 583 usec per loop

# python -m timeit "import les_4_task_1_2" "les_4_task_1_2.main(1000000)"
# 1 loop, best of 5: 603 msec per loop


# cProfile.run('main(10)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:10(generate_random_list)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:15(sum_between_min_max)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:25(main)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method _functools.reduce}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('main(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#         1    0.000    0.000    0.016    0.016 les_4_task_1_2.py:10(generate_random_list)
#         1    0.002    0.002    0.016    0.016 les_4_task_1_2.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_2.py:15(sum_between_min_max)
#       147    0.000    0.000    0.000    0.000 les_4_task_1_2.py:20(<lambda>)
#         1    0.000    0.000    0.017    0.017 les_4_task_1_2.py:25(main)
#      1000    0.003    0.000    0.012    0.000 random.py:200(randrange)
#      1000    0.003    0.000    0.015    0.000 random.py:244(randint)
#      1000    0.005    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method _functools.reduce}
#         1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1285    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('main(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   15.599   15.599 <string>:1(<module>)
#         1    0.000    0.000   15.583   15.583 les_4_task_1_2.py:10(generate_random_list)
#         1    1.552    1.552   15.583   15.583 les_4_task_1_2.py:11(<listcomp>)
#         1    0.000    0.000    0.015    0.015 les_4_task_1_2.py:15(sum_between_min_max)
#        12    0.000    0.000    0.000    0.000 les_4_task_1_2.py:20(<lambda>)
#         1    0.001    0.001   15.599   15.599 les_4_task_1_2.py:25(main)
#   1000000    3.132    0.000   11.092    0.000 random.py:200(randrange)
#   1000000    2.939    0.000   14.031    0.000 random.py:244(randint)
#   1000000    4.753    0.000    7.959    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method _functools.reduce}
#         1    0.000    0.000   15.599   15.599 {built-in method builtins.exec}
#         1    0.008    0.008    0.008    0.008 {built-in method builtins.max}
#         1    0.007    0.007    0.007    0.007 {built-in method builtins.min}
#   1000000    1.412    0.000    1.412    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1268233    1.794    0.000    1.794    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
