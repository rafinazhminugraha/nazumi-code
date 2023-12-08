from colorama import init, Style
init()
def menuKegiatan():
    def donorDarahPage():
        print(f"{Style.BRIGHT}\nDonor Darah: Sumbangkan Kebaikan, Sumbangkan Hidup")
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
                print("Inputan tidak valid")

    def vaksinasiPage():
        print(f"{Style.BRIGHT}\nVaksinasi: Langkah Proaktif untuk Kesehatan dan Perlindungan")
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
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print("Inputan tidak valid")
    
    def senamBersamaPage():
        print(f"{Style.BRIGHT}\nSenam Bersama: Langkah Menuju Kesehatan dan Kebahagiaan")
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
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print("Inputan tidak valid")
    
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
        print("\nKegiatan UPS")
        print()
        print("1. Donor Darah")
        print("2. Vaksinasi")
        print("3. Senam Bersama")
        print("4. kembali ke menu sebelumnya")
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
            print("Inputan tidak valid")

menuKegiatan()