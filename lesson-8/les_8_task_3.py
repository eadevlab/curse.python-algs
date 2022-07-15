# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from helper import int_input


def gen_graph(n):
    ret = {}
    for i in range(n):
        ret[i] = tuple(j for j in range(n) if i != j)
    return ret


def dfs(graph, start, visited=None):
    if not visited:
        visited = []
    if start not in visited:
        visited.append(start)
        for _ in graph[start]:
            dfs(graph, _, visited)
    return visited


n = int_input('Введите количество вершин в графе: ')
start = int_input('От какой вершины идти: ')
if n < start:
    print('Ошибка! Такой вершины не существует')
else:
    graph = gen_graph(n)
    print(graph)
    print(dfs(graph, start))
