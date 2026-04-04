topi_list = [1, 2, 3, 4, 5 ]
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))
del topi_list[-1]
print(len(topi_list))
print(topi_list)