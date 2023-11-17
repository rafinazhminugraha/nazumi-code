bilangan = int(input("masukkan angka ganjil dan lebih dari 50 = "))

while True:
    if bilangan % 2 == 0 or bilangan <= 50:
        print("angka yang anda masukkan salah")
        bilangan = int(input("inputkan lagi = "))
    else:
        print("benar")
        break


