"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

tong = a + b
hieu = a - b
tich = a * b

print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")

if b != 0:
    thuong = a / b
    print(f"Thương: {thuong}")
else:
    print("Thương: Không thể chia cho số 0!")

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input("Nhập bán kính hình tròn (r): "))

pi = 3.14159

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Diện tích hình tròn: {dien_tich}")
print(f"Chu vi hình tròn: {chu_vi}")

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá (%): "))

gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)

print(f"Giá sau khi giảm: {gia_sau_giam:,.0f}")

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

so_tien_usd = so_tien_vnd / ty_gia

print(f"Số USD tương ứng: {so_tien_usd:.2f}")