data_siswa = []

def menyusunDataSiswa(jumlah_siswa):
    
    for i in range(jumlah_siswa):
        data_siswa_nilai = {}
        data_siswa_nilai["nama"] = input("Nama Siswa : ")
        data_siswa_nilai["nilai"] = int(input("Nilai Siswa tersebut : "))
        print()
        
        data_siswa.append(data_siswa_nilai)

def reverseSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["nilai"] < arr[j+1]["nilai"] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def linearSearch(array, cari_nama_siswa):
    for i in range (len(array)):
        if array[i]["nama"] == cari_nama_siswa:
            return i
    return -1

def perankingan(nama_siswa):
    reverseSort(data_siswa)
    hasil_pencarian = linearSearch(data_siswa, nama_siswa)
    
    if hasil_pencarian == -1:
        print(f"{nama_siswa} tidak ada di daftar")
    elif hasil_pencarian < 3:
        print(f"{data_siswa[hasil_pencarian]['nama']} memiliki rangking {hasil_pencarian+1}")
    else:
        print(f"{data_siswa[hasil_pencarian]['nama']} masih harus belajar dengan giat")
        

jumlah_siswa = int(input("Masukkan jumlah siswa: "))
print()

menyusunDataSiswa(jumlah_siswa)

nama_siswa = input("masukan nama siswa: ")

perankingan(nama_siswa)

