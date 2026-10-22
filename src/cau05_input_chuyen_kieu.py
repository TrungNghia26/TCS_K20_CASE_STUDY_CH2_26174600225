ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = input("Nhập số phút: ")
don_gia_kwh = input("Nhập đơn giá điện/kWh: ")

print(type(ma_may), type(cong_suat_w), type(so_phut), type(don_gia_kwh))

cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(dien_nang_kwh)
print(chi_phi)