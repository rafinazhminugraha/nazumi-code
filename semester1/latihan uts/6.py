kode = "adm123"
percobaan = 0

while percobaan < 3:
    input_kode = input("Masukkan kode akses: ")

    if input_kode == kode:
        print("Sign-in berhasil. Selamat datang di achmad pay")
        break
    else:
        print("Kode akses salah. Coba lagi.")
        percobaan += 1

if percobaan == 3:
    print("udah coba 3 kali. Sign-in gagal.")
