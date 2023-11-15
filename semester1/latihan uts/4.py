"""Buat program Python yang meminta pengguna untuk memasukkan serangkaian angka positif. 
Program harus mencari angka unik dalam serangkaian angka tersebut. 
Angka unik adalah angka yang belum pernah dimasukkan sebelumnya. 
Jika angka tersebut telah dimasukkan sebelumnya, program harus mengabaikannya dan melanjutkan ke angka berikutnya. 
Program berhenti jika pengguna memasukkan angka 0. Setelah program selesai, tampilkan daftar angka unik yang dimasukkan."""

angka_unik = set()

while True:
    number = input("masukkan angka positif: ")
    if number.isnumeric():
        number = int(number)
        if number in angka_unik:
            print("angka sudah ada")
            continue
        elif number == 0:
            break
        angka_unik.add(number)
    else:
        print("masukkan angka yang valid!")
        continue
    
print(f"angka unik yang sudah dimasukkan:{angka_unik}")
#for number in angka_unik:
    #print(number)