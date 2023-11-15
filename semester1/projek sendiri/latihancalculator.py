angka1 = float(input("masukkan angka pertama : "))
operator = input("masukan operator (+, -, *, /): ")
angka2 = float(input("masukan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    while True:
        if angka2 != 0:
            hasil = angka1 / angka2
            break
        else:
            print("angka kedua tidak boleh 0")
            angka2 = float(input("masukan angka lagi: "))
        
else:
    print("operator tidak ditemukan")
    
print(f"hasil perhitungan = {hasil}")