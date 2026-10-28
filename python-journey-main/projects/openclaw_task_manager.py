"""
Ứng dụng quản lý công việc bằng Python.

Chức năng:
- Xem danh sách công việc.
- Thêm công việc mới.
- Đánh dấu công việc đã hoàn thành.
- Xóa một công việc theo ID sau khi xác nhận.
- Lưu dữ liệu trong tasks.json cạnh file này.

Cách chạy:
    python openclaw_task_manager.py
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Đọc danh sách công việc từ file JSON."""
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Không đọc được tasks.json. Bắt đầu với danh sách trống.")
        return []


def save_tasks(tasks):
    """Lưu danh sách công việc vào file JSON."""
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_tasks(tasks):
    """Hiển thị danh sách công việc."""
    print("\n===== DANH SÁCH CÔNG VIỆC =====")
    if not tasks:
        print("Chưa có công việc nào.")
        return

    for task in tasks:
        status = "Hoàn thành" if task.get("done", False) else "Chưa hoàn thành"
        print(f'#{task["id"]}. [{status}] {task["title"]}')
        print(f'   Ngày tạo: {task.get("created_at", "Không rõ")}')


def add_task(tasks):
    """Thêm công việc mới."""
    title = input("Nhập tên công việc: ").strip()
    if not title:
        print("Tên công việc không được để trống.")
        return

    next_id = max((int(task.get("id", 0)) for task in tasks), default=0) + 1
    tasks.append({
        "id": next_id,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_tasks(tasks)
    print("Đã thêm công việc thành công.")


def complete_task(tasks):
    """Đánh dấu công việc là hoàn thành theo ID."""
    if not tasks:
        print("\nChưa có công việc nào để cập nhật.")
        return

    show_tasks(tasks)
    try:
        task_id = int(input("Nhập ID công việc đã hoàn thành: ").strip())
    except ValueError:
        print("ID phải là một số nguyên.")
        return

    for task in tasks:
        if task.get("id") == task_id:
            if task.get("done", False):
                print("Công việc này đã hoàn thành trước đó.")
                return
            task["done"] = True
            save_tasks(tasks)
            print("Đã đánh dấu công việc hoàn thành.")
            return

    print("Không tìm thấy công việc có ID đó.")


def delete_task(tasks):
    """Xóa một công việc sau khi người dùng xác nhận."""
    if not tasks:
        print("\nKhông có công việc nào để xóa.")
        return

    show_tasks(tasks)
    try:
        task_id = int(input("Nhập ID công việc muốn xóa: ").strip())
    except ValueError:
        print("ID phải là một số nguyên.")
        return

    for index, task in enumerate(tasks):
        if task.get("id") == task_id:
            print(f'\nBạn đã chọn công việc: "{task["title"]}"')
            confirm = input(
                "Bạn có muốn xóa công việc này không? (Nhập CÓ hoặc KHÔNG): "
            ).strip().upper()

            if confirm == "CÓ":
                deleted_task = tasks.pop(index)
                save_tasks(tasks)
                print(f'Đã xóa công việc: {deleted_task["title"]}')
            else:
                print("Đã hủy thao tác. Công việc vẫn được giữ nguyên.")
            return

    print("Không tìm thấy công việc có ID đó.")


def main():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    tasks = load_tasks()

    while True:
        print("\n===== QUẢN LÝ CÔNG VIỆC CÁ NHÂN =====")
        print("1. Xem danh sách công việc")
        print("2. Thêm công việc")
        print("3. Đánh dấu công việc hoàn thành")
        print("4. Xóa một công việc")
        print("0. Thoát")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập 0, 1, 2, 3 hoặc 4.")


if __name__ == "__main__":
    main()
