secret_number = 777
print(
"""
    +==============================================================+
    | Selamat datang di game saya, Muggle!                         |
    | masukan suatu angka untuk dan tebak angka berapa             |
    | yang saya pilih untuk kamu                                   |
    | jadi berapa angka rahasianya                                 |
    |                                                              |
    |                                                              |
    +==============================================================+ 
""")
tamu = int(input("Masukkan angka: "))

while tamu != secret_number:
    print("hahaha ! kamu nyangkut deh di Loop saya")
    tamu = int(input("Masukkan angka: "))

print("Selamat, Muggle! kamu bebas sekarang!")