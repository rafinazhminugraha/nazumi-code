var1 = (input("masukan angka yang ingin di cek: "))

if var1.isnumeric():
    var2 = int(var1)
    if var2 % 2 == 0:
        print (f"{var2} adalah bilangan genap")
    elif var2 %2 != 0:
        print (f"{var2} adalah angka ganjil")
else:
    print("maaf angka tersebut gak valid")