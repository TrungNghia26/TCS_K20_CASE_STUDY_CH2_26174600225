# 4.1. Nhập các trường dữ liệu
ma_quan_sat = input("Nhập mã quan sát: ")
so_lan_do = int(input("Nhập số lần đo: "))
gia_tri_do = float(input("Nhập giá trị đo (°C): "))
don_vi_do = input("Nhập đơn vị đo: ")
 
# 4.2. Tính giá trị dẫn xuất
gia_tri_f = gia_tri_do * 9 / 5 + 32
 
# In mã quan sát, số lần đo, giá trị C, đơn vị và giá trị F
print()
print("Mã quan sát :", ma_quan_sat)
print("Số lần đo   :", so_lan_do)
print("Giá trị C   :", gia_tri_do)
print("Đơn vị đo   :", don_vi_do)
print("Giá trị F   :", gia_tri_f)
 
# Dùng type() để kiểm tra so_lan_do là int và gia_tri_do là float
print()
print("type(so_lan_do)  :", type(so_lan_do))
print("so_lan_do là int :", type(so_lan_do) is int)
print("type(gia_tri_do) :", type(gia_tri_do))
print("gia_tri_do là float:", type(gia_tri_do) is float)
 
# Chuyển so_lan_do sang str, in giá trị và kiểm tra kiểu
so_lan_do_text = str(so_lan_do)
print()
print("so_lan_do_text   :", so_lan_do_text)
print("type(so_lan_do_text):", type(so_lan_do_text))
print("so_lan_do_text là str:", type(so_lan_do_text) is str)
 
