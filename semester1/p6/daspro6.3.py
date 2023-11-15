nilai_ujian = int(input("berapa hasil nilai ujian siswa? " ))
kondisi_keungan = int(input("berapa kondisi keungan siswa? "))

if nilai_ujian > 90 and kondisi_keungan < 2000000:
    print("selamat anda mendapatkan beasiswa penuh")
elif 80 < nilai_ujian <= 90 and kondisi_keungan < 4000000:
    print("selamat anda mendapatkan beasiswa parsial")
else:
    print("maaf anda tidak mendapatkan beasiswa")