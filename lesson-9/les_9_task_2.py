# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, deque


class Node:
    def __init__(self, letter, freq, childs=[]):
        self.letter = letter
        self.freq = freq
        self.childs = childs

    @property
    def cord(self):
        return self.freq, ord(self.letter) if self.letter else 0

    def __str__(self):
        return f'{self.letter}={self.freq}'

    def __lt__(self, other):
        return self.cord < other.cord

    def __eq__(self, other):
        return self.cord == other.cord

    def __gr__(self, other):
        return self.cord > other.cord


def get_table(node, code=''):
    table = {}
    if node.letter is not None:
        table = {node.letter: code}
    else:
        # т.к. дерево бинарное есть всего 2 наследника с индексами 0 и 1 можно сделать так
        for i, c in enumerate(node.childs):
            table.update(get_table(c, code + str(i)))
    return table


def haffman(string):
    nodes = deque([Node(l, f) for l, f in Counter(string).items()])
    while len(nodes) > 1:
        nodes = deque(sorted(nodes))  # сортировака по частоте и букве
        childs = [nodes.popleft() for _ in range(2)]
        freq = sum([_.freq for _ in childs])
        nodes.append(Node(None, freq, childs))
    table = get_table(nodes[0])
    return ''.join([table[_] for _ in string])


if __name__ == '__main__':
    # string = 'helloworld'
    string = input('Введите строку: ')
    if len(string) == 0:
        print('Вы ничего не ввели')
    else:
        enc = haffman(string)
        print('Исходная строка: ', string)
        print('Закодированная строка: ', enc)
