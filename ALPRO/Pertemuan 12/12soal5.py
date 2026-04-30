def hitung_imt(berat, tinggi):
    imt = berat / (tinggi ** 2)
    return imt

berat = 70
tinggi = 1.75

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["normal", "gemuk", "obesitas"]
if index_massa_tubuh < 25:
    print("index massa tubuh:", index_massa_tubuh, "- Kategori:", kategori[0])
elif index_massa_tubuh < 30:
    print("index massa tubuh:", index_massa_tubuh, "- Kategori:", kategori[1])
else:
    print("index massa tubuh:", index_massa_tubuh, "- Kategori:", kategori[2], "anda harus diet woyy")