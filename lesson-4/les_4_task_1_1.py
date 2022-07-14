# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Выбрано задание #6 из урока 3
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
# Первая версия кода
import random
import cProfile


def generate_random_list(length):
    return [random.randint(0, 100) for i in range(length)]


def sum_between_min_max(items):
    def _get_min_max_index(items):
        max_idx = 0
        min_idx = 0
        for idx, item in enumerate(items):
            if item < items[min_idx]:
                min_idx = idx
            if item > items[max_idx]:
                max_idx = idx
        # print('Min index: ', min_idx)
        # print('Max index: ', max_idx)
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx
        return min_idx, max_idx

    min_idx, max_idx = _get_min_max_index(items)
    result = 0
    for idx, item in enumerate(items):
        if min_idx < idx < max_idx:
            result += item
    # print('Result: ', result)
    return result


def main(length):
    return sum_between_min_max(generate_random_list(length))

# main(100000)

# python -m timeit "import les_4_task_1_1" "les_4_task_1_1.main(10)"
# 50000 loops, best of 5: 8.67 usec per loop

# python -m timeit "import les_4_task_1_1" "les_4_task_1_1.main(1000)"
# 500 loops, best of 5: 693 usec per loop

# python -m timeit "import les_4_task_1_1" "les_4_task_1_1.main(1000000)"
# 1 loop, best of 5: 6.95 sec per loop


# cProfile.run('main(10)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:14(sum_between_min_max)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:15(_get_min_max_index)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:38(main)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:9(generate_random_list)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('main(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.001    0.001    0.015    0.015 les_4_task_1_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:14(sum_between_min_max)
#         1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:15(_get_min_max_index)
#         1    0.000    0.000    0.015    0.015 les_4_task_1_1.py:38(main)
#         1    0.000    0.000    0.015    0.015 les_4_task_1_1.py:9(generate_random_list)
#      1000    0.003    0.000    0.011    0.000 random.py:200(randrange)
#      1000    0.003    0.000    0.013    0.000 random.py:244(randint)
#      1000    0.005    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#      1000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1280    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('main(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   15.502   15.502 <string>:1(<module>)
#         1    1.524    1.524   15.373   15.373 les_4_task_1_1.py:10(<listcomp>)
#         1    0.060    0.060    0.127    0.127 les_4_task_1_1.py:14(sum_between_min_max)
#         1    0.067    0.067    0.067    0.067 les_4_task_1_1.py:15(_get_min_max_index)
#         1    0.001    0.001   15.502   15.502 les_4_task_1_1.py:38(main)
#         1    0.000    0.000   15.373   15.373 les_4_task_1_1.py:9(generate_random_list)
#   1000000    3.092    0.000   10.944    0.000 random.py:200(randrange)
#   1000000    2.905    0.000   13.849    0.000 random.py:244(randint)
#   1000000    4.689    0.000    7.852    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000   15.502   15.502 {built-in method builtins.exec}
#   1000000    1.393    0.000    1.393    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1266350    1.770    0.000    1.770    0.000 {method 'getrandbits' of '_random.Random' objects}
