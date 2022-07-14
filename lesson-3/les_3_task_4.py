import random

items = [random.randint(1, 10) for i in range(100)]
frq_cnt = 0
frq_number = 0
for item in items:
    item_frq = len([i for i in items if i == item])
    if item_frq > frq_cnt:
        frq_cnt = item_frq
        frq_number = item

# print(items)
print(frq_number)
