import csv

def updateStokBarang(nama_file, nama_item, perubahan_stok):
    with open(nama_file, "r") as file:
        baca_file = csv.reader(file)
        list_barang = list(baca_file)
        
    for i in list_barang:
        if len(i) > 1 and i[0] == nama_item:
            i[1] = str(int(i[1]) + perubahan_stok)
            
    with open(nama_file, "w", newline="") as file:
        perbarui = csv.writer(file) 
        perbarui.writerows(list_barang)
    
    print(f"Stok barang {nama_item} berhasil di perbarui. silahkan di cek di dalam file\n")
    
def tampilanStokBarang(nama_file):
    with open(nama_file, "r") as file:
        baca_file = csv.reader(file)
        print("Daftar barang dan stok")
        for baris in baca_file:
            print(f"{baris[0]} = {baris[1]} pcs")

while True:     
    print("\nUpdate Stok Barang menu\n")
    print("1. Tambah stok barang")
    print("2. Kurang stok barang")
    print("3. Tampilkan list dan stok barang")
    print("4. Keluar\n")

    pilihan = input("> ")
    if pilihan == "1":
        nama_item = input("Masukkan nama item: ")
        perubahan_stok = int(input("Banyak stok ditambah: "))
        updateStokBarang("inventaris_barang.csv", nama_item, perubahan_stok)
    elif pilihan == "2":
        nama_item = input("Masukkan nama item: ")
        perubahan_stok = int(input("Banyak stok berkurang: "))
        updateStokBarang("inventaris_barang.csv", nama_item, -perubahan_stok)
    elif pilihan == "3":
        tampilanStokBarang("inventaris_barang.csv")
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid")
        
"""note = maaf... Tolong jangan lupa pake 'Run Without Debugging (CTRL + F5)' 
karna takut ada kesalahan path directory perbedaan device, Terimakasih"""