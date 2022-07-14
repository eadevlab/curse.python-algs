import random

items = [random.randint(0, 100) for i in range(20)]
print(items)

max_idx = 0
min_idx = 0

for idx, item in enumerate(items):
    if item < items[min_idx]:
        min_idx = idx
    if item > items[max_idx]:
        max_idx = idx

print('Min index: ', min_idx)
print('Max index: ', max_idx)

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
result = 0
for idx, item in enumerate(items):
    if min_idx < idx < max_idx:
        result += item

print('Result: ', result)
