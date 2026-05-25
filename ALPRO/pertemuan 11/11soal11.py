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
        
def hari_pada_tahun(tahun, bulan, hari):
    # Validasi bulan
    if bulan < 1 or bulan > 12:
        return None
    # Validasi hari
    if hari < 1 or hari > hari_didalam_bulan(tahun, bulan):
        return None
    
    total_hari = 0
    # Jumlahkan semua hari dari bulan sebelumnya
    for b in range(1, bulan):
        total_hari += hari_didalam_bulan(tahun, b)
    # Tambahkan hari di bulan sekarang
    total_hari += hari
    return total_hari

print(hari_pada_tahun(2000, 12, 31))
