print("Welcome")

var = (input("please enter your name : "))
var1 = int(input("when you were born : "))

umur = 2023 - var1

print(f"Selamat datang {var} umur anda sekarang adalah {umur} tahun")

# tipe data sequence
x = ("apel", "jeruk", "ceri", "durian", "apel")
print(type(x))

# tipe data list
x = ("apel", "jeruk", "ceri", "durian", "apel")
print(len(x)) # melihat jumlah item dalam list

print(x[2]) # mengambil item terntentu

print(x[1:4]) # mengambil item dnegan range tertentu

x.append("sirsak") # menambah item di akhir list
print(x)

x[2] = "manggis" #mengganti indeks tertentu pada list
print(x)

x.insert(3,"semangka") # menambah item di ramge terntentu
print(x)

x.pop[3] # menghapus 
print (x)

x.sort() # mengurutkan
print(x)

# tipe data tuple (kurang lebih sama seperti list, tetapi tidak bisa di ubah dll)
# bisa di manipulasi dengan cara ubah dlu menajdi list
# packing data
x = ("apel", "belimbing", "ceri", "durian")

(a, b, c, d) = x
print (a)
print (b)
print (c)
print (d)




