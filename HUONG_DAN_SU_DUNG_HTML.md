# Hướng Dẫn Sử Dụng File HTML

## 📄 File HTML: `DOCUMENTATION.html`

File HTML này hiển thị toàn bộ tài liệu Jira dưới dạng web với:
- ✅ Mindmap cấu trúc (Mermaid)
- ✅ Navigation menu theo thứ tự đọc
- ✅ Nội dung đầy đủ tất cả các file markdown
- ✅ Styling đẹp, responsive
- ✅ Tìm kiếm và điều hướng dễ dàng

## 🚀 Cách Sử Dụng

### ⭐ Cách 1: Sử dụng file HTML Standalone (KHUYẾN NGHỊ - Dễ nhất)

**File `DOCUMENTATION_STANDALONE.html` đã được tạo sẵn với tất cả nội dung được embed!**

1. Mở file `DOCUMENTATION_STANDALONE.html` bằng trình duyệt web (double-click)
2. File sẽ hiển thị ngay lập tức, không cần file bổ sung
3. ✅ Hoạt động độc lập, không cần internet (trừ Mermaid.js và marked.js từ CDN)

**Nếu file chưa tồn tại, chạy lệnh:**
```bash
python3 generate_standalone_html.py
```

### Cách 2: Sử dụng với file JS

1. Đảm bảo file `content_data.js` nằm cùng thư mục với `DOCUMENTATION.html`
2. Mở file `DOCUMENTATION.html` bằng trình duyệt web
3. File sẽ tự động load nội dung từ `content_data.js`

**Nếu file `content_data.js` chưa tồn tại, nó đã được tạo tự động khi chạy script.**

### Cách 3: Sử dụng với local server (Nếu cách 1, 2 không hoạt động)

1. Mở terminal trong thư mục chứa file HTML
2. Chạy một trong các lệnh sau:

**Python 3:**
```bash
python3 -m http.server 8000
```

**Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Node.js (nếu có http-server):**
```bash
npx http-server -p 8000
```

3. Mở trình duyệt và truy cập: `http://localhost:8000/DOCUMENTATION_STANDALONE.html`

## 📋 Tính Năng

### Navigation Menu
- **Bắt Đầu**: Giới thiệu và Mindmap
- **Cho Admin/Manager**: 8 tài liệu theo thứ tự đọc
- **Cho Users**: 5 tài liệu theo thứ tự đọc
- **Tham Khảo**: Các tài liệu tham khảo

### Thứ Tự Đọc
File HTML được tổ chức theo thứ tự đọc được đề xuất trong README:
- Cho Admin/Manager: 7 bước từ chọn phiên bản đến phân tích issue types
- Cho Users: 5 bước từ hướng dẫn member mới đến ITIL & Quản trị

### Mindmap
Mindmap hiển thị cấu trúc toàn bộ hệ thống Jira, giúp hiểu tổng quan nhanh chóng.

## 🔧 Troubleshooting

### File không hiển thị nội dung?

**Nếu dùng DOCUMENTATION_STANDALONE.html:**
- File này đã có sẵn tất cả nội dung, không cần file bổ sung
- Nếu không hiển thị, kiểm tra console của trình duyệt (F12) để xem lỗi
- Đảm bảo trình duyệt hỗ trợ JavaScript

**Nếu dùng DOCUMENTATION.html:**
- Kiểm tra file `content_data.js` có tồn tại không
- Kiểm tra console của trình duyệt (F12) để xem lỗi
- Thử sử dụng file `DOCUMENTATION_STANDALONE.html` thay thế
- Hoặc thử sử dụng local server (Cách 3)

### Mindmap không hiển thị?
- Kiểm tra kết nối internet (Mermaid.js được load từ CDN)
- Thử refresh trang

### Styling không đúng?
- Đảm bảo trình duyệt hỗ trợ CSS3
- Thử trình duyệt khác (Chrome, Firefox, Safari, Edge)

## 📝 Lưu Ý

- File HTML sử dụng các thư viện từ CDN (marked.js, mermaid.js), cần kết nối internet
- File `content_data.json` được tạo tự động từ các file markdown
- Nếu cập nhật các file markdown, cần tạo lại `content_data.json`

## ✅ Checklist

**Cho DOCUMENTATION_STANDALONE.html (Khuyến nghị):**
- [x] File `DOCUMENTATION_STANDALONE.html` tồn tại (đã được tạo tự động)
- [ ] Trình duyệt hỗ trợ JavaScript
- [ ] Có kết nối internet (để load Mermaid.js và marked.js từ CDN)

**Cho DOCUMENTATION.html:**
- [ ] File `DOCUMENTATION.html` tồn tại
- [ ] File `content_data.js` tồn tại (hoặc sử dụng local server)
- [ ] Trình duyệt hỗ trợ JavaScript
- [ ] Có kết nối internet (để load Mermaid.js và marked.js)

---

**Chúc bạn sử dụng tài liệu hiệu quả! 🚀**
