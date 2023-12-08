def mencariAngka(angka_dicari):
    if angka_yang_dicari in array:
        return f"Angka {angka_yang_dicari} ditemukan pada index ke {array.index(angka_yang_dicari)}"
    else:
        return "Maaf nilai yang dicari tidak ada di array"

array = []

jumlah_elemen = int(input("Masukkan jumlah elemen array: "))

print()

for i in range(jumlah_elemen):
    elemen_array = input(f"masukkan angka ke {i+1}: ")
    array.append(elemen_array)
    
print()

angka_yang_dicari = input("Masukkan angka yang ingin dicari: ")

print(mencariAngka(angka_yang_dicari))