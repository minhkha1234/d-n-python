"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
ten = "An"
tuoi = 20
diem = 8.567
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")

# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50

for i in range(1, 11):
    ket_qua = 5 * i
    print(f"5 x {i:>2} = {ket_qua:>3}")

# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/phải
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"

print("=" * 29)
print(f"{'SẢN PHẨM':<18}{'GIÁ (VNĐ)':>11}")
print("-" * 29)

print(f"{'Cà phê':<18}{35000:>11,}")
print(f"{'Bánh mì':<18}{25000:>11,}")
print(f"{'Nước suối':<18}{10000:>11,}")

print("-" * 29)
print(f"{'TỔNG CỘNG':<18}{70000:>11,}")
print("=" * 29)

# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%

phan_tram = int(input("Nhập tiến trình (0-100): "))

if phan_tram < 0 or phan_tram > 100:
    print("Vui lòng nhập số trong khoảng từ 0 đến 100!")
else:
    tong_ky_tu = 20
    
    so_ky_tu_day = (phan_tram * tong_ky_tu) // 100
    so_ky_tu_trong = tong_ky_tu - so_ky_tu_day
    
    bar = "█" * so_ky_tu_day + "░" * so_ky_tu_trong
    
    print(f"[{bar}] {phan_tram}%")