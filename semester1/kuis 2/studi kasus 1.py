perpustakaan = []

def tambah_buku():
    buku = {}
    buku['judul'] = input("Masukkan judul buku: ")
    buku['penulis'] = input("Masukkan nama penulis: ")
    buku['kode'] = input("Masukkan kode buku: ")
    buku['status'] = "Tersedia"
    perpustakaan.append(buku)

def pinjam_buku():
    kode = input("Masukkan kode buku yang ingin dipinjam: ")
    for buku in perpustakaan:
        if buku['kode'] == kode:
            if buku['status'] == "Tersedia":
                buku['status'] = "Dipinjam"
                print("Buku berhasil dipinjam.")
                return
            else:
                print("Buku sedang dipinjam.")
                return
    print("Buku tidak ditemukan.")

def kembalikan_buku():
    kode = input("Masukkan kode buku yang ingin dikembalikan: ")
    for buku in perpustakaan:
        if buku['kode'] == kode:
            if buku['status'] == "Dipinjam":
                buku['status'] = "Tersedia"
                print("Buku berhasil dikembalikan.")
                return
            else:
                print("Buku tidak sedang dipinjam.")
                return
    print("Buku tidak ditemukan.")

def lihat_buku():
    ada_buku_tersedia = False
    for i, buku in enumerate(perpustakaan):
        if buku['status'] == "Tersedia":
            print(f"""
BUKU {i + 1}
Judul: {buku['judul']}
Penulis: {buku['penulis']}
Kode: {buku['kode']}
Status: {buku["status"]}""")
            ada_buku_tersedia = True
    if not ada_buku_tersedia:
        print("Tidak ada buku yang tersedia")

def lihat_buku_dipinjam():
    ada_buku_dipinjam = False
    for i, buku in enumerate(perpustakaan):
        if buku['status'] == "Dipinjam":
            print(f"""
BUKU {i + 1}
Judul: {buku['judul']}
Penulis: {buku['penulis']}
Kode: {buku['kode']}
Status: {buku["status"]}""")
            ada_buku_dipinjam = True
    if not ada_buku_dipinjam:
        print("Tidak ada buku yang dipinjam")
            
while True:
    print("\nPERPUSTAKAAN UPI")
    print()
    print("\nMenu:")
    print("1. Tambah buku baru")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Lihat buku tersedia")
    print("5. Lihat buku yang dipinjam")
    print("6. Keluar")
    
    print()
    
    pilihan = input("Masukkan pilihan Anda: ")
    
    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        pinjam_buku()
    elif pilihan == "3":
        kembalikan_buku()
    elif pilihan == "4":
        lihat_buku()
    elif pilihan == "5":
        lihat_buku_dipinjam()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid.")