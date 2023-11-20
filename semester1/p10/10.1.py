"""
Nama : Rafi Nazhmi Nugraha - 2301303
Kelas : RPL 1A
"""

import numpy as np
def convert(n):
    converter = (n * 9/5) + 32
    return [f'{nilai:,}' for nilai in converter]

suhu = np.random.randint(20, 35, 10)

print(f"""
suhu celcius = {suhu}
suhu fahrenheit = {convert(suhu)}
      """)