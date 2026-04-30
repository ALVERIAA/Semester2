data = [23, 34, 45, 56, 12, 22, 67, 3, 10]
to_find = 22
found = False
for i in range(len(data)):
    found = data[i] == to_find
    if found:
        break
        
if found:
    print("Data ditemukan pada indeks ke-", i)
else:
    print("Data tidak ditemukan dalam list")