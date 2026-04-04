jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

# Tulis kode kamu disini
total_menit = jam * 60 + menit + durasi
jam = total_menit // 60
menit = total_menit % 60

print("Acara berakhir pukul ",jam,":",menit) 