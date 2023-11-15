var1 = {
    "Merk": "Honda",
    "Tipe": "HRV",
    "Tahun": 2018,
    "Warna": "Hitam",
    "No. Polisi": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Transmisi": "Manual"
}

print("mobil lama pak oki adalah:")
print(f"merk: ", var1.get("Merk"))
print(f"tipe: ", var1.get("Tipe"))
print(f"warna: ", var1.get("Warna"))
print(f"tahun: ", var1.get("Tahun"))

print("------------------------------------")

print("Masukan informasi detail mobil baru")
var2 = input("merk: ")
var3 = input("tipe mobil: ")
var4 = input("tahun keluaran: ")
var5 = input("warna: ")
var6 = input("No. Polisi: ")
var7 = input("Bensin: ")
var8 = input("transmisi: ")

print("-------------------------------------")
print(F"""
      mobil baru pak oki adalah
      merk: {var2}
      tipe: {var3}
      warna: {var5}
      tahun: {var4}
      """)
print("--------------------------------------")