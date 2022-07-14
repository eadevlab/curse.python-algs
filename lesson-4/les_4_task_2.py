# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# Классический
import cProfile


def prime(n):
    pass


# Решето Эратосфена
def sieve(n):
    sieve = {}
    i = 2
    current_index = 0
    founded = i
    max_val = n * 2
    while current_index <= (n - 1):
        # Четные числа кроме 2 можно пропускать т.к. они являются состовными
        if i != 2 and i % 2 == 0:
            i += 1
            continue
        if i not in sieve:
            sieve[i] = i
        j = i * 2
        while j < max_val:
            sieve[j] = 0
            j += i
        sieve[j] = 0
        if sieve[i] != 0:
            current_index += 1
            founded = i
        i += 1
    return founded


def sieve_example(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]


def prime(n):
    max_n = n * n
    prime = [2]
    for i in range(3, max_n + 1, 2):
        if (i > 10 and i % 10 == 5) or i in prime:
            continue
        for j in prime:
            if j * j - 1 > i:
                prime.append(i)
                break
            if i % j == 0:
                break
        else:
            prime.append(i)
        if len(prime) == n:
            break
    return prime[n - 1]

# Тестирование Решета эрастофена
# python -m timeit "import les_4_task_2" "les_4_task_2.sieve(10)"
# 50000 loops, best of 5: 7.24 usec per loop

# python -m timeit "import les_4_task_2" "les_4_task_2.sieve(100)"
# 2000 loops, best of 5: 106 usec per loop

# python -m timeit "import les_4_task_2" "les_4_task_2.sieve(1000)"
# 200 loops, best of 5: 1.53 msec per loop

# cProfile.run('sieve(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:14(sieve)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Тестирование метода без решета
# print(prime(7))
# python -m timeit "import les_4_task_2" "les_4_task_2.prime(10)"
# 50000 loops, best of 5: 6.12 usec per loop

# python -m timeit "import les_4_task_2" "les_4_task_2.prime(100)"
# 1000 loops, best of 5: 215 usec per loop

# python -m timeit "import les_4_task_2" "les_4_task_2.prime(1000)"
# 20 loops, best of 5: 14.9 msec per loop

# cProfile.run('prime(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.044    0.044 <string>:1(<module>)
#         1    0.037    0.037    0.044    0.044 les_4_task_2.py:51(prime)
#         1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
#      3168    0.005    0.000    0.005    0.000 {built-in method builtins.len}
#       999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
