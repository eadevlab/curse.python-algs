# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import operator
import random


def generate_random_list(length):
    return [round(50 * random.random(), 2) for i in range(length)]


def merge_sort(li, compare=operator.lt):
    def _merge(li1, li2):
        ret, i, j = [], 0, 0
        while i < len(li1) and j < len(li2):
            if compare(li1[i], li2[j]):
                ret.append(li1[i])
                i += 1
            else:
                ret.append(li2[j])
                j += 1
        if i < len(li1):
            ret.extend(li1[i:])
        if j < len(li2):
            ret.extend(li2[j:])
        return ret
    if len(li) == 1:
        return li
    elif len(li) == 2:
        return li if compare(li[0], li[1]) else li[::-1]

    half_size = len(li) // 2
    return _merge(merge_sort(li[:half_size], compare), merge_sort(li[half_size:], compare))


if __name__ == '__main__':
    LENGTH = 10
    gen_list = generate_random_list(LENGTH)
    print('Исходный список: ', gen_list)
    print('Отсортированный список: ', merge_sort(gen_list))
