angka_genap = 0
angka_ganjil = 0

angka = int(input("Masukkan angka: "))

while angka!= 0:
    if angka % 2 == 1:
        angka_ganjil += 1
    else:
        angka_genap += 1
    angka = int(input("Masukkan angka: "))


print("Jumlah angka genap:", angka_genap)
print("Jumlah angka ganjil:", angka_ganjil)