<p align="center">
  <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-dark.png" alt="OpenClaw — trợ lý AI cá nhân trên thiết bị của bạn" width="900">
</p>

<h1 align="center">OpenClaw 🦞</h1>

<p align="center">
  <strong>Trợ lý AI của bạn. Trên thiết bị của bạn. Trong những ứng dụng bạn dùng hằng ngày.</strong>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=flat-square&label=CI" alt="Trạng thái CI"></a>
  <a href="https://www.npmjs.com/package/openclaw"><img src="https://img.shields.io/npm/v/openclaw?style=flat-square&label=phi%C3%AAn%20b%E1%BA%A3n%20npm" alt="Phiên bản npm"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/openclaw?style=flat-square" alt="Phiên bản Node.js"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="Giấy phép MIT"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=Discord&logo=discord&logoColor=white&color=5865F2&style=flat-square" alt="Cộng đồng Discord"></a>
</p>

OpenClaw là trợ lý AI mã nguồn mở chạy trên máy tính hoặc thiết bị của bạn. Bạn có thể trò chuyện với trợ lý qua những nền tảng nhắn tin quen thuộc, kết nối các công cụ và mở rộng khả năng bằng skills hoặc plugins. Một **Gateway** điều phối phiên làm việc, công cụ và kết nối; cấu hình sẽ quyết định cách bạn dùng cho cá nhân hay nhóm.

**Tự chủ, có thể mở rộng và ưu tiên dữ liệu tại máy của bạn.** Bộ nhớ, trạng thái và thông tin xác thực được quản lý trong môi trường bạn thiết lập. Bạn lựa chọn nhà cung cấp mô hình, kênh giao tiếp và các tích hợp được bật. Hãy đọc tài liệu bảo mật và kiểm tra quyền của từng tích hợp trước khi sử dụng.

<p align="center">
  <a href="https://openclaw.ai">Trang chủ</a> ·
  <a href="https://docs.openclaw.ai">Tài liệu</a> ·
  <a href="https://docs.openclaw.ai/start/getting-started">Bắt đầu nhanh</a> ·
  <a href="https://docs.openclaw.ai/start/why-openclaw">Kiến trúc và lý do chọn OpenClaw</a> ·
  <a href="https://docs.openclaw.ai/help/faq">Câu hỏi thường gặp</a> ·
  <a href="VISION.md">Tầm nhìn dự án</a>
</p>

---

## Mục lục

- [OpenClaw làm được gì?](#openclaw-làm-được-gì)
- [Kiến trúc tổng quan](#kiến-trúc-tổng-quan)
- [Cài đặt](#cài-đặt)
- [Thiết lập lần đầu](#thiết-lập-lần-đầu)
- [Các hướng mở rộng](#các-hướng-mở-rộng)
- [Bảo mật trước khi sử dụng](#bảo-mật-trước-khi-sử-dụng)
- [Tài liệu theo nhu cầu](#tài-liệu-theo-nhu-cầu)
- [Phát triển từ mã nguồn](#phát-triển-từ-mã-nguồn)
- [Đóng góp và cộng đồng](#đóng-góp-và-cộng-đồng)
- [Giấy phép](#giấy-phép)

## OpenClaw làm được gì?

| Khả năng | Mô tả |
| --- | --- |
| **Trò chuyện đa kênh** | Kết nối các nền tảng được hỗ trợ như Telegram, Discord, WhatsApp, Slack, Signal, iMessage và những kênh khác. Danh sách và điều kiện hỗ trợ có thể thay đổi theo nền tảng. |
| **Nhiều nhà cung cấp mô hình** | Chọn nhà cung cấp AI được hỗ trợ hoặc mô hình chạy cục bộ, tùy cấu hình và phần cứng. |
| **Công cụ và tự động hóa** | Cho phép trợ lý sử dụng các công cụ đã cấu hình để hỗ trợ quy trình làm việc. Chỉ bật những quyền thực sự cần thiết. |
| **Skills và plugins** | Mở rộng chức năng theo nhu cầu thay vì sửa trực tiếp phần lõi. |
| **Giao diện điều khiển** | Quản lý trợ lý thông qua Control UI, dòng lệnh (CLI) hoặc giao diện đầu cuối (TUI). |
| **Ứng dụng và thiết bị đồng hành** | Trên nền tảng tương thích, có thể mở rộng sang các khả năng như giọng nói và hành động tại thiết bị. |

> OpenClaw là nền tảng có thể cấu hình, không phải mọi tích hợp đều tự động hoạt động sau khi cài đặt. Bạn có thể cần thiết lập tài khoản, thông tin xác thực, quyền truy cập và dịch vụ bên ngoài.

## Kiến trúc tổng quan

```text
Ứng dụng nhắn tin / Control UI / CLI / TUI
                    │
                    ▼
              OpenClaw Gateway
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    Phiên & bộ nhớ  Công cụ    Kênh / Plugins
        │           │           │
        └───────────┼───────────┘
                    ▼
       Nhà cung cấp mô hình AI đã chọn
```

- **Gateway:** lớp điều phối trung tâm cho phiên, sự kiện, công cụ và kết nối.
- **Control UI / CLI / TUI:** các giao diện để vận hành và tương tác với Gateway.
- **Channels:** kết nối trợ lý với nền tảng nhắn tin.
- **Tools, skills và plugins:** bổ sung khả năng theo cấu hình.

Tìm hiểu chi tiết trong tài liệu [kiến trúc](https://docs.openclaw.ai/concepts/architecture) và [Gateway](https://docs.openclaw.ai/gateway).

## Cài đặt

OpenClaw cung cấp cách cài đặt cho macOS, Linux và Windows. Hãy xem [hướng dẫn cài đặt chính thức](https://docs.openclaw.ai/install) để kiểm tra yêu cầu hệ thống và phương án phù hợp với máy của bạn.

### Windows — PowerShell

Mở PowerShell và chạy trình cài đặt chính thức:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### macOS / Linux / WSL2

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Lưu ý an toàn:** các lệnh trên tải và thực thi trình cài đặt từ Internet. Nếu muốn kiểm tra trước, hãy mở trang cài đặt chính thức, xem nội dung script và xác nhận bạn đang dùng đúng nguồn trước khi chạy.

### Cài qua npm

Nếu bạn đã quản lý Node.js và npm, hãy làm theo yêu cầu phiên bản trong tài liệu hiện hành. README của nhánh `main` hiện hướng dẫn Node.js **24.16+ hoặc 26.1+** (khuyến nghị Node.js 26) và npm tương thích:

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

Tham số `--allow-scripts=openclaw` áp dụng cho npm 12 hoặc npm 11.16+. Với npm 11.15 trở xuống, hãy làm theo ghi chú trong [hướng dẫn cài đặt](https://docs.openclaw.ai/install), không tự ý thay đổi lệnh nếu chưa hiểu tác động.

## Thiết lập lần đầu

Sau khi cài đặt, hoàn tất trình hướng dẫn onboarding. Nếu bạn cài gói trực tiếp qua npm, pnpm hoặc Bun, chạy:

```bash
openclaw onboard --install-daemon
```

Kiểm tra Gateway và mở giao diện điều khiển:

```bash
openclaw gateway status
openclaw dashboard
```

Tiếp theo:

1. Cấu hình nhà cung cấp mô hình và thông tin xác thực.
2. Kết nối một kênh nhắn tin theo hướng dẫn tương ứng.
3. Kiểm tra kết nối bằng một tin nhắn thử.
4. Xem lại quyền của công cụ, plugins và người dùng được phép tương tác.
5. Đọc hướng dẫn bảo mật trước khi cho phép người khác truy cập hoặc mở Gateway ra mạng.

Hướng dẫn đầy đủ: [Bắt đầu với OpenClaw](https://docs.openclaw.ai/start/getting-started).

## Các hướng mở rộng

### Kết nối kênh nhắn tin

Chọn nền tảng bạn cần và làm theo hướng dẫn chính thức: [Danh sách Channels](https://docs.openclaw.ai/channels).

### Thêm công cụ, skills và plugins

Mở rộng theo từng nhu cầu và chỉ cấp quyền cần thiết:

- [Tools](https://docs.openclaw.ai/tools)
- [Skills](https://docs.openclaw.ai/tools/skills)
- [Plugins](https://docs.openclaw.ai/plugins)
- [Plugin SDK](https://docs.openclaw.ai/plugins/building-plugins)
- [ClawHub](https://clawhub.ai)

### Chạy trên thiết bị được hỗ trợ

Tham khảo [nền tảng](https://docs.openclaw.ai/platforms) và [nodes](https://docs.openclaw.ai/nodes) để xem khả năng tương thích, giới hạn và cách cấu hình.

## Bảo mật trước khi sử dụng

OpenClaw có thể được cấp quyền dùng công cụ và tài nguyên trên máy chủ chạy nó. Hãy cấu hình cẩn thận, đặc biệt nếu kết nối các kênh có tin nhắn từ người lạ.

- **Coi tin nhắn đầu vào là dữ liệu không đáng tin cậy.** Không làm theo hướng dẫn trong tin nhắn chỉ vì nội dung đó yêu cầu trợ lý tiết lộ bí mật hoặc thực hiện hành động.
- **Giới hạn người được phép nhắn tin.** Với kênh hỗ trợ ghép đôi (pairing), hãy xem xét và phê duyệt yêu cầu trước khi cho phép.
- **Hạn chế quyền công cụ.** Chỉ bật các công cụ cần thiết; đọc kỹ hành vi của plugins và skills trước khi cài.
- **Không công khai Gateway tùy tiện.** Tránh mở trực tiếp dịch vụ ra Internet. Nếu cần truy cập từ xa, hãy làm theo hướng dẫn bảo mật chính thức.
- **Cân nhắc sandboxing.** Công cụ có thể chạy với quyền của tiến trình chủ nếu bạn không cấu hình cơ chế cô lập phù hợp.
- **Bảo vệ thông tin xác thực.** Không commit API key, token hoặc tệp cấu hình chứa bí mật lên Git.
- **Kiểm tra trước khi hành động quan trọng.** Với việc gửi thông điệp, thay đổi dữ liệu hoặc thực thi lệnh, hãy cấu hình quy trình xác nhận phù hợp.

Tài liệu cần đọc:

- [Hướng dẫn bảo mật](https://docs.openclaw.ai/gateway/security)
- [Kịch bản bảo vệ khi mở dịch vụ ra mạng](https://docs.openclaw.ai/gateway/security/exposure-runbook)
- [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)
- [Chính sách báo cáo lỗ hổng](SECURITY.md)

## Tài liệu theo nhu cầu

| Bạn muốn… | Tài liệu |
| --- | --- |
| Cấu hình mô hình và xác thực | [Models](https://docs.openclaw.ai/concepts/models) · [Model providers](https://docs.openclaw.ai/concepts/model-providers) |
| Kết nối ứng dụng nhắn tin | [Channels](https://docs.openclaw.ai/channels) |
| Tìm hiểu công cụ và mở rộng | [Tools](https://docs.openclaw.ai/tools) · [Skills](https://docs.openclaw.ai/tools/skills) · [Plugins](https://docs.openclaw.ai/plugins) |
| Dùng giao diện hoặc dòng lệnh | [Control UI](https://docs.openclaw.ai/web/control-ui) · [CLI](https://docs.openclaw.ai/cli) · [TUI](https://docs.openclaw.ai/web/tui) |
| Quản lý Gateway | [Gateway](https://docs.openclaw.ai/gateway) · [Cấu hình](https://docs.openclaw.ai/gateway/configuration) |
| Cập nhật và chọn kênh phát hành | [Updating](https://docs.openclaw.ai/install/updating) · [Release channels](https://docs.openclaw.ai/install/development-channels) |
| Khắc phục sự cố | [FAQ](https://docs.openclaw.ai/help/faq) |

## Phát triển từ mã nguồn

Repository sử dụng **pnpm workspace**; `npm install` ở thư mục gốc không được hỗ trợ.

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build
```

Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [hướng dẫn thiết lập môi trường phát triển](https://docs.openclaw.ai/start/setup) trước khi sửa mã nguồn.

### Cấu trúc cấp cao

| Đường dẫn | Vai trò |
| --- | --- |
| `apps/` | Các ứng dụng theo nền tảng |
| `ui/` | Giao diện người dùng |
| `packages/` | Các gói dùng chung trong workspace |
| `extensions/` | Tích hợp và mở rộng |
| `examples/` | Ví dụ tham khảo |
| `docs/` | Tài liệu dự án |
| `tools/` | Công cụ hỗ trợ phát triển |
| `openclaw.mjs` và `package.json` | Điểm vào CLI và cấu hình package ở thư mục gốc |

Đây là bản tóm tắt định hướng; hãy kiểm tra nội dung thư mục và cấu hình hiện tại trước khi thay đổi cấu trúc.

## Đóng góp và cộng đồng

- Đọc [hướng dẫn đóng góp](CONTRIBUTING.md).
- Dùng [Issue chooser](https://github.com/openclaw/openclaw/issues/new/choose) để báo lỗi hoặc đề xuất theo đúng mẫu.
- Trao đổi và nhận hỗ trợ tại [cộng đồng OpenClaw](https://community.openclaw.ai/) hoặc [Discord](https://discord.gg/clawd).
- Báo cáo vấn đề bảo mật qua quy trình riêng trong [SECURITY.md](SECURITY.md); không công khai chi tiết lỗ hổng chưa được khắc phục.
- Các tính năng mới thường nên được đề xuất trước; hãy cân nhắc plugin thay vì sửa phần lõi nếu phù hợp với định hướng dự án.

OpenClaw được phát triển dưới sự quản lý của [OpenClaw Foundation](https://openclaw.org). Xem [tầm nhìn dự án](VISION.md) để hiểu định hướng phát triển.

## Giấy phép

OpenClaw sử dụng giấy phép [MIT](LICENSE) © OpenClaw Foundation. Xem thêm [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) về các thành phần bên thứ ba được tích hợp hoặc điều chỉnh.

---

<p align="center">
  <em>Hãy bắt đầu từ một kênh, cấp quyền tối thiểu và mở rộng dần theo nhu cầu.</em>
</p>
