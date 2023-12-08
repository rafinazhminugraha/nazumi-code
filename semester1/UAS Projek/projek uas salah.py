data_pengguna = {}

def welcomePage():
    print("Welcome to UPS")
        
    print()
    
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        print()

        pilihan_user = input("> ")

        if pilihan_user == "1":
            loginPage()
        elif pilihan_user == "2":
            registerPage()
        elif pilihan_user == "3":
            break
        else:
            print("Inputan tidak valid")
        
def loginPage():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in data_pengguna and data_pengguna[username] == password:
        print("Login berhasil!")
        return
    else:
        while True:
            print("Login gagal")
            print()
            print("1. Login ulang")
            print("2. Register")
            print("3. Kembali ke welcome page")
            print()
        
            pilihan_user = input("> ")
        
            if pilihan_user == "1":
                loginPage()
            elif pilihan_user == "2":
                registerPage()
            elif pilihan_user == "3":
                welcomePage()
            else:
                print("Inputan tidak valid")
                
def registerPage():
    banyak_password = 8
    
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    while len(password) < banyak_password:
        print("Password harus memiliki minimal 8 karakter")
        password = input("Masukkan password: ")
    
    print()
    
    data_pengguna[username] = password
    print("Pengguna berhasil didaftarkan.")
    
    print(data_pengguna)
    
    print()
    
    while True:
        print("1. Login")
        print("2. Kembali ke welcome page")
        
        print()
        
        pilihan_user = input("> ")
        if pilihan_user == "1":
            loginPage()
        elif pilihan_user == "2":
            welcomePage()
        else:
            print("Inputan tidak valid")
        
welcomePage()