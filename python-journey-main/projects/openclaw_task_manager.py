"""
Ứng dụng quản lý chi tiêu cá nhân bằng Python.

Chức năng:
- Xem lịch sử chi tiêu.
- Thêm khoản chi mới.
- Xem tổng số tiền đã chi tiêu và tổng tiền theo từng danh mục.
- Lưu dữ liệu trong expenses.json cạnh file này.

Cách chạy:
    python openclaw_task_manager.py
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    """Đọc dữ liệu chi tiêu từ file JSON."""
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Không đọc được expenses.json. Bắt đầu với danh sách trống.")
        return []


def save_expenses(expenses):
    """Lưu dữ liệu chi tiêu vào file JSON."""
    DATA_FILE.write_text(
        json.dumps(expenses, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def format_money(amount):
    """Định dạng số tiền theo đơn vị VND."""
    return f"{amount:,.0f} VND"


def show_expenses(expenses):
    """Hiển thị lịch sử các khoản chi."""
    print("\n===== LỊCH SỬ CHI TIÊU =====")
    if not expenses:
        print("Chưa có khoản chi nào.")
        return

    for item in expenses:
        print(
            f'#{item["id"]} | {item["date"]} | {item["category"]} | '
            f'{format_money(item["amount"])}'
        )
        print(f'   Ghi chú: {item["note"]}')


def add_expense(expenses):
    """Thêm một khoản chi mới."""
    raw_amount = input("Nhập số tiền đã chi (VND): ").strip().replace(",", "")

    try:
        amount = float(raw_amount)
        if amount <= 0:
            print("Số tiền phải lớn hơn 0.")
            return
    except ValueError:
        print("Số tiền không hợp lệ. Vui lòng nhập một con số.")
        return

    category = input(
        "Danh mục (ví dụ: Ăn uống, Đi lại, Học tập, Giải trí): "
    ).strip()
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
    print("Đã lưu khoản chi thành công.")


def show_summary(expenses):
    """Hiển thị tổng số tiền đã chi và tổng tiền theo từng danh mục."""
    total = sum(float(item["amount"]) for item in expenses)

    print("\n===== TỔNG KẾT CHI TIÊU =====")
    print(f"Số khoản chi: {len(expenses)}")
    print(f"TỔNG SỐ TIỀN ĐÃ CHI TIÊU: {format_money(total)}")

    if not expenses:
        print("Chưa có khoản chi nào để thống kê theo danh mục.")
        return

    category_totals = {}
    for item in expenses:
        category = item.get("category", "Khác")
        category_totals[category] = (
            category_totals.get(category, 0) + float(item["amount"])
        )

    print("\nChi tiêu theo danh mục:")
    for category, amount in sorted(category_totals.items()):
        print(f"- {category}: {format_money(amount)}")


def main():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    expenses = load_expenses()

    while True:
        print("\n===== QUẢN LÝ CHI TIÊU CÁ NHÂN =====")
        print("1. Xem lịch sử chi tiêu")
        print("2. Thêm khoản chi")
        print("3. Xem tổng số tiền đã chi tiêu")
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
            print("Lựa chọn không hợp lệ. Hãy nhập 0, 1, 2 hoặc 3.")


if __name__ == "__main__":
    main()
