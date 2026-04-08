data = []
cek = int(input("Masukkan panjang data: "))
swapped = True

for i in range(cek):
    num = int(input(f"Masukkan data ke-{i + 1}: "))
    data.append(num)
while swapped:
    swapped = False
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True
print("Data setelah diurutkan:", data)