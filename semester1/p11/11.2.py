def heapify(arr, n, i):
    largest = i  # Menginisialisasi simpul terbesar sebagai root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Bandingkan dengan anak kiri
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    # Bandingkan dengan anak kanan
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Jika simpul terbesar tidak berada di root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Tukar dengan root
        heapify(arr, n, largest)  # Rekursif untuk memastikan sub-tree juga memenuhi properti heap

def heap_sort(arr):
    n = len(arr)

    # Membangun max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Ekstraksi elemen satu per satu
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Tukar elemen pertama dengan elemen terakhir
        heapify(arr, i, 0)  # Memastikan sub-tree yang tersisa juga merupakan max heap

# Contoh penggunaan:
arr_heap_sort = [12, 11, 13, 5, 6, 7, 16, 9, 17, 20]
heap_sort(arr_heap_sort)
print("Sorted array using Heap Sort:", arr_heap_sort)
