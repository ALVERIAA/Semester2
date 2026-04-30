def pipeline_manajemen_log(logs, batch_baru, limit):
    """
    TUGAS 1: PURE LIST - DATA PIPELINE (C6)
    
    Skenario:
    Anda sedang merancang urutan pemrosesan log sistem.
    
    Aturan (Tanpa IF):
    1. Tambahkan seluruh elemen dari 'batch_baru' ke dalam 'logs'.
    2. Urutkan seluruh data secara alfabetis (A-Z).
    3. Ambil data sebanyak 'limit' dari urutan PALING AKHIR.
    4. Kembalikan hasilnya dalam bentuk LIST.
    
    Input:
        logs (List): ["WARN", "INFO"]
        batch_baru (List): ["ERROR", "DEBUG"]
        limit (Int): 2
    Output:
        List: ["INFO", "WARN"] (Contoh setelah sort & slice)
    """
    # isi Jawaban dibawah ini
    gabung = logs + batch_baru          # 1. gabungkan
    urut = sorted(gabung)              # 2. urutkan A-Z
    hasil = urut[-limit:]              # 3. ambil dari belakang
    return hasil                       # 4. kembalikan

logs = ["WARN", "INFO"]
batch_baru = ["ERROR", "DEBUG"]
limit = 2

print(pipeline_manajemen_log(logs, batch_baru, limit))
    
pass