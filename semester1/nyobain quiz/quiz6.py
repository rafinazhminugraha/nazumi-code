var1 = {
    "Merk": "Honda",
    "Tipe": "HRV",
    "Tahun": 2018,
    "Warna": "Hitam",
    "No. Polisi": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Transmisi": "Manual"
}

print("Informasi Mobil Lama Pak Oki:")
for key, value in var1.items():
    print(f"{key}: {value}")

print("-------------------------------------")

var2 = {
    "Merk": "Honda",
    "Tipe": "Civic Turbo",
    "Tahun": 2023,
    "Warna": "Merah",
    "No. Polisi": "D 0 KI",
    "Bensin": "Pertamax",
    "Transmisi": "Automatic"
}

print("Informasi Mobil Baru Pak Oki:")
for key, value in var2.items():
    print(f"{key}: {value}")