"""Buatkan sebuah program yang meminta 3 digit terakhir dari nim dan menentukan kelasnya. J
ika nomornya lebih dari 0 dan kurang dari sama dengan 300 maka akan masuk ke kelas A, 
jika lebih dari 300 dan sama dengan 800 maka akan masuk ke kelas B, 
jika lebih dari 800 maka akan masuk ke kelas C. Jika nomornya ganjil, maka akan masuk ke kelas 1. 
Tetapi jika genap akan masuk ke kelas 2.

Contoh:
NIM (3 digit terakhir): 203

Anda masuk ke kelas A-1"""

nim = int(input("masukkan 3 angka terakhir nim anda =  "))

if nim > 0 and nim <= 300:
    if nim % 2 != 0:
        print("anda masuk ke kelas A-1")
    else:
        print("anda masuk ke kelas A-2")
        
elif nim > 300 and nim <= 800:
    if nim % 2 != 0:
        print("anda masuk ke kelas B-1")
    else:
        print("anda masuk ke kelas B-2")
        
elif nim > 800:
    if nim % 2 != 0:
        print("anda masuk ke kelas C-1")
    else:
        print("anda masuk ke kelas C-2")