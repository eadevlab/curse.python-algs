# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Выбрано задание #6 из урока 3
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
# Третья версия кода
import random
import cProfile


def generate_random_list(length):
    # Попробуем ускорить генерацию списка
    return [int(128 * random.random()) for i in range(length)]


def sum_between_min_max(items):
    # оставим прежним
    min_idx, max_idx = items.index(min(items)), items.index(max(items))
    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx
    # reduce заменим на sum
    return sum(items[min_idx + 1:max_idx])


def main(length):
    return sum_between_min_max(generate_random_list(length))

# print(main(10))

# python -m timeit "import les_4_task_1_3" "les_4_task_1_3.main(10)"
# 100000 loops, best of 5: 2.64 usec per loop

# python -m timeit "import les_4_task_1_3" "les_4_task_1_3.main(1000)"
# 2000 loops, best of 5: 153 usec per loop

# python -m timeit "import les_4_task_1_3" "les_4_task_1_3.main(1000000)"
# 2 loops, best of 5: 160 msec per loop

# cProfile.run('main(10)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:14(sum_between_min_max)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:23(main)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:9(generate_random_list)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

# cProfile.run('main(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 les_4_task_1_3.py:11(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:14(sum_between_min_max)
#         1    0.000    0.000    0.003    0.003 les_4_task_1_3.py:23(main)
#         1    0.000    0.000    0.003    0.003 les_4_task_1_3.py:9(generate_random_list)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#      1000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}

# cProfile.run('main(1000000)')
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.006    3.006 <string>:1(<module>)
#         1    1.573    1.573    2.989    2.989 les_4_task_1_3.py:11(<listcomp>)
#         1    0.000    0.000    0.015    0.015 les_4_task_1_3.py:14(sum_between_min_max)
#         1    0.002    0.002    3.006    3.006 les_4_task_1_3.py:23(main)
#         1    0.000    0.000    2.989    2.989 les_4_task_1_3.py:9(generate_random_list)
#         1    0.000    0.000    3.006    3.006 {built-in method builtins.exec}
#         1    0.008    0.008    0.008    0.008 {built-in method builtins.max}
#         1    0.007    0.007    0.007    0.007 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#   1000000    1.416    0.000    1.416    0.000 {method 'random' of '_random.Random' objects}
