
"""Anda diminta untuk membuat program Python yang dapat digunakan untuk menghitung nilai akhir mahasiswa berdasarkan nilai ujian mereka.
Program ini harus memungkinkan pengguna untuk memasukkan sejumlah nilai ujian, menghitung nilai akhir, 
dan memberikan peringkat berdasarkan kriteria tertentu. Berikut adalah langkah-langkahnya:
"""

nilai_ujian = []

while True:
    nilai = float(input("masukkan nilai siswa (): "))
    if nilai == -1:
        break
    nilai_ujian.append(nilai)
    
if len(nilai_ujian) == 0:
    print("tidak adda nilai")
else:
    rerata = sum(nilai_ujian) / len(nilai_ujian)
    
    if rerata >= 90:
        pringkat = "A"
    elif rerata >= 80:
        pringkat = "B"
    elif rerata >= 70:
        pringkat = "C"
    else:
        pringkat = "D"
    
print(f"rata rata : {rerata}")
print(f"peringkat: {pringkat}")
        