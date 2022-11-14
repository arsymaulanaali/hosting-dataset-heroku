import streamlit as st

st.title("Sistem Klasifikasi Data")
st.write("""
# Web Apps - Klasifikasi Menu Makanan Dataset
Applikasi Berbasis Web untuk Mengklasifikasi Jenis **Menu Makanan**
""")

algoritma = st.sidebar.selectbox(
    "Pilih Algoritma",
    ("KNN", "Naive Bayes", "Random Forest")
)
st.subheader("Parameter Inputan")

Per_Serve_Size = st.number_input("Masuukan Per Serve Size :")
Energy = st.number_input("Masuukan Energy :")
Protein = st.number_input("Masuukan Protein :")
Total_fat = st.number_input("Masukkan Total fat :")
Sat_Fat = st.number_input("Masukkan Sat Fat :")
Trans_fat = st.number_input("Masukkan Trans fat :")
Cholesterols = st.number_input("Masukkan Cholesterols :")
Total_carbohydrate = st.number_input("Masukkan Total carbohydrate :")
Total_Sugars = st.number_input("Masukkan Total Sugars :")
Added_Sugars = st.number_input("Masukkan Added Sugars :")
Sodium = st.number_input("Masukkan Sodium :")
hasil = st.button("Cek Klasifikasi")

st.subheader("Hasil Klasifikasi")
st.write(f"Class   = ")

st.write(f"Algoritma = {algoritma}")
st.write(f"Hasil Akurasi   = ")