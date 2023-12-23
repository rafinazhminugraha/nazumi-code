import pandas as pd

csv_file = pd.read_csv("Daftar_Mahasiswa_2018.csv")
df_sort = csv_file.sort_values(by=["Nama"])
df_filter = df_sort.filter(items=["NIM", "Nama", "L/P", "Status", "SKS", "IPK", "Lama Studi(Smt)"])
print("Hasil read, sorting dan filter data csv: \nNo.", df_filter.head(10))

rerata_ipk= csv_file["IPK"].mean()
print(f"\nRata - Rata IPK Mahasiswa Keseluruhan: {rerata_ipk}")

jumlah_laki_laki = csv_file[csv_file['L/P'] == 'L'].shape[0]
jumlah_perempuan = csv_file[csv_file['L/P'] == 'P'].shape[0]

print(f"""
Jumlah Mahasiswa Laki - Laki Kekeseluruhan : {jumlah_laki_laki}
Jumlah Mahasiswa Perempuan Keseluruhan: {jumlah_perempuan}""")

df_perempuan_terdaftar = csv_file[(csv_file['L/P'] == 'P') & (csv_file['Status'] == 'Terdaftar')]
print(f"""
Daftar mahasiswa "perempuan" dengan status 'Terdaftar' Keseluruhan:
{df_perempuan_terdaftar}""")

df_bukan_terdaftar = csv_file[csv_file['Status'] != 'Terdaftar']
print(f"""
Data mahasiswa dengan status bukan 'Terdaftar' Keseluruhan:
{df_bukan_terdaftar}""")