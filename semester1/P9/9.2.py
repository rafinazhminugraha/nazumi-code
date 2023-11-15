def hitung_vol_tabung(jari_jari, tinggi):
    volume = 3.14 * jari_jari**2 * tinggi   
    return volume

jari_jari = int(input("masukkan jari jari tabung: "))
tinggi = int(input("masukkan tinggi tabung: "))
volume_tabung = int(hitung_vol_tabung(jari_jari, tinggi))

print(f"volume tabung nya adalah {volume_tabung} cm^3")