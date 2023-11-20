jumlah_nyanyian = int(input("Berapa kali lagu ingin dinyanyikan : "))

for nyanyian in range(jumlah_nyanyian, 0, -1):
    anak_ayam_turun = nyanyian
    anak_ayam_mati = nyanyian -1
    
    if nyanyian == 1:
        print(f"""
Anak ayam turunlah {anak_ayam_turun}
Mati satu tinggallah induknya""")
    else:
        print(f"""
Anak ayam turunlah {anak_ayam_turun}
Mati satu tinggallah {anak_ayam_mati}
        """)

# N = int(input("Masukkan jumlah anak ayam: "))

# for i in range(N, 0, -1):
#     print(f"anak ayam turunlah {i}")
#     if i == 1:
#         print("mati satu tinggallah induknya")
#     else:
#         tinggal = i - 1
#         print(f"mati satu tinggallah {tinggal}")
#     print()