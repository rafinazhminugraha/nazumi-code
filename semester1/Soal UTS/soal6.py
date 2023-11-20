n = int(input("masukkan nilai N = "))
total = 0

for i in range (1, n+1):
    bilangan = int(input(f"masukkan bilangan ke{i} = "))
    if bilangan > 1:
        for j in range(2, bilangan):
            if bilangan % j == 0:
                break
        else:
            total += bilangan
print(f"Jumlah bilangan prima adalah {total}")

