data = [10, 69, 67, 3, 17]
swapped = True
while swapped:
    swapped = False
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True
print("Data setelah diurutkan:", data)