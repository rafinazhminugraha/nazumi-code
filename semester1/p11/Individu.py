# """
# Nama : Rafi Nazhmi Nugraha - 2301303
# Kelas : RPL 1-A
# """
# #bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# import time as tm

# waktu_mulai = tm.perf_counter()

# arr_buble_sort = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76,
# 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

# print(f"angka urut menggunakan bubble sort : {bubble_sort(arr_buble_sort)}") 

# waktu_selesai = tm.perf_counter()
# waktu_proses = waktu_selesai - waktu_mulai
# print(f"Waktu pemrosesan: {waktu_proses: .2} detik")

# """
# Nama : Rafi Nazhmi Nugraha - 2301303
# Kelas : RPL 1-A
# """
#selec sort
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

waktu_mulai = tm.time()

arr_selection_sort = [random.randint(1, 10000000) for _ in range(10000000)]

# print(f"angka urut menggunakan selection sort : {selection_sort(arr_selection_sort)}") 

waktu_selesai = tm.time()
waktu_proses = waktu_selesai - waktu_mulai
print(f"Waktu pemrosesan: {waktu_proses: .2} detik")

# """
# # Nama : Rafi Nazhmi Nugraha - 2301303
# # Kelas : RPL 1-A
# """
# #heap sort
# def heapify(arr, n, i):
#     terbesar = i
#     anak_kiri = 2 * i + 1
#     anak_kanan = 2 * i + 2

#     if anak_kiri < n and arr[i] < arr[anak_kiri]:
#         terbesar = anak_kiri

#     if anak_kanan < n and arr[terbesar] < arr[anak_kanan]:
#         terbesar = anak_kanan

#     if terbesar != i:
#         arr[i], arr[terbesar] = arr[terbesar], arr[i]
#         heapify(arr, n, terbesar)

# def heap_sort(arr):
#     n = len(arr)

#     for i in range(n//2 - 1, -1, -1):
#         heapify(arr, n, i)

#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     return arr

# import time as tm

# waktu_mulai = tm.perf_counter()

# arr_heap_sort = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76,
# 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

# print(f"angka urut menggunakan heap sort : {heap_sort(arr_heap_sort)}") 

# waktu_selesai = tm.perf_counter()
# waktu_proses = waktu_selesai - waktu_mulai
# print(f"Waktu pemrosesan: {waktu_proses: .3} detik")