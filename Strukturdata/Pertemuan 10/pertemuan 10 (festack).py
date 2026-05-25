import stack
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="📊 Stack Visualization", layout="wide")

# Judul
st.title("📊 Stack Visualizer")

# Inisialisasi Stack
if 'stack' not in st.session_state:
    st.session_state.stack = stack.Stack()

# Fungsi tampil stack
def display_stack():
    temp = st.session_state.stack.head
    if temp is None:
        st.write("Stack kosong")
    else:
        while temp:
            st.write(f"👉 {temp.data}")
            temp = temp.next
        st.write("🔚 None")

# Form input
with st.form("input_form"):
    data = st.text_input("Masukkan Data")
    submit = st.form_submit_button("Tambah ke Stack")

    if submit:
        if data:
            st.session_state.stack.push(data)
            st.success(f"{data} ditambahkan ke stack")
            st.rerun()
        else:
            st.warning("Input tidak boleh kosong!")

# Tombol Pop
st.subheader("Aksi Stack")

if st.button("Pop"):
    if not st.session_state.stack.is_empty():
        removed = st.session_state.stack.pop()
        st.success(f"{removed} dihapus dari stack")
    else:
        st.warning("Stack kosong!")
    st.rerun()

# Peek (Top)
st.subheader("Stack Teratas")
top = st.session_state.stack.peek()
st.write(top if top else "Stack kosong")

# Cek kosong
st.subheader("Apakah Stack Kosong?")
st.write(st.session_state.stack.is_empty())

# Tampilkan isi stack
st.subheader("Seluruh Isi Stack")
display_stack()