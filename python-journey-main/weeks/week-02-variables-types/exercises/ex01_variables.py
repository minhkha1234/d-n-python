"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
ten = "kha"
tuoi = 19
diem_tb = 8.5
dang_hoc = True

print("Tên:", ten, "-", type(ten))
print("Tuổi:", tuoi, "-", type(tuoi))
print("Điểm trung bình:", diem_tb, "-", type(diem_tb))
print("Đang học:", dang_hoc, "-", type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20

a, b = b, a

print(f"Sau hoán đổi: a = {a}, b = {b}")

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
print(f"Giá trị ban đầu: x = {x}")

x += 50
print(f"Bước 1 (+=): x = {x}")

x -= 30
print(f"Bước 2 (-=): x = {x}")

x *= 2
print(f"Bước 3 (*=): x = {x}")

x //= 5
print(f"Bước 4 (//=): x = {x}")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "Nguyễn", "Văn Minh", 18

print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")