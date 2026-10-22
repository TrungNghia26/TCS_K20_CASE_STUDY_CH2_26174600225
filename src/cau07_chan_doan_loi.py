ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
# Lỗi 1: TypeError ở dòng 5, do cong_suat_w là str (quên float()), không nhân/chia được với số.
# Lỗi 2: NameError ở dòng 7, do f-string dùng sai tên biến dien_nang thay vì dien_nang_kwh.