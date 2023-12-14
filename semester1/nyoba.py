import os
import time

def tampilkan_halaman(halaman):
    os.system('cls')  # membersihkan layar terminal di Linux/macOS, gunakan 'cls' di Windows
    print(halaman)

# Daftar konten halaman
halaman1 = "Ini adalah halaman 1"
halaman2 = "Ini adalah halaman 2"
halaman3 = "Ini adalah halaman 3"

# Daftar halaman
daftar_halaman = [halaman1, halaman2, halaman3]

for halaman in daftar_halaman:
    tampilkan_halaman(halaman)
    time.sleep(1)  # Tunggu 2 detik sebelum mengganti halaman