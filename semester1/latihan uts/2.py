"""Berikut ini contoh dari barisan bilangan kelipatan 3: 3, 6, 9, 12, 15, 18, 21, dst.
Saat ini, Asep ingin mencari jumlah dari barisan bilangan kelipatan 3
dibawah 10. Namun, Asep ingat bahwa kemarin dia juga ingin mencari
dibawah 23. Bantulah Asep dalam mencari jumlah barisan bilangan
kelipatan 3!"""

nilai = int(input("masukan angka :  "))

jumlah = 0

for angka in range (3, nilai, 3):
    jumlah += angka
    
print(jumlah)