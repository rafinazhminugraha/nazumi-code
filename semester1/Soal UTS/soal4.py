nim = int(input("input 3 digit NIM terakhir : "))

if nim > 0 and nim < 51:
    if nim % 2 == 0:
        print("Silakan masuk ke ke kelash k2")
    else:
        print("Silakan masuk ke ke kelash k1")
elif nim > 50 and nim < 101:
    if nim % 2 == 0:
        print("Silakan masuk ke ke kelash k4")
    else:
        print("Silakan masuk ke ke kelash k3")
elif nim > 100 and nim < 151:
    if nim % 2 == 0:
        print("Silakan masuk ke ke kelash k6")
    else:
        print("Silakan masuk ke ke kelash k5")
elif nim > 150:
    if nim % 2 == 0:
        print("Silakan masuk ke ke kelash k8")
    else:
        print("Silakan masuk ke ke kelash k7")