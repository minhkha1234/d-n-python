# AI Usage

## Tôi đã dùng AI cho việc gì?

- Hỗ trợ chia yêu cầu Week 15 thành bot strategy, kiểm thử, tài liệu và đánh giá.
- Gợi ý cách kiểm tra state đầu vào và thiết kế strategy composition đơn giản.
- Hỗ trợ viết bản nháp README và checklist kiểm thử.

## Tôi đã tự viết hoặc thay đổi phần nào?

- Trước khi nộp, tôi sẽ đọc và kiểm tra lại từng hàm, sửa cách đặt tên hoặc logic nếu cần.
- Tôi sẽ tự chạy tournament và tests trên máy mình, rồi cập nhật báo cáo theo kết quả thực tế.

## Tôi đã kiểm chứng câu trả lời của AI như thế nào?

- Chạy các tests của project bằng `python -m pytest projects/vuacoc-bot-journey/tests -q`.
- Chạy tournament bằng `python projects/vuacoc-bot-journey/local_arena/tournament_cli.py`.
- Kiểm tra các trường hợp state bình thường, đã tới goal, thiếu field và chứa giá trị sai kiểu.

## Một điều tôi hiểu rõ hơn

Bot nhận một dictionary `state` và trả về một action. Với composition, lớp `Bot` không cần biết quy tắc cụ thể; nó chỉ gọi strategy đã được truyền vào. Tôi cần hiểu và có thể giải thích từng quyết định trong code trước khi bảo vệ bài.
