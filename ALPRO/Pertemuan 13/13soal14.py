kelas_informatika = {}

while True:
    nama = input("Masukkan nama mahasiswa: ")
    if nama == "":
        break

    try:
        nilai = int(input("Masukkan nilai (0-10): "))
        if nilai not in range(0, 11):
            print("Nilai harus 0-10!")
            continue
    except:
        print("Input nilai harus angka!")
        continue

    if nama in kelas_informatika:
        kelas_informatika[nama] += (nilai,)
    else:
        kelas_informatika[nama] = (nilai,)

for nama in sorted(kelas_informatika.keys()):
    total = sum(kelas_informatika[nama])
    jumlah = len(kelas_informatika[nama])
    print(nama, ":", total / jumlah)