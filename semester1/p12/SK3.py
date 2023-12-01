import time as tm 
def linearSearch(array, cariNilai):
    for i in range (len(array)):
        if array[i] == cariNilai:
            return i
    return -1

def binarySearch(array,cariNilai):
    awal = 0
    akhir = len(array)-1
    tengah = 0

    while awal <= akhir:
        tengah = (akhir + awal) // 2

        if array[tengah] < cariNilai:
            awal = tengah + 1
        elif array[tengah] > cariNilai:
            akhir = tengah - 1
        else:
            return tengah
    return -1


array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 
34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 
60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

nilai = 60
#pemrosesan menggunakan binary search
waktu_mulai = tm.perf_counter()

hasil_linear = linearSearch(array, nilai)

waktu_selesai = tm.perf_counter()
waktu_proses_linear = (waktu_selesai - waktu_mulai) 

print(f"waktu pemrosesan untuk mencari angka 60 menggunakan linear search adalah {waktu_proses_linear: .2} detik")

print()
#pemrosesan menggunakan binary search
waktu_mulai = tm.perf_counter()

hasil_binary = binarySearch(array, nilai)

waktu_selesai = tm.perf_counter() 
waktu_proses_binary = (waktu_selesai - waktu_mulai) 

print(f"waktu pemrosesan untuk mencari angka 60 menggunakan binary search adalah {waktu_proses_binary: .2} detik")