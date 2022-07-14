import random

items = [random.randint(-100, 100) for i in range(10)]
max_item = None
max_item_index = None
print(items)
for i, item in enumerate(items):
    if (item < 0 and max_item_index is None) or (item < 0 and abs(item) < abs(max_item)):
        max_item = item
        max_item_index = i

print('Max negative: ', max_item)
print('Max negative index: ', max_item_index)
