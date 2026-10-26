<p align="center">
  <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-banner-dark.png" alt="OpenClaw — trợ lý AI cá nhân" width="920">
</p>

<h1 align="center">OpenClaw <sup>🦞</sup></h1>

<p align="center">
  <strong>Một trợ lý AI. Những ứng dụng bạn dùng. Quy trình làm việc do bạn kiểm soát.</strong>
  <br>
  Hướng dẫn tiếng Việt về cài đặt, kết nối và mở rộng OpenClaw.
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw"><img src="https://img.shields.io/badge/PROJECT-OpenClaw-111827?style=for-the-badge&logo=github" alt="Dự án OpenClaw"></a>
  <a href="https://www.npmjs.com/package/openclaw"><img src="https://img.shields.io/npm/v/openclaw?style=for-the-badge&label=NPM" alt="Phiên bản npm"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/openclaw?style=for-the-badge&label=NODE.JS" alt="Phiên bản Node.js"></a>
</p>

<p align="center">
  <a href="https://docs.openclaw.ai/start/getting-started">🚀 Bắt đầu</a>
  &nbsp; · &nbsp;
  <a href="https://docs.openclaw.ai">📚 Tài liệu</a>
  &nbsp; · &nbsp;
  <a href="https://docs.openclaw.ai/gateway/security">🛡️ Bảo mật</a>
  &nbsp; · &nbsp;
  <a href="https://discord.gg/clawd">💬 Cộng đồng</a>
</p>

---

<table>
  <tr>
    <td width="33%" align="center">
      <h3>💬 Kết nối</h3>
      Trò chuyện qua các nền tảng nhắn tin được hỗ trợ.
    </td>
    <td width="33%" align="center">
      <h3>🧩 Mở rộng</h3>
      Thêm công cụ, skills và plugins theo nhu cầu.
    </td>
    <td width="33%" align="center">
      <h3>🔐 Tự kiểm soát</h3>
      Tự chọn mô hình, kết nối và quyền truy cập.
    </td>
  </tr>
</table>

## 🧭 Bản đồ nội dung

| Nhanh đến phần | Dành cho bạn |
| --- | --- |
| **[Cài đặt](#-cài-đặt)** | Muốn cài OpenClaw trên Windows, macOS hoặc Linux |
| **[Thiết lập lần đầu](#-thiết-lập-lần-đầu)** | Muốn chạy Gateway và mở giao diện điều khiển |
| **[Tích hợp & mở rộng](#-tích-hợp--mở-rộng)** | Muốn kết nối ứng dụng, công cụ hoặc plugins |
| **[Bảo mật](#-bảo-mật-trước-khi-sử-dụng)** | Muốn kiểm tra quyền và cấu hình an toàn |
| **[Phát triển](#-dành-cho-người-phát-triển)** | Muốn tải mã nguồn và đóng góp dự án |

## ✨ OpenClaw là gì?

OpenClaw là trợ lý AI mã nguồn mở chạy trong môi trường do bạn thiết lập. Bạn có thể tương tác với trợ lý qua các nền tảng nhắn tin, kết nối công cụ và mở rộng chức năng bằng skills hoặc plugins. **Gateway** là lớp điều phối trung tâm cho phiên làm việc, công cụ và các kết nối.

Bạn có thể chọn nhà cung cấp mô hình AI, kênh giao tiếp và các tích hợp được bật. Tuy nhiên, không phải tích hợp nào cũng hoạt động ngay sau khi cài: một số cần tài khoản, thông tin xác thực, cấu hình và quyền riêng biệt.

### Những khả năng chính

<table>
  <tr>
    <td width="50%">
      <h3>💬 Nhắn tin đa kênh</h3>
      Kết nối những nền tảng được hỗ trợ như Telegram, Discord, WhatsApp, Slack, Signal, iMessage và các kênh khác.
    </td>
    <td width="50%">
      <h3>🧠 Lựa chọn mô hình</h3>
      Dùng nhà cung cấp AI tương thích hoặc mô hình chạy cục bộ, tùy cấu hình và phần cứng.
    </td>
  </tr>
  <tr>
    <td>
      <h3>⚙️ Công cụ & tự động hóa</h3>
      Cho phép trợ lý sử dụng công cụ đã cấu hình để hỗ trợ các quy trình làm việc.
    </td>
    <td>
      <h3>🧩 Skills & plugins</h3>
      Mở rộng tính năng mà không nhất thiết phải sửa phần lõi.
    </td>
  </tr>
  <tr>
    <td>
      <h3>🖥️ Nhiều giao diện</h3>
      Vận hành qua Control UI, dòng lệnh (CLI) hoặc giao diện đầu cuối (TUI).
    </td>
    <td>
      <h3>📱 Thiết bị tương thích</h3>
      Có thể mở rộng sang các khả năng trên thiết bị được hỗ trợ; tính năng thực tế phụ thuộc nền tảng.
    </td>
  </tr>
</table>

## 🏗️ Cách các thành phần hoạt động

    Ứng dụng nhắn tin · Control UI · CLI · TUI
                      │
                      ▼
                OpenClaw Gateway
           ┌──────────┼──────────┐
           ▼          ▼          ▼
       Phiên &      Công cụ    Channels /
       bộ nhớ                  Plugins
           └──────────┼──────────┘
                      ▼
             Mô hình AI đã chọn

| Thành phần | Vai trò |
| --- | --- |
| **Gateway** | Điều phối phiên, sự kiện, công cụ và kết nối |
| **Control UI / CLI / TUI** | Các giao diện để vận hành OpenClaw |
| **Channels** | Kết nối trợ lý với những nền tảng nhắn tin |
| **Tools / Skills / Plugins** | Bổ sung khả năng theo cấu hình |

Đọc thêm: [Kiến trúc](https://docs.openclaw.ai/concepts/architecture) · [Gateway](https://docs.openclaw.ai/gateway).

## 🚀 Cài đặt

Chọn hướng dẫn phù hợp với hệ điều hành. Trước khi cài, hãy kiểm tra [yêu cầu và hướng dẫn chính thức](https://docs.openclaw.ai/install) vì yêu cầu phiên bản có thể thay đổi.

<details>
  <summary><strong>🪟 Windows — PowerShell</strong></summary>

  Mở PowerShell và chạy trình cài đặt chính thức:

  <pre><code>iwr -useb https://openclaw.ai/install.ps1 | iex</code></pre>
</details>

<details>
  <summary><strong>🐧 macOS / Linux / WSL2</strong></summary>

  Chạy lệnh cài đặt chính thức:

  <pre><code>curl -fsSL https://openclaw.ai/install.sh | bash</code></pre>
</details>

<details>
  <summary><strong>📦 Cài qua npm</strong></summary>

  README của nhánh main trong dự án OpenClaw hiện nêu Node.js **24.16+ hoặc 26.1+**, đồng thời khuyến nghị Node.js 26. Hãy xác nhận lại phiên bản yêu cầu trong tài liệu chính thức trước khi cài.

  <pre><code>npm install -g openclaw@latest --allow-scripts=openclaw</code></pre>

  Tham số <code>--allow-scripts=openclaw</code> áp dụng cho npm 12 hoặc npm 11.16+. Nếu bạn dùng npm 11.15 trở xuống, hãy làm theo ghi chú trong [hướng dẫn cài đặt](https://docs.openclaw.ai/install).
</details>

> **Lưu ý an toàn:** Các lệnh cài đặt bằng script sẽ tải và thực thi nội dung từ Internet. Nếu muốn kiểm tra trước, hãy xem script và xác nhận nguồn tải là chính thức trước khi chạy.

## 🛠️ Thiết lập lần đầu

Sau khi cài đặt, hoàn tất trình hướng dẫn onboarding. Với bản cài trực tiếp qua npm, pnpm hoặc Bun, chạy:

<pre><code>openclaw onboard --install-daemon</code></pre>

Kiểm tra Gateway và mở giao diện điều khiển:

<pre><code>openclaw gateway status
openclaw dashboard</code></pre>

### Checklist sau khi cài

- [ ] Chọn nhà cung cấp mô hình và thiết lập thông tin xác thực.
- [ ] Kết nối một kênh nhắn tin theo tài liệu của kênh đó.
- [ ] Gửi tin nhắn thử để kiểm tra kết nối.
- [ ] Rà soát quyền của công cụ, plugins và người được phép tương tác.
- [ ] Đọc hướng dẫn bảo mật trước khi cho người khác truy cập hoặc mở Gateway ra mạng.

Hướng dẫn đầy đủ: [Bắt đầu với OpenClaw](https://docs.openclaw.ai/start/getting-started).

## 🧩 Tích hợp & mở rộng

<table>
  <tr>
    <td width="50%">
      <h3>💬 Kênh nhắn tin</h3>
      Chọn nền tảng bạn muốn kết nối và làm theo yêu cầu riêng của nền tảng.
      <p><a href="https://docs.openclaw.ai/channels">Xem danh sách Channels →</a></p>
    </td>
    <td width="50%">
      <h3>🧰 Công cụ & plugins</h3>
      Xem chức năng, quyền cần thiết và nguồn gốc của từng phần mở rộng trước khi bật.
      <p><a href="https://docs.openclaw.ai/tools">Tools</a> · <a href="https://docs.openclaw.ai/tools/skills">Skills</a> · <a href="https://docs.openclaw.ai/plugins">Plugins</a></p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>🧱 Tự xây dựng plugin</h3>
      Tham khảo hướng dẫn và SDK để tạo tích hợp theo nhu cầu.
      <p><a href="https://docs.openclaw.ai/plugins/building-plugins">Plugin SDK & hướng dẫn →</a></p>
    </td>
    <td>
      <h3>📱 Nodes & nền tảng</h3>
      Kiểm tra khả năng tương thích và cách cấu hình cho các thiết bị được hỗ trợ.
      <p><a href="https://docs.openclaw.ai/platforms">Platforms</a> · <a href="https://docs.openclaw.ai/nodes">Nodes</a></p>
    </td>
  </tr>
</table>

Bạn cũng có thể khám phá [ClawHub](https://clawhub.ai) để tìm skills. Chỉ cài phần mở rộng từ nguồn bạn tin cậy và xem xét quyền mà chúng yêu cầu.

## 🛡️ Bảo mật trước khi sử dụng

OpenClaw có thể được cấp quyền dùng công cụ và tài nguyên trong môi trường chạy nó. Cấu hình sai có thể làm lộ dữ liệu hoặc cho phép thực hiện hành động ngoài dự kiến, nhất là khi nhận tin nhắn từ người lạ.

| Nguyên tắc | Việc nên làm |
| --- | --- |
| **Xác minh nguồn tin nhắn** | Coi nội dung đầu vào là dữ liệu không đáng tin cậy; không để lời nhắn tự ý ghi đè quy tắc hoặc tiết lộ bí mật. |
| **Giới hạn quyền truy cập** | Chỉ cho phép người dùng cần thiết; xem xét và phê duyệt yêu cầu pairing khi tính năng này được dùng. |
| **Cấp quyền tối thiểu** | Chỉ bật công cụ cần thiết; kiểm tra mã nguồn và hành vi của skills/plugins trước khi cài. |
| **Bảo vệ Gateway** | Không mở trực tiếp dịch vụ ra Internet nếu chưa hiểu rủi ro và chưa làm theo hướng dẫn bảo mật. |
| **Cô lập công cụ** | Xem xét sandboxing; nếu không, công cụ có thể chạy với quyền của tiến trình chủ. |
| **Giữ bí mật thông tin xác thực** | Không đưa API key, token hoặc cấu hình chứa bí mật lên Git hay nơi công khai. |
| **Xác nhận hành động quan trọng** | Thiết lập bước kiểm tra phù hợp trước khi gửi thông điệp, thay đổi dữ liệu hoặc chạy lệnh. |

Tài liệu nên đọc:

- [Hướng dẫn bảo mật Gateway](https://docs.openclaw.ai/gateway/security)
- [Hướng dẫn khi mở dịch vụ ra mạng](https://docs.openclaw.ai/gateway/security/exposure-runbook)
- [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)
- [Chính sách bảo mật của dự án](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)

## 📚 Tài liệu tra cứu nhanh

| Khi cần… | Mở tài liệu |
| --- | --- |
| Chọn mô hình và nhà cung cấp | [Models](https://docs.openclaw.ai/concepts/models) · [Model providers](https://docs.openclaw.ai/concepts/model-providers) |
| Kết nối ứng dụng nhắn tin | [Channels](https://docs.openclaw.ai/channels) |
| Sử dụng công cụ và phần mở rộng | [Tools](https://docs.openclaw.ai/tools) · [Skills](https://docs.openclaw.ai/tools/skills) · [Plugins](https://docs.openclaw.ai/plugins) |
| Dùng giao diện hoặc dòng lệnh | [Control UI](https://docs.openclaw.ai/web/control-ui) · [CLI](https://docs.openclaw.ai/cli) · [TUI](https://docs.openclaw.ai/web/tui) |
| Cấu hình Gateway | [Gateway](https://docs.openclaw.ai/gateway) · [Cấu hình](https://docs.openclaw.ai/gateway/configuration) |
| Cập nhật phiên bản | [Updating](https://docs.openclaw.ai/install/updating) · [Release channels](https://docs.openclaw.ai/install/development-channels) |
| Khắc phục sự cố | [FAQ](https://docs.openclaw.ai/help/faq) |

## 👩‍💻 Dành cho người phát triển

Repository nguồn sử dụng **pnpm workspace**; không chạy <code>npm install</code> ở thư mục gốc của repository nguồn.

<pre><code>git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build</code></pre>

Trước khi sửa mã nguồn, hãy đọc [CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) và [hướng dẫn thiết lập môi trường](https://docs.openclaw.ai/start/setup).

### Cấu trúc repository nguồn

| Thư mục / tệp | Vai trò khái quát |
| --- | --- |
| <code>apps/</code> | Ứng dụng theo nền tảng |
| <code>ui/</code> | Giao diện người dùng |
| <code>packages/</code> | Các gói dùng chung trong workspace |
| <code>extensions/</code> | Tích hợp và phần mở rộng |
| <code>examples/</code> | Ví dụ tham khảo |
| <code>docs/</code> | Tài liệu dự án |
| <code>tools/</code> | Công cụ hỗ trợ phát triển |
| <code>openclaw.mjs</code> và <code>package.json</code> | Điểm vào CLI và cấu hình package ở thư mục gốc |

Đây là sơ đồ định hướng; hãy kiểm tra cấu trúc và cấu hình hiện tại của nhánh bạn đang dùng trước khi thay đổi.

## 🤝 Đóng góp & cộng đồng

- Đọc [hướng dẫn đóng góp](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md).
- Báo lỗi hoặc đề xuất qua [Issue chooser](https://github.com/openclaw/openclaw/issues/new/choose).
- Trao đổi tại [OpenClaw Community](https://community.openclaw.ai/) hoặc [Discord](https://discord.gg/clawd).
- Với vấn đề bảo mật, hãy dùng quy trình báo cáo riêng; không công khai chi tiết lỗ hổng chưa được khắc phục.
- Tham khảo [VISION.md](https://github.com/openclaw/openclaw/blob/main/VISION.md) để hiểu định hướng dự án.

## 📄 Giấy phép

OpenClaw được phát hành theo giấy phép [MIT](https://github.com/openclaw/openclaw/blob/main/LICENSE). Xem thêm [thông báo thành phần bên thứ ba](https://github.com/openclaw/openclaw/blob/main/THIRD_PARTY_NOTICES.md).

---

<p align="center">
  <strong>Bắt đầu nhỏ. Cấp quyền tối thiểu. Mở rộng khi bạn đã hiểu rõ cấu hình.</strong>
  <br>
  <sub>Bản hướng dẫn tiếng Việt độc lập cho dự án OpenClaw.</sub>
</p>
