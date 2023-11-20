import numpy as np

def multiply_with_scalar(arr, scalar):
    return arr * scalar

data = np.array[1, 2, 3, 4, 5] # Contoh array NumPy

hasil = multiply_with_scalar(data, 10)
print("Hasil perkalian setiap elemen dengan angka 10 adalah:", hasil)
print(type(hasil))