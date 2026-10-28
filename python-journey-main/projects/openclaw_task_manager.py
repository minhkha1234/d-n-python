"""
Ứng dụng quản lý thời gian cá nhân bằng Python.

Chức năng:
- Xem lịch trình theo ngày và giờ.
- Thêm lịch trình với ngày, giờ bắt đầu và thời lượng.
- Đánh dấu lịch trình đã hoàn thành.
- Xóa một lịch trình sau khi xác nhận.
- Thống kê thời lượng đã lên lịch và đã hoàn thành.
- Lưu dữ liệu trong time_schedule.json cạnh file này.

Cách chạy:
    python openclaw_task_manager.py
"""

import json
from pathlib import Path
from datetime import datetime, date

DATA_FILE = Path(__file__).with_name("time_schedule.json")


def load_schedule():
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Không đọc được time_schedule.json. Bắt đầu với lịch trống.")
        return []


def save_schedule(schedule):
    DATA_FILE.write_text(
        json.dumps(schedule, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_schedule(schedule):
    print("\n===== LỊCH TRÌNH CỦA BẠN =====")
    if not schedule:
        print("Chưa có lịch trình nào.")
        return
    for item in sorted(schedule, key=lambda x: (x.get("date", ""), x.get("time", ""))):
        status = "Đã hoàn thành" if item.get("done", False) else "Chưa hoàn thành"
        print(
            f'#{item["id"]}. [{status}] {item["title"]}\n'
            f'   Thời gian: {item.get("date", "Chưa đặt")} '
            f'{item.get("time", "")} | {item.get("duration", 0)} phút'
        )


def add_schedule(schedule):
    title = input("Tên hoạt động: ").strip()
    if not title:
        print("Tên hoạt động không được để trống.")
        return

    date_text = input("Ngày (YYYY-MM-DD, Enter để dùng hôm nay): ").strip()
    if not date_text:
        date_text = date.today().isoformat()
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        print("Ngày không hợp lệ. Hãy nhập theo dạng YYYY-MM-DD.")
        return

    time_text = input("Giờ bắt đầu (HH:MM): ").strip()
    try:
        datetime.strptime(time_text, "%H:%M")
    except ValueError:
        print("Giờ không hợp lệ. Hãy nhập theo dạng HH:MM.")
        return

    duration_text = input("Thời lượng dự kiến (phút): ").strip()
    try:
        duration = int(duration_text)
        if duration <= 0:
            raise ValueError
    except ValueError:
        print("Thời lượng phải là số phút lớn hơn 0.")
        return

    next_id = max((int(item.get("id", 0)) for item in schedule), default=0) + 1
    schedule.append({
        "id": next_id,
        "title": title,
        "date": date_text,
        "time": time_text,
        "duration": duration,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_schedule(schedule)
    print("Đã thêm lịch trình.")


def complete_schedule(schedule):
    if not schedule:
        print("Chưa có lịch trình nào.")
        return
    show_schedule(schedule)
    try:
        item_id = int(input("Nhập ID lịch trình đã hoàn thành: ").strip())
    except ValueError:
        print("ID phải là số nguyên.")
        return
    for item in schedule:
        if item.get("id") == item_id:
            item["done"] = True
            save_schedule(schedule)
            print("Đã cập nhật trạng thái.")
            return
    print("Không tìm thấy ID đó.")


def delete_schedule(schedule):
    if not schedule:
        print("Không có lịch trình để xóa.")
        return
    show_schedule(schedule)
    try:
        item_id = int(input("Nhập ID lịch trình muốn xóa: ").strip())
    except ValueError:
        print("ID phải là số nguyên.")
        return
    for index, item in enumerate(schedule):
        if item.get("id") == item_id:
            print(f'Bạn đã chọn: "{item["title"]}"')
            confirm = input("Bạn có chắc muốn xóa không? (CÓ/KHÔNG): ").strip().upper()
            if confirm == "CÓ":
                removed = schedule.pop(index)
                save_schedule(schedule)
                print(f'Đã xóa lịch trình "{removed["title"]}".')
            else:
                print("Đã hủy. Lịch trình vẫn được giữ nguyên.")
            return
    print("Không tìm thấy ID đó.")


def show_summary(schedule):
    total = sum(int(item.get("duration", 0)) for item in schedule)
    done = sum(int(item.get("duration", 0)) for item in schedule if item.get("done", False))
    pending = total - done
    print("\n===== THỐNG KÊ THỜI GIAN =====")
    print(f"Số lịch trình: {len(schedule)}")
    print(f"Tổng thời lượng đã lên lịch: {total} phút ({total // 60} giờ {total % 60} phút)")
    print(f"Thời lượng hoạt động hoàn thành: {done} phút")
    print(f"Thời lượng chưa hoàn thành: {pending} phút")


def main():
    schedule = load_schedule()
    while True:
        print("\n===== QUẢN LÝ THỜI GIAN CÁ NHÂN =====")
        print("1. Xem lịch trình")
        print("2. Thêm lịch trình")
        print("3. Đánh dấu lịch trình hoàn thành")
        print("4. Xóa một lịch trình")
        print("5. Xem thống kê thời gian")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            show_schedule(schedule)
        elif choice == "2":
            add_schedule(schedule)
        elif choice == "3":
            complete_schedule(schedule)
        elif choice == "4":
            delete_schedule(schedule)
        elif choice == "5":
            show_summary(schedule)
        elif choice == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập 0, 1, 2, 3, 4, 5 hoặc 0.")


if __name__ == "__main__":
    main()
