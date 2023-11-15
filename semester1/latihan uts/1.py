"""Suhu di kota bandung saat ini 30°C. Haryo ingin mengetahui suhu tersebut
dan suhu di esok hari dalam derajat Fahrenheit (9/5 * C + 32). Bantulah
haryo untuk menghitung suhu dalam dejarat Fahrenheit menggunakan
python!"""

print("suhu di kota bandung hari ini adalah 30 derajat celcius")
suhu = int(input("masukan angka untuk cek suhu dalam satuan farenheit : "))
celcius_ke_farenheit = 9 / 5 * suhu + 32

print(f"suhu {suhu} derajat celcius dalam satua farenheit adalah {celcius_ke_farenheit} derajat farenheit")