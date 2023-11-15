performa = str(input("performa sang pekerja: "))
gaji = int(input("gaji sang pekerja: "))

if performa == "sangat baik":
    bonus = gaji * 0.2
    print(f"bonus yang anda terima adalah Rp.{bonus}")
elif performa == "cukup":
    bonus = gaji * 0.1
    print(f"bonus yang anda terima adalah Rp.{bonus}")
else:
    bonus = gaji * 0.05
    print(f"bonus yang anda terima adalah Rp.{bonus}")