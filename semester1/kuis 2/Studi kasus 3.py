def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

jumlah_elemen = int(input("Masukkan jumlah elemen array: "))
arr = []
for i in range(jumlah_elemen):
    elemen = int(input(f"Masukkan elemen ke-{i+1}: "))
    arr.append(elemen)

bubble_sort(arr)
print("Array setelah disortir: ", arr)
