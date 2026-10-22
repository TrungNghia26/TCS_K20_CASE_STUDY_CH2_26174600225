from datetime import datetime
#lan 2
#Bai 5.1 Thiết kế dữ liệu nhập
ma_quan_sat = input("Nhap ma quan sat: ")
ten_dai_luong = input("Nhap ten dai luong: ")
gia_tri_do = float(input("Nhap gia tri do: "))
don_vi = input("Nhap don vi: ")

#Bai 5.2 Gắn thời điểm hiện tại
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

#Bai 5.3 Xuất bản ghi bằng f-string
print()
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng   : {ten_dai_luong}")
print(f"Giá trị     : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm   : {thoi_diem_text}")
