import random

items = [random.randint(0, 100) for i in range(10)]
print('List: ', items)
min_item = items[0]
min_index = 0
max_item = items[0]
max_index = 0

for i, item in enumerate(items):
    if item < min_item:
        min_item = item
        min_index = i
    if item > max_item:
        max_item = item
        max_index = i

items[min_index], items[max_index] = items[max_index], items[min_index]
print('Result ', items)
print('Min: ', min_item)
print('Max: ', max_item)
