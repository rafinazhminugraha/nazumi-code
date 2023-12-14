from colorama import init, Style
from colorama import init, Fore, Style
# from tkinter import *
# from PIL import ImageTk, Image
# from ascii_magic import from_image_file
import os
import time
# image_path = "path/to/your/image.jpg"
# ascii_art = from_image_file(image_path)
# print(ascii_art)

init()

pengguna_saat_ini = None
data_pengguna = []
status_login = False

# def tampilkan_gambar(namafile):
#     root = Tk()
#     img = ImageTk.PhotoImage(Image.open(namafile))
#     panel = Label(root, image = img)
#     panel.pack(side = "bottom", fill = "both", expand = "yes")
#     root.mainloop()

def printMenu(*menu):
    for i, item in enumerate(menu):
        print(f"[{i+1}] {item.title()}")

def printTitle():
    os.system("cls")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}\n        UPS")
    print(Style.RESET_ALL)
    # print(pengguna_saat_ini)
    # print(type(pengguna_saat_ini))
    # print(data_pengguna)
    # print(type(data_pengguna))
    print("━━━━━━━━━━━━━━━━━━━━")
    print()
    
def inputanInvalid():
    print(f"{Fore.RED}Inputan tidak valid")
    print(Style.RESET_ALL)
    time.sleep(1)
    
# def menuUtamaTitle():
#     os.system("cls")
#     print(f"{Fore.CYAN}\nUPS")
#     print(Style.RESET_ALL)

def welcomePage():
    global status_login
    global pengguna_saat_ini
    while True:
        printTitle()
        printMenu("login", "register", "exit")
        print()
        pilihan_user = input("> ")
        if pilihan_user == "1":
            loginPage()
            break
        elif pilihan_user == "2":
            registerPage()
        elif pilihan_user == "3":
            print(f"{Fore.CYAN}Terimakasih Telah Menggunakan UPS")
            print(Style.RESET_ALL)
            time.sleep(1)
            os.system("cls")
            exit()
        else:
            inputanInvalid()
            

def loginPage():
    global status_login
    global pengguna_saat_ini
    while True:
        printTitle()
        # username = input("Username: ")
        # password = input("Password: ")
        # if username in data_pengguna and data_pengguna[username] == password:
        #     print(f"{Fore.GREEN}\nSelamat Datang {username}")
        #     print(Style.RESET_ALL)
        #     lanjutkan = input("Tekan Enter Untuk Melanjutkan")
        #     print()
        #     status_login = True
        #     return status_login
        nama = input("Nama: ")
        while len(nama) < 1:
            print(f"{Fore.RED}Username tidak boleh kosong")
            print(Style.RESET_ALL)
            time.sleep(1)
            printTitle()
            nama = input("Nama: ")
        
        password = input("Password: ")
        while len(password) < 8:
            print(f"{Fore.RED}Password minimal 8 karakter")
            print(Style.RESET_ALL)
            time.sleep(1)
            printTitle()
            print(f"Nama: {nama}")
            password = input("Password: ")
            
        for pengguna in data_pengguna:
            if pengguna["nama"] == nama and pengguna["password"] == password:
                print(f"{Fore.GREEN}\nSelamat Datang {nama}")
                print(Style.RESET_ALL)
                input("Tekan Enter Untuk Melanjutkan")
                print()
                pengguna_saat_ini = pengguna
                status_login = True
                return status_login
        # for user, password in data_pengguna.items():
        #     if user == nama and password == password:
        #         print(f"{Fore.GREEN}\nSelamat Datang {nama}")
        #         print(Style.RESET_ALL)
        #         input("Tekan Enter Untuk Melanjutkan")
        #         print()
        #         status_login = True
        #         return status_login

        # if not berhasil_login:
        #     print(f"{Fore.RED}Gagal Login")
        #     print(Style.RESET_ALL)
        else:
            print(f"{Fore.RED}Login gagal")
            print(Style.RESET_ALL)
            time.sleep(1)
            while True:
                printTitle()
                printMenu("login ulang", "register", "kembali ke menu utama" )
                print()
                pilihan_user = input("> ")
                if pilihan_user == "1":
                    break
                elif pilihan_user == "2":
                    registerPage()
                    return False
                elif pilihan_user == "3":
                    return False
                else:
                    inputanInvalid()
                    

def registerPage():
    global data_pengguna
    printTitle()
    nama = input("Nama: ")
    while len(nama) < 1:
        print(f"{Fore.RED}Tidak boleh kosong")
        print(Style.RESET_ALL)
        time.sleep(1)
        printTitle()
        nama = input("Nama: ")  
        
    password = input("Password: ")
    while len(password) < 8:
        print(f"{Fore.RED}Password harus memiliki minimal 8 karakter")
        print(Style.RESET_ALL)
        time.sleep(1)
        printTitle()
        print(f"Nama: {nama}")
        password = input("Password: ")
        
    kelamin = input("Kelamin: ")
    while len(kelamin) < 1:
        print(f"{Fore.RED}Tidak boleh kosong")
        print(Style.RESET_ALL)
        time.sleep(1)
        printTitle()
        print(f"Nama: {nama}")
        print(f"Password: {password}")
        kelamin = input("Kelamin: ")
        
    alamat = input("Alamat: ")
    while len(alamat) < 1:
        print(f"{Fore.RED}Tidak boleh kosong")
        print(Style.RESET_ALL)
        time.sleep(1)
        printTitle()
        print(f"Nama: {nama}")
        print(f"Password: {password}")
        print(f"Kelamin: {kelamin}")
        alamat = input("Alamat: ")
        
    nomor_hp = input("Nomor HP: ")
    while len(nomor_hp) < 1:
        print(f"{Fore.RED}Tidak boleh kosong")
        print(Style.RESET_ALL)
        time.sleep(1)
        printTitle()
        print(f"Nama: {nama}")
        print(f"Password: {password}")
        print(f"Kelamin: {kelamin}")
        print(f"Alamat: {alamat}")
        nomor_hp = input("Nomor HP: ")
        
    riwayat_penyakit = input("Riwayat Penyakit (jika tidak ada - saja): ")
    while len(riwayat_penyakit) < 1:
        print(f'{Fore.RED}isi dengan strip "-" bila tidak ada')
        print(Style.RESET_ALL)
        time.sleep(2)
        printTitle()
        print(f"Nama: {nama}")
        print(f"Password: {password}")
        print(f"Kelamin: {kelamin}")
        print(f"Alamat: {alamat}")
        print(f"Nomor HP: {nomor_hp}")
        riwayat_penyakit = input("Riwayat Penyakit (jika tidak ada - saja): ")
        
    print()
    pengguna = {
        "nama": nama, 
        "password": password, 
        "kelamin": kelamin, 
        "alamat": alamat, 
        "nomor_hp": nomor_hp, 
        "riwayat_penyakit": riwayat_penyakit}
    
    data_pengguna.append(pengguna)
    
    print(pengguna)
    
    print(f"{Fore.GREEN}Pengguna berhasil didaftarkan.")
    print(Style.RESET_ALL)
    time.sleep(1)

def menuObat():
    printTitle()
    
    list_obat = [
        {"nama": "Bisolvon", "Jenis Obat": "Obat Batuk", "Kemasan": "Botol", "Isi": "60 ml" },
        {"nama": "Flutamol", "Jenis Obat": "Obat Flu", "Kemasan": "Botol", "Isi": "50 ml" },
        {"nama": "Sanmol", "Jenis Obat": "Obat Demam", "Kemasan": "Tablet", "Isi": "4 Tablet" },
        {"nama": "Paramex", "Jenis Obat": "Obat sakit Kepala", "Kemasan": "Tablet", "Isi": "8 Tablet" },
        {"nama": "Polysilane", "Jenis Obat": "Obat Magh", "Kemasan": "Botol", "Isi": "100 ml" },
        {"nama": "Aspirin", "Jenis Obat": "Obat Sakit Kepala", "Kemasan": "Tablet", "Isi": "8 Tablet" },
        {"nama": "Betadine", "Jenis Obat": "Obat Luka", "Kemasan": "Botol", "Isi": "30 ml" },
        {"nama": "Amoxicillin", "Jenis Obat": "Antibiotik", "Kemasan": "Tablet", "Isi": "12 Tablet" },
        {"nama": "Tretinoin", "Jenis Obat": "Obat Kulit", "Kemasan": "Tube", "Isi": "15 gram" },
    ]
    
    def informasiObat(pencarianObat):
        printTitle()
        print(f"Nama Obat: {pencarianObat['nama']}")
        print(f"Jenis Obat: {pencarianObat['Jenis Obat']}")
        print(f"Kemasan: {pencarianObat['Kemasan']}")
        print(f"Isi: {pencarianObat['Isi']}")
        
        print()
        
        while True:
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                inputanInvalid()

    def cariObat(nama):
        for i in list_obat:
            if i["nama"].lower() == nama.lower():
                return i
        return None

    while True:
        printTitle()
        printMenu("bisolvon", "flutamol", "sanmol", "paramex", "polysilane", "aspirin", "betadine", "amoxicillin", "tretinoin", "kembali ke manu utama")
        print()
        print("[11] Search")
        print()
        
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            hasil = cariObat("Bisolvon")
            
            informasiObat(hasil)
        elif pilihan_user == "2":
            hasil = cariObat("Flutamol")
            
            informasiObat(hasil)
        elif pilihan_user == "3":
            hasil = cariObat("Sanmol")
            
            informasiObat(hasil)
        elif pilihan_user == "4":
            hasil = cariObat("Paramex")
            
            informasiObat(hasil)
        elif pilihan_user == "5":
            hasil = cariObat("Polysilane")
            
            informasiObat(hasil)
        elif pilihan_user == "6":
            hasil = cariObat("Aspirin")
            
            informasiObat(hasil)
        elif pilihan_user == "7":
            hasil = cariObat("Betadine")
            
            informasiObat(hasil)
        elif pilihan_user == "8":
            hasil = cariObat("Amoxicillin")
            
            informasiObat(hasil)
        elif pilihan_user == "9":
            hasil = cariObat("Tretinoin")
            
            informasiObat(hasil)
        elif pilihan_user == "10":
            break
        elif pilihan_user == "11":
            while True:
                printTitle()
                nama_obat = input("Masukkan nama barang yang ingin dicari: ")
                hasil = cariObat(nama_obat)
                
                if hasil != None:
                    informasiObat(hasil)
                    break
                elif len(nama_obat) < 1:
                    print(f"{Fore.RED}Nama obat tidak boleh kosong")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                else:
                    print(f"{Fore.RED}Obat tidak ditemukan")
                    print(Style.RESET_ALL)
                    time.sleep(1)
        else:
            inputanInvalid()
            
def menuKegiatan():
    def donorDarahPage():
        printTitle()
        print(f"{Style.BRIGHT}{Fore.BLUE}\nDonor Darah: Sumbangkan Kebaikan, Sumbangkan Hidup")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Donor Darah kami! Di sini, kami membangun jembatan 
kebaikan antara kamu dan kesempatan untuk menyelamatkan nyawa. Donor darah 
adalah tindakan luar biasa yang memiliki dampak luar biasa pula.

Mengapa Donor Darah Penting?

Setiap detik, seseorang di luar sana membutuhkan bantuan darah 
untuk mempertahankan hidup. Dengan setiap donasi yang kamu berikan, 
kamu menjadi pahlawan bagi orang-orang yang sedang berjuang. 
Donor darah tidak hanya menyelamatkan nyawa, tetapi juga memberikan 
harapan bagi mereka yang memerlukan perawatan medis mendesak.

Bagaimana Proses Donor Darah?

Proses donor darah sederhana dan aman. Kami memiliki tim profesional 
yang siap membantu selama seluruh proses. Setelah pendaftaran dan pemeriksaan 
sederhana, kamu akan memberikan sumbangan darahmu. Satu tindakan kecil dari 
kamu bisa memiliki dampak besar dalam kehidupan orang lain.

Manfaat bagi Kesehatan

Selain membantu orang lain, donor darah juga memiliki manfaat bagi kesehatanmu 
sendiri. Ini adalah kesempatan untuk membersihkan dan meregenerasi sel-sel 
darahmu yang baru. Selain itu, proses ini dapat membantu mengurangi risiko 
penyakit tertentu dan meningkatkan kesehatan jantung.

Bergabunglah dalam Gerakan Kebaikan

Kami mengundangmu untuk bergabung dalam gerakan kebaikan ini. 
Informasi mengenai lokasi donor darah terdekat, jadwal acara, dan 
cara bergabung dengan komunitas kami dapat kamu temukan di sini.""")
        while True:
            print()
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                inputanInvalid()

    def vaksinasiPage():
        printTitle()
        print(f"{Style.BRIGHT}{Fore.BLUE}\nVaksinasi: Langkah Proaktif untuk Kesehatan dan Perlindungan")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Vaksinasi kami! Di sini, kami menekankan pentingnya 
langkah proaktif dalam melindungi diri dan komunitas melalui vaksinasi.

Perlunya Vaksinasi

Vaksinasi adalah salah satu langkah terpenting dalam menjaga kesehatan kita. 
Ini bukan hanya tentang melindungi diri sendiri, tetapi juga tentang menjaga 
kesehatan orang-orang di sekitar kita. Vaksinasi membantu mencegah penyebaran 
penyakit dan mengurangi risiko komplikasi yang serius.

Manfaat Vaksinasi

Dapatkan informasi lengkap mengenai manfaat vaksinasi. Selain memberikan perlindungan 
diri dari penyakit tertentu, vaksinasi juga berperan dalam mengendalikan wabah penyakit, 
melindungi yang rentan, dan menciptakan kekebalan komunitas yang lebih luas.

Mitos dan Fakta

Dapatkan jawaban atas pertanyaan umum dan temukan fakta-fakta yang jelas mengenai 
vaksinasi. Kami hadir untuk memberikan informasi yang akurat dan terpercaya guna 
membantu menjawab keraguan atau pertanyaan yang mungkin kamu miliki tentang vaksinasi.

Bergabunglah dalam Perlindungan Bersama

Vaksinasi adalah langkah kecil dengan dampak besar. Mari bersama-sama menjadi bagian 
dari gerakan perlindungan dan kesehatan bersama. Dengan vaksinasi, kita membuka jalan 
menuju masa depan yang lebih sehat dan aman bagi kita semua.""")
        while True:
            print()
            print("[1] kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                inputanInvalid()
    
    def senamBersamaPage():
        printTitle()
        print(f"{Style.BRIGHT}{Fore.BLUE}\nSenam Bersama: Langkah Menuju Kesehatan dan Kebahagiaan")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Senam Bersama kami! 
Di sini, kami mengajakmu untuk menemukan kebugaran, energi, 
dan keceriaan melalui sesi senam yang menyenangkan.

Mengapa Senam?

Senam bukan hanya tentang gerakan tubuh, tetapi juga tentang menjaga kesehatan dan kebugaran. 
Aktivitas fisik yang teratur membawa banyak manfaat bagi tubuh dan pikiran. Bersama-sama, 
kita bisa merasakan peningkatan energi, kekuatan, dan semangat yang positif.

Jenis Senam yang Ditawarkan

Temukan berbagai jenis senam yang ditawarkan di komunitas kami. Dari senam aerobik yang 
mengasyikkan hingga yoga yang menenangkan, ada sesi untuk setiap preferensi dan tingkat 
kebugaran. Jangan lewatkan kesempatan untuk merasakan beragam pengalaman senam yang bermanfaat.

Jadwal Sesi Senam

Cek jadwal lengkap dari sesi senam kami. Kami menyediakan waktu yang fleksibel untuk 
memastikan setiap orang dapat bergabung. Sesi-sesi ini tidak hanya tentang gerakan fisik, 
tetapi juga tentang menciptakan ikatan komunitas yang solid.

Manfaat Senam Teratur

Dapatkan informasi lengkap mengenai manfaat dari rutinitas senam secara teratur. Ini bukan 
hanya tentang kebugaran fisik, tetapi juga tentang kesehatan mental, peningkatan fokus, 
dan penurunan tingkat stres.

Bergabunglah dengan Komunitas Senam Kami

Ayo, jadikan setiap langkahmu sebagai langkah menuju kesehatan yang lebih baik bersama 
komunitas senam kami. Bergabunglah dengan kami dan rasakan kebahagiaan dalam setiap gerakan!
              """)
        while True:
            print()
            print("[1] kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                inputanInvalid()
    
    list_kegiatan = [
        {"nama_kegiatan": "Donor Darah", 
         "deskripsi_kegiatan": """
    Kami hadir untuk mengajakmu menjadi bagian dari gerakan kebaikan melalui donor darah. 
    Dengan satu tindakan sederhana, kamu bisa menjadi pahlawan bagi mereka yang membutuhkan. 
    Di sini, temukan informasi lengkap tentang proses donor darah, manfaat bagi kesehatan, 
    serta jadwal lokasi dan waktu donor darah kami. Bergabunglah dengan komunitas kami untuk 
    emberikan harapan dan kehidupan kepada mereka yang membutuhkan. Jadilah bagian dari perubahan positif 
    dengan menyumbangkan satu tetes darah untuk kebaikan bersama.
         """},
        {"nama_kegiatan": "Vaksinasi",
         "deskripsi_kegiatan": """
    Jangan lewatkan kesempatan untuk melindungi diri dan orang-orang di sekitarmu! Halaman vaksinasi 
    kami adalah pintu menuju perlindungan dan keamanan. Temukan informasi tentang vaksin yang tersedia, 
    jadwal lokasi vaksinasi, dan pentingnya mendapatkan vaksin. Satu langkah kecil ini bisa menjadi langkah 
    besar untuk kesehatan dan keselamatan kita bersama. Ayo, bergabunglah dalam langkah proaktif melindungi 
    diri dari penyakit dengan vaksinasi.
         """},
        {"nama_kegiatan": "Senam Bersama",
         "deskripsi_kegiatan": """
    Rasakan energi, kebugaran, dan keceriaan dalam setiap gerakan! Halaman senam bersama kami adalah tempat 
    di mana kamu bisa bergabung dalam sesi senam yang menyenangkan dan bermanfaat. Dapatkan informasi tentang 
    jadwal, jenis senam yang ditawarkan, dan manfaat dari rutinitas senam secara teratur. Ayo, jadikan setiap 
    langkahmu sebagai langkah menuju kesehatan dan kebugaran yang lebih baik bersama komunitas senam kami!
         """}]
        

    for i, kegiatan in enumerate(list_kegiatan):
        print(f"""
{i+1}. Kegiatan {i+1}
   ---------------
    {kegiatan["nama_kegiatan"]}

    {kegiatan["deskripsi_kegiatan"]}
    """)
    
    while True:
        printTitle()
        printMenu("donor darah", "vaksinasi", "senam bersama", "kembali ke menu sebelumnya")
        print()
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            donorDarahPage()
        elif pilihan_user == "2":
            vaksinasiPage()
        elif pilihan_user == "3":
            senamBersamaPage()
        elif pilihan_user == "4":
            break
        else:
            inputanInvalid()
            
def menuProfile():
    global data_pengguna
    global pengguna_saat_ini
    
    def editProfile():
        global pengguna_saat_ini
        for i, pengguna in enumerate(data_pengguna):
            if pengguna["nama"] == pengguna_saat_ini["nama"]:
                printTitle()
                print(f"{Style.BRIGHT}{Fore.BLUE}\nEdit Profile")
                print(Style.RESET_ALL)
                
                nama_baru = input("Nama: ")
                while len(nama_baru) < 1:
                    print(f"{Fore.RED}Tidak boleh kosong")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    printTitle()
                    nama_baru = input("Nama: ")  
                    
                password_baru = input("Password: ")
                while len(password_baru) < 8:
                    print(f"{Fore.RED}Password harus memiliki minimal 8 karakter")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    printTitle()
                    print(f"Nama: {nama_baru}")
                    password_baru = input("Password: ")
                    
                kelamin_baru = input("Kelamin: ")
                while len(kelamin_baru) < 1:
                    print(f"{Fore.RED}Tidak boleh kosong")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    printTitle()
                    print(f"Nama: {nama_baru}")
                    print(f"Password: {password_baru}")
                    kelamin_baru = input("Kelamin: ")
                    
                alamat_baru = input("Alamat: ")
                while len(alamat_baru) < 1:
                    print(f"{Fore.RED}Tidak boleh kosong")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    printTitle()
                    print(f"Nama: {nama_baru}")
                    print(f"Password: {password_baru}")
                    print(f"Kelamin: {kelamin_baru}")
                    alamat_baru = input("Alamat: ")
                    
                nomor_hp_baru = input("Nomor HP: ")
                while len(nomor_hp_baru) < 1:
                    print(f"{Fore.RED}Tidak boleh kosong")
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    printTitle()
                    print(f"Nama: {nama_baru}")
                    print(f"Password: {password_baru}")
                    print(f"Kelamin: {kelamin_baru}")
                    print(f"Alamat: {alamat_baru}")
                    nomor_hp_baru = input("Nomor HP: ")
                    
                riwayat_penyakit_baru = input("Riwayat Penyakit (jika tidak ada - saja): ")
                while len(riwayat_penyakit_baru) < 1:
                    print(f'{Fore.RED}isi dengan strip "-" bila tidak ada')
                    print(Style.RESET_ALL)
                    time.sleep(2)
                    printTitle()
                    print(f"Nama: {nama_baru}")
                    print(f"Password: {password_baru}")
                    print(f"Kelamin: {kelamin_baru}")
                    print(f"Alamat: {alamat_baru}")
                    print(f"Nomor HP: {nomor_hp_baru}")
                    riwayat_penyakit_baru = input("Riwayat Penyakit (jika tidak ada - saja): ")
                    
                print()
                data_pengguna[i] = {
                    "nama": nama_baru, 
                    "password": password_baru, 
                    "kelamin": kelamin_baru, 
                    "alamat": alamat_baru, 
                    "nomor_hp": nomor_hp_baru, 
                    "riwayat_penyakit": riwayat_penyakit_baru}
                
                pengguna_saat_ini = {
                    "nama": nama_baru, 
                    "password": password_baru, 
                    "kelamin": kelamin_baru, 
                    "alamat": alamat_baru, 
                    "nomor_hp": nomor_hp_baru, 
                    "riwayat_penyakit": riwayat_penyakit_baru}
                
                print(f"{Fore.GREEN}Biodata Pengguna Berhasil Di Update.")
                print(Style.RESET_ALL)
                time.sleep(1)
                printTitle
                break
                
    while True:            
        global pengguna_saat_ini
        printTitle()
        print(f"{Style.BRIGHT}{Fore.BLUE}\nProfile")
        print()
        print(f"""{Style.RESET_ALL}
Nama: {pengguna_saat_ini["nama"]}
Kelamin: {pengguna_saat_ini["kelamin"]}
Alamat: {pengguna_saat_ini["alamat"]}
Nomor HP: {pengguna_saat_ini["nomor_hp"]}
Riwayat Penyakit: {pengguna_saat_ini["riwayat_penyakit"]}""")
        print()
        printMenu("edit profile", "kembali ke manu sebelumnya")
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            editProfile()
        elif pilihan_user == "2":
            break
        else:
            inputanInvalid()

def menuUtama():
    global status_login
    global pengguna_saat_ini
    while True:
        printTitle()
        printMenu("obat", "kegiatan", "profile", "tentang kami", "logout")
        print()
        
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            menuObat()
        elif pilihan_user == "2":
            menuKegiatan()
        elif pilihan_user == "3":
            menuProfile()
        # elif pilihan_user == "5":
        #     menuTentangKami()
        elif pilihan_user == "5":
            status_login = False
            pengguna_saat_ini = None
            return status_login
        else:
            inputanInvalid()

        
while True:
    if not status_login:
        os.system("cls")
        welcomePage()
    else:
        os.system("cls")
        menuUtama()




# while True:
#     if not status_login:
#         welcomePage()
#     else:
#         print("Selamat datang")
#         print()
#         while True:
#             print("1. Logout")
#             print("2. Exit")
#             print()
#             pilihan_user = input("> ")
#             if pilihan_user == "1":
#                 status_login = False
#                 break
#             elif pilihan_user == "2":
#                 break
#             else:
#                 print("Inputan tidak valid")
