# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

from hashlib import md5


def substrings_cnt(string):
    hashs = []
    str_length = len(string)
    str_hash = md5(string.encode('utf-8')).hexdigest()
    all_cnt = 0
    for i in range(str_length - 1):
        for j in range(i + 1, str_length):
            sub = string[i:j]
            sub_hash = md5(sub.encode('utf-8')).hexdigest()
            all_cnt += 1
            if sub_hash != str_hash and sub != '' and sub_hash not in hashs:
                hashs.append(sub_hash)
    return len(hashs), all_cnt


string = input('Введите строку: ')
# string = 'Qwerrty'

if len(string) == 0:
    print('Вы ничего не ввели')
else:
    uniq_cnt, all_cnt = substrings_cnt(string)
    print('Количество различных подстрок: ', uniq_cnt)
    print('Количество всех подстрок: ', all_cnt)
