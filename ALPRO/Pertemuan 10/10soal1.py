pangkat = [x ** 2 for x in range(10)]
print(pangkat)
dua_pangkat = [2 ** i for i in range(10)]
print(dua_pangkat)
ganjil = [x for x in pangkat if x % 2 != 0]
print(ganjil)