"""Anda sedang berkemah bersama teman-teman Anda jauh dari rumah, 
tetapi ketika tiba waktunya untuk kembali, Anda menyadari bahwa bahan bakar Anda hampir habis dan pompa terdekat 
berjarak 50 mil! Anda tahu bahwa rata-rata, kecepatan mobil Anda sekitar 25 mil per galon. Tinggal 2 galon lagi.
Dengan mempertimbangkan faktor-faktor ini, tuliskan fungsi yang memberitahukan Anda apakah pompa dapat dijangkau atau tidak.
Fungsi harus mengembalikan nilai true jika memungkinkan dan false jika tidak."""

def apakah_dapat_mencapai_pompa(bahan_bakar_tersisa, rata_rata_mpg, jarak_ke_pompa):
    jarak_maksimum = bahan_bakar_tersisa * rata_rata_mpg
    return jarak_maksimum >= jarak_ke_pompa

bahan_bakar_tersisa = 2 
rata_rata_mpg = 25  
jarak_ke_pompa = 50  

hasil = apakah_dapat_mencapai_pompa(bahan_bakar_tersisa, rata_rata_mpg, jarak_ke_pompa)
if hasil:
    print("Anda dapat mencapai pompa bahan bakar terdekat.")
else:
    print("Anda tidak dapat mencapai pompa bahan bakar terdekat.")
