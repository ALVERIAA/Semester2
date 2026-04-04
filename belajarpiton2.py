"""
Sistem Informasi Absensi Mahasiswa Sederhana Menggunakan Python
Dengan data mahasiswa tetap (predefined)
"""

import os

# Data mahasiswa tetap berdasarkan daftar
# Format: {NIM: {'nama': str, 'absensi': [{'tanggal': str, 'status': str}]}}
data_mahasiswa = {
    "2530801001": {"nama": "NAELA NISHFI RAMADHANI", "absensi": []},
    "2530801002": {"nama": "TAUFIK ARROKHMAN", "absensi": []},
    "2530801003": {"nama": "YOHANES DAVID", "absensi": []},
    "2530801004": {"nama": "PRAMA ABID MUZAKKI", "absensi": []},
    "2530801005": {"nama": "PIGA MISBAHUL HAPIDHIIN", "absensi": []},
    "2530801006": {"nama": "FITRIA EKA RACHMADANI", "absensi": []},
    "2530801007": {"nama": "GHIYAS MUHARRARAN", "absensi": []},
    "2530801008": {"nama": "MUSYFIQ FAKHRUZZAMAN", "absensi": []},
    "2530801009": {"nama": "LASIAH", "absensi": []},
    "2530801010": {"nama": "NAHDIYA ILMY", "absensi": []},
    "2530801011": {"nama": "MAULANA AZIDAN GHONI", "absensi": []},
    "2530801012": {"nama": "FAIRUZ IDZIHAR IFTIRAN", "absensi": []},
    "2530801013": {"nama": "PASYA NIZARULLAH", "absensi": []},
    "2530801014": {"nama": "MASDIKA PAHLEPI ISKANDAR", "absensi": []},
    "2530801015": {"nama": "AHMAD DA'IL MUKARROM", "absensi": []},
    "2530801016": {"nama": "AKBAR FABIANSYAH", "absensi": []},
    "2530801017": {"nama": "KHOLIL FIRDAUS", "absensi": []},
    "2530801018": {"nama": "WAWAN MAULANA ENDANG", "absensi": []},
    "2530801019": {"nama": "SAID MUZAKI", "absensi": []},
    "2530801020": {"nama": "KHANDIAS FAYZULHAQ", "absensi": []},
    "2530801021": {"nama": "AUFA NUAIM IBNU ZIYA", "absensi": []},
    "2530801022": {"nama": "NAYLA SABRYNA", "absensi": []},
    "2530801023": {"nama": "ABIE PRAYOGA ALFARISI", "absensi": []},
    "2530801024": {"nama": "MOH. NI'AM BILLI YACHSYI", "absensi": []},
    "2530801025": {"nama": "AL FARID MAULANI", "absensi": []},
    "2530801026": {"nama": "FADRIAL JUNYANA PUTRA", "absensi": []},
    "2530801027": {"nama": "FARRAS FAIRUZABADI KUROZY", "absensi": []},
}

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_judul():
    """Menampilkan judul program"""
    print("=" * 50)
    print("   SISTEM INFORMASI ABSENSI MAHASISWA")
    print("=" * 50)
    print()

def tambah_absensi():
    """Fungsi untuk mencatat kehadiran mahasiswa"""
    print("--- TAMBAH ABSENSI ---")
    # Tampilkan daftar mahasiswa untuk memudahkan
    print("\nDaftar Mahasiswa:")
    for nim, data in data_mahasiswa.items():
        print(f"{nim} - {data['nama']}")
    print()
    
    nim = input("Masukkan NIM mahasiswa: ").strip()
    if nim not in data_mahasiswa:
        print("NIM tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return
    
    print(f"Mahasiswa: {data_mahasiswa[nim]['nama']}")
    tanggal = input("Masukkan tanggal (contoh: 2025-02-18): ").strip()
    if tanggal == "":
        print("Tanggal tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return
    
    print("Pilih status kehadiran:")
    print("1. Hadir")
    print("2. Tidak Hadir")
    pilihan = input("Pilihan (1/2): ").strip()
    
    if pilihan == '1':
        status = "Hadir"
    elif pilihan == '2':
        status = "Tidak Hadir"
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return
    
    # Cek duplikasi absensi untuk tanggal yang sama
    for absen in data_mahasiswa[nim]['absensi']:
        if absen['tanggal'] == tanggal:
            print(f"Absensi untuk tanggal {tanggal} sudah ada!")
            input("Tekan Enter untuk kembali...")
            return
    
    data_mahasiswa[nim]['absensi'].append({
        'tanggal': tanggal,
        'status': status
    })
    print(f"Absensi berhasil ditambahkan untuk {data_mahasiswa[nim]['nama']} pada {tanggal} ({status})")
    input("Tekan Enter untuk kembali...")

def tampilkan_semua_absensi():
    """Menampilkan seluruh data absensi semua mahasiswa"""
    print("--- SEMUA DATA ABSENSI ---")
    print("\nDaftar Mahasiswa dan Riwayat Absensi:")
    for nim, data in data_mahasiswa.items():
        print(f"\nNIM : {nim}")
        print(f"Nama: {data['nama']}")
        if not data['absensi']:
            print("  (Belum ada catatan absensi)")
        else:
            print("  No | Tanggal    | Status")
            print("  ---+------------+--------------")
            for i, absen in enumerate(data['absensi'], start=1):
                print(f"  {i:2} | {absen['tanggal']} | {absen['status']}")
    input("\nTekan Enter untuk kembali...")

def tampilkan_absensi_mahasiswa():
    """Menampilkan absensi per mahasiswa berdasarkan NIM"""
    print("--- ABSENSI PER MAHASISWA ---")
    nim = input("Masukkan NIM mahasiswa: ").strip()
    if nim not in data_mahasiswa:
        print("NIM tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return
    
    data = data_mahasiswa[nim]
    print(f"\nNIM  : {nim}")
    print(f"Nama : {data['nama']}")
    print("\nRiwayat Absensi:")
    if not data['absensi']:
        print("  (Belum ada catatan absensi)")
    else:
        print("  No | Tanggal    | Status")
        print("  ---+------------+--------------")
        for i, absen in enumerate(data['absensi'], start=1):
            print(f"  {i:2} | {absen['tanggal']} | {absen['status']}")
    input("\nTekan Enter untuk kembali...")

def rekap_persentase():
    """Menghitung dan menampilkan persentase kehadiran semua mahasiswa"""
    print("--- REKAP PERSENTASE KEHADIRAN ---")
    print("\nPersentase Kehadiran Mahasiswa:")
    print("NIM        | Nama                      | Total Hadir | Total Pertemuan | Persentase")
    print("-----------+---------------------------+-------------+-----------------+-----------")
    for nim, data in data_mahasiswa.items():
        total_pertemuan = len(data['absensi'])
        if total_pertemuan == 0:
            persentase = 0
            total_hadir = 0
        else:
            total_hadir = sum(1 for absen in data['absensi'] if absen['status'] == "Hadir")
            persentase = (total_hadir / total_pertemuan) * 100
        
        print(f"{nim:9} | {data['nama']:25} | {total_hadir:11} | {total_pertemuan:15} | {persentase:6.2f}%")
    input("\nTekan Enter untuk kembali...")

def main():
    """Program utama"""
    while True:
        clear_screen()
        tampilkan_judul()
        print("MENU UTAMA:")
        print("1. Tambah Absensi")
        print("2. Lihat Semua Absensi")
        print("3. Lihat Absensi per Mahasiswa")
        print("4. Rekap Persentase Kehadiran")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            clear_screen()
            tambah_absensi()
        elif pilihan == '2':
            clear_screen()
            tampilkan_semua_absensi()
        elif pilihan == '3':
            clear_screen()
            tampilkan_absensi_mahasiswa()
        elif pilihan == '4':
            clear_screen()
            rekap_persentase()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem absensi.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()