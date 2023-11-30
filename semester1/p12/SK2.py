def linearSearch(array, cariNilai):
    for i in range (len(array)):
        if array[i] == cariNilai:
            return i

    return -1

nama_mahasiswa = ["achmad", "shandy", "nashirul", "zam", "mahesa", "kyo", "christian",
                  "satria", "nanda", "daffa", "fadhil", "fahmi", "fahreza", "fahri",
                 "fajar", "fandi", "fandi", "fandi", "fandi", "fandi"]

nama = input("masukkan nama mahasiswa yang ingin dicari : ")
hasil = linearSearch(nama_mahasiswa, nama )

if hasil != -1:
    print(f"{nama} adalah mahasiswa UPI prodi RPL")
else:
    print(f"{nama} bukanlah mahasiswa UPI prodi RPL")