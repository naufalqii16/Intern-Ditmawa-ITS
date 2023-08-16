import pandas as pd
import numpy as np
import os

lokasi = "c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace/Bayan/"
output_folder = os.path.join("c:/Users/Naufalqii/Downloads/magang ditmawa/Workspace", "Bayan")

def bobot_penghasilan(x):
    if x <= 500000:
        return 300
    else :
        return 300 - 3*(x-500000)/200000

def bobot_ukt(x):
    return 200 - 4*x/300000

def bobot_rata_raport(x):
    if x < 75:
        return 0
    elif x == 75:
        return 8
    else :
        return (x-75)*8
    
def bobot_prestasi(x):
    return x*40

def bobot_jurusan(x):
    jurusan_prioritas = ["teknik industri" , "teknik lingkungan", "teknik mesin", "teknik sipil"]
    if x.lower() in jurusan_prioritas:
        return 100
    else :
        return 0
    
def total_nilai(penghasilan, ukt, rata_raport, prestasi, jurusan):
    return bobot_penghasilan(penghasilan) + bobot_ukt(ukt) + bobot_rata_raport(rata_raport) + bobot_prestasi(prestasi) + bobot_jurusan(jurusan)

data = pd.read_excel(os.path.join(lokasi, "Registrasi_Bayan_baru.xlsx"))

data["total_nilai"] = data.apply(lambda x: total_nilai(x["Penghasilan Orang Tua (Gabungan)"], x["UKT"], x["Nilai Rata-Rata Raport (Kelas XII)  SMA"], x["Prestasi"], x["Departemen"]), axis=1)

file_output = os.path.join(output_folder, "Pembobotan_Bayan.xlsx")
data.to_excel(file_output, index=False)

    