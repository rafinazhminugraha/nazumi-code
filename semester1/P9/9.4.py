def menu_login():
    kesempatan_login = 0
    
    masukan_username = input("username: ")
    
    while kesempatan_login < 3:
        masukan_password = input("password: ")
        if masukan_password == "Latihan":
            print(f"""
HALO!
Selamat Datang {masukan_username}
                  """)
            break
        else:
            kesempatan_login += 1
            print("Password salah. Kesempatan tersisa:", 3 - kesempatan_login)
            continue 
        
menu_login()           