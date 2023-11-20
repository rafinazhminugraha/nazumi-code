kesempatan_login = 3

while True:
    username = input("Username : ")
    password = input("Password : ")
    
    if username == "utsdaspro" and password == "rpl2023":
        print("Selamat datng di aplikasi prodil RPL")
        break
    else:
        kesempatan_login -= 1
        if kesempatan_login == 2:
            print(f"login salah! kesempatan anda {kesempatan_login}x lagi")
            continue
        elif kesempatan_login == 1:
            print(f"login salah! kesempatan anda {kesempatan_login}x lagi")
            continue
        elif kesempatan_login == 0:
            print("Anda tidak diperkenankan masuk aplikasi ini")
            break