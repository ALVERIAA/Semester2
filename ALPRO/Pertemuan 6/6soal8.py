secret_numer = 777
a = 1
while a <= 3:
    tamu = int(input("Masukkan angka: "))
    a += 1
    if tamu == secret_numer:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break

    else:
        print("hahaha ! kamu nyangkut deh di Loop saya")