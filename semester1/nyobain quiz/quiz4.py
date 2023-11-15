var1 = [
    "T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok",
    "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"
]

var2 = [
    "T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok",
    "Gamis", "Tas", "Topi", "Sepatu", "Sendal", "Ikat Rambut", "Kerudung"
]

var3 = len(var1)

var4 = len(var2)

print("Daftar barang jualan bulan Juli adalah ")
for barang in var1:
    print(f"- {barang}")

print(f"Jumlah barang di bulan Juli: {var3}")

print("Daftar barang jualan bulan ini adalah ")
for barang in var2:
    print(f"- {barang}")

print(f"Jumlah barang di bulan ini: {var4}")

