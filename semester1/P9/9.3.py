def nilai_total_dan_rerata(*angka):
    total = sum(angka)
    rerata = total / len(angka)
    return total, rerata

nilai = input("masukan nilai (pisahkan dengan koma): ")
nilai = [int(i) for i in nilai.split(",")]


total, rerata = nilai_total_dan_rerata(*nilai)
print(f"total: {total}, rerata: {rerata}")



# nilai = input("masukan nilai (pisahkan dengan koma): ")).split(",")
# for i in range(len(nilai)):
#     nilai[i] = int(nilai[i]   