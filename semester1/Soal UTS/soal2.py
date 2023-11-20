bilangan_genap = []
bilangan_negatif = []

while True:
    bilangan = int(input("Input Bilangan : "))
    if bilangan < 0:
        break
    elif bilangan % 2 == 0:
        bilangan_genap.append(bilangan)
        continue
    elif bilangan % 2 != 0:
        bilangan_negatif.append(bilangan)
        continue

print(f"Jumlah bilangan genap : {sum(bilangan_genap)}")
print(f"Jumlah bilangan negatif : {sum(bilangan_negatif)}")