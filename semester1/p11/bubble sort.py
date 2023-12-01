# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import time as tm
import random as rd

waktu_mulai = tm.perf_counter()

arr_buble_sort = [rd.randint(1, 10000000) for _ in range (10000000)]

waktu_selesai = tm.perf_counter()
waktu_proses = waktu_selesai - waktu_mulai
print(f"Waktu pemrosesan sorting angka random dengan Bubble Sort : {waktu_proses: .2} detik")