def menambahkanAntrian(antrian, banyak_antrian):
    if len(antrian) < banyak_antrian:
        nomor_antrian = len(antrian)+1
        antrian.append(nomor_antrian)
        print(f"Nomor antrian anda {nomor_antrian}")
    else:
        print("Antrian sudah penuh")

antrian = []

banyak_antrian = int(input("Masukkan jumlah antrian: "))

while True:
    print("\n Selamat Datang Di Klinik")
    print()
    print("1. Ambil Antrian")
    print("2. Keluar")
    print()
    pilihan_user = input("> ")
    if pilihan_user == "1":
        menambahkanAntrian(antrian, banyak_antrian)
    elif pilihan_user == "2":
        break
    else:
        print("Inputan tidak valid")
        
