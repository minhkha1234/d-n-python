"""
Dự án mini lấy cảm hứng từ OpenClaw: Trình quản lý công việc bằng Python.

Lưu ý:
- Đây là ứng dụng độc lập, KHÔNG kết nối trực tiếp tới OpenClaw.
- Chỉ dùng thư viện chuẩn của Python.
- Dữ liệu được lưu trong tasks.json cạnh file này.

Cách chạy:
    python openclaw_task_manager.py
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Đọc danh sách công việc; nếu chưa có file thì trả về danh sách rỗng."""
    if not DATA_FILE.exists():
        return []

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Không đọc được tasks.json. Bắt đầu với danh sách trống.")
        return []


def save_tasks(tasks):
    """Lưu công việc thành JSON để dùng lại ở lần chạy sau."""
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_tasks(tasks):
    """Hiển thị tất cả công việc."""
    if not tasks:
        print("\nChưa có công việc nào.")
        return

    print("\n===== DANH SÁCH CÔNG VIỆC =====")
    for task in tasks:
        status = "Hoàn thành" if task["done"] else "Chưa xong"
        print(f'{task["id"]}. [{status}] {task["title"]}')
        print(f'   Tạo lúc: {task["created_at"]}')


def add_task(tasks):
    """Thêm một công việc mới."""
    title = input("Nhập tên công việc: ").strip()
    if not title:
        print("Tên công việc không được để trống.")
        return

    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append(
        {
            "id": next_id,
            "title": title,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )
    save_tasks(tasks)
    print("Đã thêm công việc.")


def complete_task(tasks):
    """Đánh dấu một công việc là hoàn thành."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("Nhập ID công việc đã hoàn thành: "))
    except ValueError:
        print("ID phải là một số nguyên.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Đã cập nhật trạng thái công việc.")
            return

    print("Không tìm thấy công việc có ID đó.")


def main():
    """Vòng lặp menu chính của chương trình."""
    tasks = load_tasks()

    while True:
        print("\n=== OPENCLAW-INSPIRED TASK MANAGER ===")
        print("1. Xem công việc")
        print("2. Thêm công việc")
        print("3. Đánh dấu hoàn thành")
        print("0. Thoát")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn 0, 1, 2 hoặc 3.")


if __name__ == "__main__":
    main()
