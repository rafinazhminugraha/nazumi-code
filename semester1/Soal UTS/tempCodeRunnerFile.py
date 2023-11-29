hitung = 0
total = 0
bilangan_sebelumnya = int(input("Input bilangan: "))
while hitung < 3:
    bilangan = int(input("Input bilangan: "))
    if bilangan > bilangan_sebelumnya:
        total += bilangan
        hitung = 0
    else:
        hitung += 1
    bilangan_sebelumnya = bilangan
print("Hasil penjumlahan nilai yang membesar", total)
