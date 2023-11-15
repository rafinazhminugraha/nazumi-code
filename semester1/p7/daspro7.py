#looping : for
"""
jumlah_perulangan = 3

for index in range(jumlah_perulangan):
    print(f"index ke {index})
"""

"""k
for i in "python":
    print(f"huruf: {i}")
"""
"""
buah = ["apel", "belimbing", "cari", "durian"]

for i in buah:
    print(f"buah: {i}")
"""

"""l
buah = ["apel", "belimbing", "cari", "durian"]

for i in range(len(buah));
    print(f"buah: {bauh[i]}")
"""

banyakBilangan = int(input("Banyak bilangan: "))
jumlah = 0

for i in range(1, banyakBilangan + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    if bilangan % 2 == 0 or bilangan > 2:
        jumlah += bilangan
        print(jumlah)
        continue
    else:   
        jumlah += 0
            
print(f"Hasil penjumlahan bilangan yang bukan prima: {jumlah}")