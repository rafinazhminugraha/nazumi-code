weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    converted = weight * 0.45
    print(f"You are {converted} Kg")