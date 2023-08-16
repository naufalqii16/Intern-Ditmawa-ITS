import pandas as pd
import os

lokasi = "c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace/Bayan/"
output_folder = os.path.join("c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace", "Bayan")

data_awal = pd.read_excel(os.path.join(lokasi, "Registrasi_Bayan_baru.xlsx"))
tambahan = pd.read_excel(os.path.join(lokasi, "Tambahan data Bayan.xlsx"))

# Mengubah kolom 'Nama Lengkap' di data_awal menjadi lowercase
data_awal['Nama'] = data_awal['Nama'].str.lower()

# Mengubah kolom 'Nama' di tambahan menjadi lowercase
tambahan['Nama'] = tambahan['Nama'].str.lower()

data = pd.merge(data_awal, tambahan[['Nama', 'NRP', 'Angkatan']], left_on='Nama', right_on='Nama', how='left')

file_output = os.path.join(output_folder, "data_merger_kedua.xlsx")
data.to_excel(file_output, index=False)


    