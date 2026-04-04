"""
Sistem Informasi Absensi Mahasiswa Sederhana
Menggunakan Python
"""

import os

# Inisialisasi penyimpanan data
# Format: {NIM: {'nama': str, 'absensi': [{'tanggal': str, 'status': str}]}}
data_mahasiswa = {}

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_judul():
    """Menampilkan judul program"""
    print("=" * 50)
    print("   SISTEM INFORMASI ABSENSI MAHASISWA")
    print("=" * 50)
    print()

def tambah_mahasiswa():
    """Fungsi untuk menambah data mahasiswa baru"""
    print("--- TAMBAH MAHASISWA ---")
    nim = input("Masukkan NIM: ")
    if nim in data_mahasiswa:
        print("NIM sudah terdaftar!")
        input("Tekan Enter untuk kembali...")
        return
    
    nama = input("Masukkan Nama: ")
    if nama == "":
        print("Nama tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return
    
    data_mahasiswa[nim] = {
        'nama': nama,
        'absensi': []
    }
    print(f"Mahasiswa {nama} (NIM: {nim}) berhasil ditambahkan!")
    input("Tekan Enter untuk kembali...")

def tambah_absensi():
    """Fungsi untuk mencatat kehadiran mahasiswa"""
    print("--- TAMBAH ABSENSI ---")
    if not data_mahasiswa:
        print("Belum ada data mahasiswa. Silakan tambah mahasiswa terlebih dahulu.")
        input("Tekan Enter untuk kembali...")
        return
    
    nim = input("Masukkan NIM mahasiswa: ")
    if nim not in data_mahasiswa:
        print("NIM tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return
    
    print(f"Mahasiswa: {data_mahasiswa[nim]['nama']}")
    tanggal = input("Masukkan tanggal (contoh: 2025-02-18): ")
    if tanggal == "":
        print("Tanggal tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return
    
    print("Pilih status kehadiran:")
    print("1. Hadir")
    print("2. Tidak Hadir")
    pilihan = input("Pilihan (1/2): ")
    
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
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        input("Tekan Enter untuk kembali...")
        return
    
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
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        input("Tekan Enter untuk kembali...")
        return
    
    nim = input("Masukkan NIM mahasiswa: ")
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
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        input("Tekan Enter untuk kembali...")
        return
    
    print("\nPersentase Kehadiran Mahasiswa:")
    print("NIM        | Nama                 | Total Hadir | Total Pertemuan | Persentase")
    print("-----------+----------------------+-------------+-----------------+-----------")
    for nim, data in data_mahasiswa.items():
        total_pertemuan = len(data['absensi'])
        if total_pertemuan == 0:
            persentase = 0
            total_hadir = 0
        else:
            total_hadir = sum(1 for absen in data['absensi'] if absen['status'] == "Hadir")
            persentase = (total_hadir / total_pertemuan) * 100
        
        print(f"{nim:9} | {data['nama']:20} | {total_hadir:11} | {total_pertemuan:15} | {persentase:6.2f}%")
    input("\nTekan Enter untuk kembali...")

def main():
    """Program utama"""
    while True:
        clear_screen()
        tampilkan_judul()
        print("MENU UTAMA:")
        print("1. Tambah Mahasiswa")
        print("2. Tambah Absensi")
        print("3. Lihat Semua Absensi")
        print("4. Lihat Absensi per Mahasiswa")
        print("5. Rekap Persentase Kehadiran")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == '1':
            clear_screen()
            tambah_mahasiswa()
        elif pilihan == '2':
            clear_screen()
            tambah_absensi()
        elif pilihan == '3':
            clear_screen()
            tampilkan_semua_absensi()
        elif pilihan == '4':
            clear_screen()
            tampilkan_absensi_mahasiswa()
        elif pilihan == '5':
            clear_screen()
            rekap_persentase()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem absensi.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-6.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()