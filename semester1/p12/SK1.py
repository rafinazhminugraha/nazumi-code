def linearSearch(array, cariNilai):
    for i in range (len(array)):
        if array[i] == cariNilai:
            return i
    return -1

barang = ["asus", "vivo", "samsung", "apple", "xiaomi", "realme", "levis", "adidas", "nike",
         "puma", "gucci", "h&m", "uniqlo", "zara", "burberry"]

nilai = "burberry"
hasil = linearSearch(barang, nilai)

if nilai != -1:
    print(f"barang {nilai} tersedia di katalog barang no {hasil}")
else:
    print(f"barang {nilai} tidak tersedia di katalog barang")