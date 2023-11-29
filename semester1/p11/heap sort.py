# heap sort
def heapify(arr, n, i):
    terbesar = i
    anak_kiri = 2 * i + 1
    anak_kanan = 2 * i + 2

    if anak_kiri < n and arr[i] < arr[anak_kiri]:
        terbesar = anak_kiri

    if anak_kanan < n and arr[terbesar] < arr[anak_kanan]:
        terbesar = anak_kanan

    if terbesar != i:
        arr[i], arr[terbesar] = arr[terbesar], arr[i]
        heapify(arr, n, terbesar)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

import time as tm
import random as rd

waktu_mulai = tm.perf_counter()

arr_heap_sort = [rd.randint(1, 10000000) for _ in range (10000000)]

waktu_selesai = tm.perf_counter()
waktu_proses = waktu_selesai - waktu_mulai
print(f"Waktu pemrosesan sorting angka random dengan Heap Sort: {waktu_proses: .2} detik")