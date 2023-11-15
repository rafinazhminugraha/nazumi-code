nilai_siswa= [90, 86, 57, 59, 95, 77, 67, 94, 82, 86]

nomor_urut = int(input("nomor berapa siswa yang ingin di cek(1-10)? "))


if nomor_urut >= 1 and nomor_urut <= 10:
    
    nilai = nilai_siswa[nomor_urut - 1]
    
    print(f"Nilai Mtk siswa nomor {nomor_urut} adalah {nilai}")
else:
    print("Nomor siswa tersebut tidak ada")
