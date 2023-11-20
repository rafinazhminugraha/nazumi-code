"""
Nama : Rafi Nazhmi Nugraha - 2301303
Kelas : RPL 1A
"""

import numpy as np

def nilai_mtk(n):
    mengurutkan = np.sort(n)[::-1]
    lima_nilai_terbesar = mengurutkan[0:5]
    return [f'{nilai:,}' for nilai in lima_nilai_terbesar]

nilai_matematika = np.random.randint(0,100,30)

print(f"""
Daftar nilai matematika: {nilai_matematika}
5 nilai terbesar: {nilai_mtk(nilai_matematika)}
      """)