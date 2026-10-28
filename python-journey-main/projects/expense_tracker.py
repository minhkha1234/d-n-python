"""
Ứng dụng quản lý chi tiêu cá nhân bằng Python.
Dùng thư viện chuẩn, lưu dữ liệu trong expenses.json cùng thư mục.

Chạy:
    python expense_tracker.py
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Không đọc được expenses.json. Bắt đầu với danh sách trống.")
        return []


def save_expenses(expenses):
    DATA_FILE.write_text(
        json.dumps(expenses, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def money(amount):
    return f"{amount:,.0f} VND"


def show_expenses(expenses):
    if not expenses:
        print("\nChưa có khoản chi nào.")
        return

    print("\n===== LỊCH SỬ CHI TIÊU =====")
    for item in expenses:
        print(
            f'#{item["id"]} | {item["date"]} | {item["category"]} | '
            f'{money(item["amount"])} | {item["note"]}'
        )


def add_expense(expenses):
    try:
        amount = float(input("Số tiền đã chi (VND): ").replace(",", "").strip())
        if amount <= 0:
            print("Số tiền phải lớn hơn 0.")
            return
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ.")
        return

    category = input("Danh mục (ăn uống/đi lại/học tập/khác): ").strip()
    note = input("Ghi chú: ").strip()
    next_id = max((item["id"] for item in expenses), default=0) + 1
    expenses.append({
        "id": next_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category or "Khác",
        "note": note or "Không có ghi chú",
    })
    save_expenses(expenses)
    print("Đã lưu khoản chi.")


def show_summary(expenses):
    total = sum(item["amount"] for item in expenses)
    print("\n===== TỔNG KẾT CHI TIÊU =====")
    print(f"Tổng số khoản chi: {len(expenses)}")
    print(f"Tổng tiền đã chi: {money(total)}")
    if expenses:
        print("\nTheo danh mục:")
        categories = {}
        for item in expenses:
            categories[item["category"]] = categories.get(item["category"], 0) + item["amount"]
        for category, amount in sorted(categories.items()):
            print(f"- {category}: {money(amount)}")


def main():
    expenses = load_expenses()
    while True:
        print("\n===== QUẢN LÝ CHI TIÊU CÁ NHÂN =====")
        print("1. Xem lịch sử chi tiêu")
        print("2. Thêm khoản chi")
        print("3. Xem tổng kết chi tiêu")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            show_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn 0, 1, 2 hoặc 3.")


if __name__ == "__main__":
    main()
