def tahun_kabisat(tahun):
    if tahun % 4 != 0:
        return False
    elif tahun % 100 != 0:
        return True
    elif tahun % 400 != 0:
        return False
    else:
        return True
    
def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
# data uji
data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]
# testing
for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "-> ", end="")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")