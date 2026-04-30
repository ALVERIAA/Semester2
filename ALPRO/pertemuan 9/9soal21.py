data = [1, 2, 4, 4, 1, 5, 2, 6, 2, 9]
second = []
for i in data:
    if i not in second:
        second.append(i)
print("Data tanpa duplikat:", second)