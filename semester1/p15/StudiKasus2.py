import pandas as pd

df = pd.read_csv("data_penjualan_dummy.csv")

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

total_bulanan = df.groupby(df["Tanggal"].dt.month)["Total"].sum()

rata_rata = df["Total"].mean()

pendapatan_min = df["Total"].min()
pendapatan_max = df["Total"].max()

produk_terlaris = df.groupby("Produk")["Jumlah"].sum().idxmax()

print(f"""
Total pendapatan setiap bulan (bulan berdasarkan angka):
{total_bulanan.to_string(header=False)}""")
print("\nRata-rata pendapatan 2023:", rata_rata)
print("\nPendapatan paling sedikit:", pendapatan_min)
print("Pendapatan paling banyak:", pendapatan_max)
print("\nProduk terlaris yang paling banyak terjual:", produk_terlaris)
