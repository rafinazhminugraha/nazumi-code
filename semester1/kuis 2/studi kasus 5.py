menu = ["ayam Gulai", "babat", "cumi", "ckan Kembung", "kikil", "limpa", "otak", "paru", "rendang", "telur", "usus"]

def cariMenu(array, menu_yang_dicari):
    for i in range (len(array)):
        if array[i] == menu_yang_dicari:
            return 1
    return -1
        
print("\nRestoran Padang")

print("""
Menu:
● Ayam Gulai
● Babat
● Cumi
● Ikan Kembung
● Kikil
● Limpa
● Otak
● Paru
● Rendang
● Telur
● Usus
""")

menu_yang_dicari = input("Cek menu : ").lower()

hasil_pencarian = cariMenu(menu, menu_yang_dicari)

if hasil_pencarian == 1:
    print(f"{menu_yang_dicari} tersedia di dalam menu")
else:
    print(f"{menu_yang_dicari} tidak tersedia di dalam menu")