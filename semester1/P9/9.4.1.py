# def hitung_selisih_waktu(start_hour, start_minute, start_second, end_hour, end_minute, end_second):
#     total_start_seconds = start_hour * 3600 + start_minute * 60 + start_second
#     total_end_seconds = end_hour * 3600 + end_minute * 60 + end_second

#     selisih_seconds = total_end_seconds - total_start_seconds

#     jam = selisih_seconds // 3600
#     sisa_detik = selisih_seconds % 3600
#     menit = sisa_detik // 60
#     detik = sisa_detik % 60

#     return jam, menit, detik


# start_hour = 8
# start_minute = 10
# start_second = 20

# end_hour = 9
# end_minute = 15
# end_second = 30

# hasil_selisih = hitung_selisih_waktu(start_hour, start_minute, start_second, end_hour, end_minute, end_second)

# print(f"Selisih waktu: {hasil_selisih[0]} jam - {hasil_selisih[1]} menit - {hasil_selisih[2]} detik")