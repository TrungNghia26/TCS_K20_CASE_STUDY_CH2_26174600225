tong_phut = 135
cong_suat_w = 250

gio_tron = tong_phut // 60
phut_con_lai = tong_phut % 60
print(gio_tron, phut_con_lai)

su_dung_lau = tong_phut > 60
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print(su_dung_lau)
print(du_lieu_hop_le)

print(100 + 20 * 3)
print((100 + 20) * 3)