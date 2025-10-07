# 🔐 SecureFileChain — Blockchain-Based File Storage

**SecureFileChain** là ứng dụng minh họa hệ thống **lưu trữ file an toàn phi tập trung** dựa trên **Blockchain** và **IPFS (InterPlanetary File System)**.  
Dự án được xây dựng bằng **Flask**, sử dụng **PyCryptodome** để mã hóa dữ liệu và **IPFS** để lưu trữ tệp tin nhằm đảm bảo **tính bảo mật, toàn vẹn và minh bạch**.

---

## ⚙️ 1. Yêu cầu hệ thống

- Python **3.10** hoặc cao hơn  
- **IPFS Desktop** hoặc **IPFS Daemon (CLI)**  
- Trình quản lý gói **pip** (đi kèm Python)

---

## 📦 2. Cài đặt môi trường

### 🔹 Bước 1: Tải mã nguồn

Clone dự án từ GitHub:

```bash
git clone https://github.com/codingBeast25/Blockchain-based-File-Storage.git
cd Blockchain-based-File-Storage
```

Hoặc tải file ZIP từ GitHub → giải nén → mở thư mục dự án trong **VS Code** hoặc **Command Prompt**.

---

### 🔹 Bước 2: Tạo môi trường ảo (khuyến nghị)

Tạo môi trường ảo để cách ly các gói thư viện Python:

```bash
python -m venv venv
```

Kích hoạt môi trường ảo:

**Trên Windows:**
```bash
venv\Scripts\activate
```

**Trên macOS / Linux:**
```bash
source venv/bin/activate
```

---

### 🔹 Bước 3: Cài đặt thư viện cần thiết

Cài đặt các gói Python bằng file `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Nội dung khuyến nghị cho file `requirements.txt`:**

```
Flask==1.1.4
numpy==1.23.5
requests==2.28.1
Werkzeug==1.0.1
pycryptodome
ipfshttpclient
```

> ⚠️ **Lưu ý:**  
> Gói `ipfs-http-client` đã bị ngừng hỗ trợ. Hãy thay bằng `ipfshttpclient` (viết liền, không có dấu gạch giữa).

---

## 🌐 3. Cài đặt và khởi động IPFS

### 🔸 Cách 1: Dùng **IPFS Desktop** (Khuyến nghị)

Tải IPFS Desktop tại:  
👉 [https://github.com/ipfs/ipfs-desktop/releases](https://github.com/ipfs/ipfs-desktop/releases)

Cài đặt file tương ứng với hệ điều hành của bạn (ví dụ cho Windows):

```
ipfs-desktop-setup-0.45.0-win-x64.exe
```

Sau khi cài đặt, mở **IPFS Desktop** và đảm bảo trạng thái hiển thị là **Online**.

IPFS thường hoạt động ở địa chỉ:

```
http://127.0.0.1:5001
```

---

### 🔸 Cách 2: Dùng **IPFS CLI**

Nếu bạn đã cài IPFS CLI, chạy lệnh sau trong terminal:

```bash
ipfs daemon
```

Khi thấy thông báo:

```
Daemon is ready
```

→ IPFS đã sẵn sàng hoạt động.

---

## 🚀 4. Chạy ứng dụng Flask

Sau khi cài đặt đầy đủ thư viện và IPFS đang hoạt động, chạy server Flask:

```bash
python app.py
```

Hoặc nếu file chính của bạn tên khác (ví dụ `main.py`):

```bash
python main.py
```

Mở trình duyệt và truy cập địa chỉ:

```
http://127.0.0.1:5000
```

Nếu thấy giao diện web hiển thị → ứng dụng đã chạy thành công 🎉

---

## 🧩 5. Chức năng chính của dự án

| Chức năng | Mô tả |
|------------|--------|
| 🔒 **Mã hóa file** | Sử dụng thuật toán **AES** thông qua thư viện **PyCryptodome** |
| ☁️ **Lưu trữ IPFS** | Upload file mã hóa lên **IPFS**, nhận về **CID** duy nhất |
| ⛓️ **Ghi nhận Blockchain** | Lưu CID lên **Blockchain** để đảm bảo tính minh bạch và bất biến |
| 🔓 **Giải mã & tải xuống** | Cho phép người dùng giải mã và tải lại file gốc khi cần thiết |

---

## 📁 6. Cấu trúc thư mục dự án

```
Blockchain-based-File-Storage/
│
├── app.py                 # Flask server chính
├── requirements.txt       # Danh sách thư viện cần thiết
├── templates/             # Giao diện web (HTML)
├── static/                # CSS, JS, hình ảnh
├── blockchain/            # Mô-đun xử lý blockchain
├── encryption/            # Mã hóa & giải mã file
└── README.md              # Tài liệu hướng dẫn cài đặt & sử dụng
```

---

## 🧠 7. Cách kiểm tra hoạt động

1. Mở **IPFS Desktop** → đảm bảo trạng thái là “Online”.  
2. Mở **terminal** tại thư mục dự án.  
3. Kích hoạt **môi trường ảo** (nếu có).  
4. Chạy lệnh:
   ```bash
   python app.py
   ```
5. Truy cập địa chỉ:
   ```
   http://127.0.0.1:5000
   ```
6. Tải lên 1 tệp → kiểm tra xem **CID** có được sinh ra không.  
7. Dán **CID** vào:
   ```
   https://ipfs.io/ipfs/<CID>
   ```
   để kiểm tra file trên mạng IPFS.

---

## 🧾 8. Ghi chú thêm

- Nếu IPFS không hoạt động, hãy kiểm tra **cổng 5001** có bị chặn bởi tường lửa không.  
- Nếu Flask báo lỗi `ModuleNotFoundError`, hãy chạy lại:
  ```bash
  pip install -r requirements.txt
  ```
- Dự án có thể mở rộng thêm phần **ghi nhận giao dịch CID lên Blockchain** (ví dụ **Ethereum Testnet**) để minh họa quá trình lưu vết dữ liệu.

---

## 🔮 9. Hướng phát triển tương lai

- 🌍 Tích hợp **Ethereum hoặc Polygon Testnet** để lưu CID lên blockchain thực.  
- 🧱 Xây dựng **giao diện quản lý lịch sử tải lên**, cho phép tra cứu CID theo người dùng.  
- 🔐 Bổ sung **xác thực người dùng (Flask-Login)** để phân quyền upload/download.  
- 📊 Thêm **dashboard thống kê** dung lượng và số file lưu trữ.

---

## ❤️ Tác giả & Đóng góp

**Tác giả:** [codingBeast25](https://github.com/codingBeast25)  
**Người biên tập README:** *Tùng Chu (2025)*  

Nếu bạn thấy dự án hữu ích, hãy ⭐ nó trên GitHub để ủng hộ nhé!

---

## 📜 Giấy phép

Dự án được phân phối dưới **Giấy phép MIT License**.  
Bạn có thể sử dụng, chỉnh sửa và mở rộng cho mục đích học tập hoặc nghiên cứu.

---
