# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,‘E’].

from collections import deque
from functools import reduce

AVAILABLE_CHARS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


class HexNumber:
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError
        self.value = deque(value)

    @staticmethod
    def validate(value):
        is_valid = True
        for v in value:
            if v not in AVAILABLE_CHARS:
                is_valid = False
                break
        return is_valid

    def __str__(self):
        return ''.join(self.value)

    @staticmethod
    def to_hex(v):
        if v < 16:
            return AVAILABLE_CHARS[v], 0
        return AVAILABLE_CHARS[v % 16], v // 16

    @staticmethod
    def sum(x, y, k=0):
        return HexNumber.to_hex(x + y + k)

    def __add__(self, other):
        x, y = self.value.copy(), other.value.copy()
        max_iterations = max(len(x), len(y))
        k = 0
        result = deque()
        while max_iterations > 0:
            ret, k = self.sum(AVAILABLE_CHARS.index(x.pop()) if len(x) else 0,
                              AVAILABLE_CHARS.index(y.pop()) if len(y) else 0,
                              k)
            result.appendleft(ret)
            max_iterations -= 1

        return HexNumber(result)

    def __mul__(self, other):
        x, y = self.value.copy(), other.value
        results = []
        for i in range(len(y)):
            mul = AVAILABLE_CHARS.index(y.pop())
            tmp = deque()
            for j in x:
                tmp.appendleft(mul * AVAILABLE_CHARS.index(j))
            for ii in range(i):  # необходимо добавить пустые значения как при умножении в столбик
                tmp.appendleft(0)
            results.append(tmp)

        for idx, r in enumerate(results):
            k = 0
            for i in range(len(r)):
                r[i], k = self.to_hex(r[i] + k)
            if k:
                r.append(str(k))
            r.reverse()
            results[idx] = HexNumber(r)
        return reduce(lambda i, j: i + j, results)


def main():
    while True:
        try:
            a = HexNumber(list(input('Input first hex: ').upper()))
            break
        except ValueError:
            print('Input error')
    while True:
        try:
            b = HexNumber(list(input('Input second hex: ').upper()))
            break
        except ValueError:
            print('Input error')
    # a = HexNumber('A2')
    # b = HexNumber('C4F')

    print('Sum: ', a + b)
    print('Multiple: ', a * b)


if __name__ == '__main__':
    main()
