#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

import random
import time as tm

waktu_mulai = tm.perf_counter()

arr_selection_sort = [random.randint(1, 10000000) for _ in range(10000000)]

waktu_selesai = tm.perf_counter()
waktu_proses = waktu_selesai - waktu_mulai
print(f"Waktu pemrosesan sorting angka random dengan Selection Sort: {waktu_proses: .2} detik")