def fibonacci(banyak_deret):
    deret_fibonacci = [0, 1]
    for i in range(2, banyak_deret):
        deret_fibonacci.append(deret_fibonacci[i-1] + deret_fibonacci[i-2])
    return deret_fibonacci

banyak_deret = int(input("mau berapa deret: "))
print(fibonacci(banyak_deret))


"""n = int(input("mau berapa deret: "))
deret_fibonacci = [0, 1]

for i in range(2, n):
    deret_fibonacci.append(deret_fibonacci[i-1] + deret_fibonacci[i-2])

hasil = deret_fibonacci
print(f"Deret Fibonacci dengan {n} elemen: {hasil}")"""

"""def deretFibonacci(banyakDeret):
    a, b = 0, 1 
    jumlah = 0
    
    for i in range(banyakDeret):
        print(jumlah, end=" ")
        a, b = b, jumlah
        jumlah = a + b

inputBanyakDeret = int(input("Masukkan banyak deret Fibonacci: "))

deretFibonacci(inputBanyakDeret)"""