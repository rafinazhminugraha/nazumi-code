def hitung_volume_tabung(radius, tinggi):
    volume = 3.14 * radius**2 * tinggi
    return volume

radius_tabung = 5
tinggi_tabung = 10
volume_tabung = hitung_volume_tabung(radius_tabung, tinggi_tabung)
print(f"Volume tabung dengan radius {radius_tabung} dan tinggi {tinggi_tabung}: {volume_tabung:.2f}")
