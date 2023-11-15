total_belanjaan = int(input("berapa total belanjaan anda: Rp."))

if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.1
    total_belanjaan_akhir = total_belanjaan - diskon
    print(f"""
          anda berhak mendapatkan diskon sebesar 10%
          dan total belanjaan yang harus anda bayar adalah: {total_belanjaan_akhir}
          """)
else:
    print(f"""
          maaf anda tidak berhak mendapatkan diskon
          dan total belanjaan yang harus anda bayar adalah: {total_belanjaan}
          """)