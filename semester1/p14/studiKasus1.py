with open("semester1/p14/nilaiSiswa.txt", "r") as file:
    jumlah = 0
    banyak_data = 0
    
    for i in file:
        nama, skor = i.strip().split(":")
        jumlah += int(skor)
        banyak_data += 1
    rerata = jumlah / banyak_data

print(f"nilai rerata ujian adalah siswa RPL A adalah = {rerata}")