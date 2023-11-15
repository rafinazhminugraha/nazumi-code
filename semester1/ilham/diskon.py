belanjaan = int(input("berapa total belanjaan anda: Rp."))

if belanjaan > 500000:
    diskon = belanjaan * 0.1
    total_belanjaan_akhir = belanjaan - diskon
    print(f"""
          diskon 10%
          total belanjaan adalah {total_belanjaan_akhir}
          """)
else:
    print(f"""
          maaf tidak ada diskon
          total belanjaan adalah {belanjaan}
          """)