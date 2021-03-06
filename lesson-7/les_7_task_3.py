# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).
import random


def generate_random_list(length):
    return [random.randint(-50, 50) for i in range(length)]


# Метод нахождения медианы
def find_median(li):
    li_len = len(li)
    # Без сортировки придётся проверить каждый элемент списка и найти количество элементов не больше и не меньше его
    for i in range(li_len):
        gt_cnt = len([e for e in li if li[i] > e])  # количество элементов больше проверяемого
        lt_cnt = len([e for e in li if li[i] < e])  # количество элементов меньше проверяемого
        eq_cnt = len([e for e in li if li[i] == e])  # эквивалентные значения
        if gt_cnt == lt_cnt or abs(gt_cnt - lt_cnt) - eq_cnt == 0:
            return li[i]
    return 0


if __name__ == '__main__':
    m = 5
    LENGTH = 2 * m + 1
    gen_list = generate_random_list(LENGTH)
    print('Исходный список: ', gen_list)
    print('Медиана: ', find_median(gen_list))
