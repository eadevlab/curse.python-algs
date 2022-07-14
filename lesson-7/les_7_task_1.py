# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import operator
import random


def generate_random_list(length):
    return [random.randint(-100, 99) for i in range(length)]


# Сортировка пузырьком
def bubble_sort(li):
    list_length = len(li)
    for i in range(list_length - 1):
        swapped = False
        for j in range(i + 1, list_length):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
                swapped = True
        if not swapped:
            break
    return li


if __name__ == '__main__':
    LENGTH = 10
    gen_list = generate_random_list(LENGTH)
    print('Исходный список: ', gen_list)
    print('Отсортированный список: ', bubble_sort(gen_list))
