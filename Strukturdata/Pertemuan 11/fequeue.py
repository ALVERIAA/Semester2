import streamlit as st
from gtts import gTTS
import os

# Judul Aplikasi
st.title("🏥 Antrian Klinik dengan Nama")

# Inisiasi antrian di session state
if 'daftar_antrian' not in st.session_state:
    st.session_state.daftar_antrian = []

# --- BAGIAN AMBIL ANTRIAN ---
st.subheader("Registrasi Pasien")

# Input Nama Pasien
nama_pasien = st.text_input("Masukkan Nama Anda:", key="input_nama")

if st.button("Ambil Nomor Antrian", key="btn_ambil"):
    if nama_pasien:  # Cek jika nama tidak kosong
        st.session_state.daftar_antrian.append(nama_pasien)
        nomor = len(st.session_state.daftar_antrian)
        
        st.success(f"Berhasil! {nama_pasien}, Anda berada di urutan ke-{nomor}")
        
        # Buat suara konfirmasi
        text_ambil = f"Terima kasih {nama_pasien}, silakan menunggu."
        tts = gTTS(text=text_ambil, lang='id')
        tts.save("ambil.mp3")
        st.audio("ambil.mp3", format="audio/mp3", autoplay=True)
    else:
        st.error("Silakan masukkan nama terlebih dahulu!")

st.divider()

# --- BAGIAN PANGGIL ANTRIAN ---
st.subheader("Panggil Pasien")
if st.button("Panggil Pasien Berikutnya", key="btn_panggil"):
    if len(st.session_state.daftar_antrian) > 0:
        # Mengambil nama pasien paling depan (Queue)
        pasien_dipanggil = st.session_state.daftar_antrian.pop(0)
        
        st.warning(f"Memanggil Pasien: **{pasien_dipanggil}**")
        
        # Buat suara panggilan dengan nama
        text_panggil = f"Pasien atas nama {pasien_dipanggil}, silakan masuk ke ruang periksa."
        tts = gTTS(text=text_panggil, lang='id')
        tts.save("panggil.mp3")
        st.audio("panggil.mp3", format="audio/mp3", autoplay=True)
    else:
        st.error("Tidak ada pasien dalam antrian.")

# Menampilkan daftar tunggu di samping
st.sidebar.write("### 📝 Daftar Tunggu Nama:")
for i, nama in enumerate(st.session_state.daftar_antrian):
    st.sidebar.write(f"{i+1}. {nama}")