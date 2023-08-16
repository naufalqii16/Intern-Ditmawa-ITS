import pandas as pd
import numpy as np
import os

# Tentukan nama file untuk setiap data
data_full_nonIPK_sebelumnya = "kotor_14_agus_sore.xlsx"
data_diamati_nonIPK = "kotor_15_agus.xlsx"
data_diamati_berIPK = "kotor_beripk_15_agus.xlsx"
nama_file_output = "coba_output3.xlsx"

kolom_terpilih = ['No.', 'Semester', 'Singkatan', 'Prodi', 'NRP', 'Nama', 'Status Beasiswa', 'SKS Total', 'SKS Lulus', 'Status Akademik']

# Tentukan alamat folder tempat file-file berada
folder = "c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace/flag 5/"
output_folder = os.path.join("c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace", "data_bersih_flag5")

def get_data():
    data_awal = pd.read_excel(os.path.join(folder, data_full_nonIPK_sebelumnya), usecols=kolom_terpilih)
    data_diamati = pd.read_excel(os.path.join(folder, data_diamati_nonIPK), usecols=kolom_terpilih)
    data_ber_ipk = pd.read_excel(os.path.join(folder, data_diamati_berIPK))
    return data_awal, data_diamati, data_ber_ipk

def seleksi_data(data_awal, data_diamati):
    # Seleksi data yang tidak ada di data awal
    kunci_b = data_awal['NRP'].tolist()
    data_diamati = data_diamati[~data_diamati['NRP'].isin(kunci_b)]

    if data_diamati.empty:
        print("\nTidak ada data terbaru\n")
        exit()
        
    return data_diamati
    
def rename_kolom(data_diamati, data_ber_ipk):
    data_diamati = data_diamati.rename(columns={'Status Akademik': 'Status Akademik Ganjil'})
    data_ber_ipk = data_ber_ipk.rename(columns={'Status Akademik': 'Status Akademik Genap', 'Biaya': 'UKT', 'Unnamed: 14': 'Biaya Hidup' })
    return data_diamati, data_ber_ipk

def delete_first_row(data_diamati):
    if(np.isnan(data_diamati['No.'].iloc[0])):
        data_diamati = data_diamati.iloc[1:]
    return data_diamati

def merge_data(data_diamati, data_ber_ipk):
    # Gabungkan data semester ber IPK dengan data yang tidak ada nilai IPK nya
    df_merged = pd.merge(data_diamati, data_ber_ipk[['NRP', 'Status Akademik Genap','UKT','Biaya Hidup', 'IPS', 'IPK']], on=['NRP'], how='left')
    if df_merged.duplicated().any():
        df_merged = df_merged.drop_duplicates()
    file_output = os.path.join(output_folder, nama_file_output)
    df_merged.to_excel(file_output, index=False)

# Panggil semua fungsi dan jalankan alur pemrosesan data
data_awal, data_diamati, data_ber_ipk = get_data()
data_diamati = seleksi_data(data_awal, data_diamati)
data_diamati, data_ber_ipk = rename_kolom(data_diamati, data_ber_ipk)
data_diamati = delete_first_row(data_diamati)
merge_data(data_diamati, data_ber_ipk)
