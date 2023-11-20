# def selisih():
def selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    selisih_jam = jam_selesai - jam_mulai
    selisih_menit = menit_selesai - menit_mulai
    selisih_detik = detik_selesai - detik_mulai
    
    if selisih_jam < 0:
        selisih_jam += 24
    if selisih_menit < 0:
        selisih_menit += 60
        selisih_jam -= 1
    if selisih_detik < 0:
        selisih_detik += 60
        selisih_menit -= 1
        
    print(f"{selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")
    

print("Input Mulai:")
jam_mulai = int(input("jam: "))
menit_mulai = int(input("Menit: "))
detik_mulai = int(input("detik: "))
print("                               ")
print("Input Selesai:")
jam_selesai = int(input("jam: "))
menit_selesai = int(input("Menit: "))
detik_selesai = int(input("detik: "))

selisih(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)