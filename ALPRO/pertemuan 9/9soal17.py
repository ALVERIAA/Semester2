data = [23, 34, 45, 56, 12, 22, 67, 3, 10]
largest = data[0]
for i in range(1, len(data)):
    if data[i] > largest:
        largest = data[i]
        
print("Nilai terbesar dalam data:", largest)