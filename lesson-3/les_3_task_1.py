
result = {i: 0 for i in range(2, 10)}
for i in range(2, 100):
    is_ok = True
    for j in range(2, 10):
        if i % j == 0:
            result[j] += 1

# print(result)
for i, v in result.items():
    print(i, v)
