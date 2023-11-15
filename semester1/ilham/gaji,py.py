performa = str(input("performa pekerja: "))
gaji = int(input("gaji pekerja: "))

if performa == "sangat baik":
    bonus = gaji * 0.2
    print(f"bonus untuk pekerja adalah {bonus}")
elif performa == "cukup":
    bonus = gaji * 0.1
    print(f"bonus untuk pekerja adalah {bonus}")
else:
    bonus = gaji * 0.05
    print(f"bonus untuk pekerja adalah {bonus}")