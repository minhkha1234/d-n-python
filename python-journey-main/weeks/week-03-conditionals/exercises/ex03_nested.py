"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp

so_du = float(input("Nhập số dư hiện tại của bạn: "))
tien_rut = float(input("Nhập số tiền bạn muốn rút: "))

if tien_rut <= 0:
    print("Giao dịch thất bại: Số tiền rút phải lớn hơn 0đ!")
elif tien_rut > so_du:
    print("Giao dịch thất bại: Số dư tài khoản không đủ!")
elif tien_rut % 50000 != 0:
    print("Giao dịch thất bại: Số tiền rút phải là bội số của 50,000đ!")
else:
    so_du_moi = so_du - tien_rut
    print(f"Giao dịch thành công! Bạn đã rút: {tien_rut:,.0f}đ.")
    print(f"Số dư còn lại của bạn là: {so_du_moi:,.0f}đ.")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

if bmi < 18.5:
    print("Xếp loại: Thiếu cân. Bạn nên bổ sung dinh dưỡng và tập luyện để tăng cân nhé!")
elif bmi <= 24.9:
    print("Xếp loại: Bình thường. Tuyệt vời! Hãy tiếp tục duy trì vóc dáng và lối sống lành mạnh này.")
elif bmi <= 29.9:
    print("Xếp loại: Thừa cân. Cảnh báo nhẹ: Bạn nên chú ý hơn đến chế độ ăn uống và chăm vận động nhé.")
else:
    print("Xếp loại: Béo phì. Khuyến nghị: Bạn nên gặp bác sĩ hoặc chuyên gia dinh dưỡng để được tư vấn lộ trình giảm cân an toàn.")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Nhập loại vé (thuong/vip): ").strip().lower()
ngay = input("Nhập ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi của bạn: "))

if loai_ve == "vip":
    gia_ve = 120000
else:
    gia_ve = 80000

if ngay == "cuoi_tuan":
    gia_ve *= 1.3

if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5  # Giảm 50%
elif 18 <= tuoi <= 25:
    gia_ve *= 0.8  # Giảm 20%

print(f"Giá vé cuối cùng là: {gia_ve:,.0f}đ.")