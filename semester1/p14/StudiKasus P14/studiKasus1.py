with open("nilaiSiswa.txt", "r") as file:
    jumlah = 0
    banyak_data = 0
    
    for i in file:
        nama, skor = i.strip().split(":")
        jumlah += int(skor)
        banyak_data += 1
    rerata = jumlah / banyak_data

print(f"nilai rerata ujian adalah siswa RPL A adalah = {rerata}")

"""note = maaf... Tolong jangan lupa pake 'Run Without Debugging (CTRL + F5)' 
karna takut ada kesalahan path directory perbedaan device, Terimakasih"""