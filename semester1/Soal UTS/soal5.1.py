list_bilangan_baru = ""
list_bilangan_sebelumnya = ""
bilangan_dijumlahkan = []
kesempatan_input = 3

while kesempatan_input != 0:
    bilangan = input("Input bilangan : ")
    list_bilangan_baru += bilangan
    list_bilangan_sebelumnya += bilangan
    
    if list_bilangan_baru > list_bilangan_sebelumnya:
        bilangan_dijumlahkan.append(bilangan)
        list_bilangan_sebelumnya -= bilangan
    elif list_bilangan_baru < list_bilangan_sebelumnya:
        kesempatan_input -= 1

total = sum(bilangan_dijumlahkan)
print(f"hasil penjumlahan nilai yang membesar : {total}")
    
