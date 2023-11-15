angka = input('masukkan angka:')

if angka.isdigit():
    angka2 = int(angka)
    if angka2 %2==0:
        print('Angka tersebut merupakan angka genap')
    elif angka2 % 2 !=0:
        print('Angka tersebut merupakan angka ganjil')
else:
    print('maaf angka tersebut gak valid')