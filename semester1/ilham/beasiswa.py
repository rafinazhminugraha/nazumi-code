nilai = int(input("nilai ujian siswa? " ))
keuangan = int(input("berapa keungan siswa? "))

if nilai > 90 and keuangan < 2000000:
    print("beasiswa penuh")
elif 80 < nilai <= 90 and keuangan < 4000000:
    print("beasiswa parsial")
else:
    print("tidak mendapatkan beasiswa")