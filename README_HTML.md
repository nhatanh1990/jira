# 📄 File HTML Documentation

## ⚡ Sử Dụng Nhanh

**Mở file `DOCUMENTATION_STANDALONE.html` bằng trình duyệt web (double-click)**

File này đã chứa sẵn TẤT CẢ nội dung, không cần file bổ sung!

---

## 📋 Các File HTML

### 1. DOCUMENTATION_STANDALONE.html ⭐ **KHUYẾN NGHỊ**
- ✅ Tất cả nội dung đã được embed trực tiếp
- ✅ Không cần file bổ sung
- ✅ Hoạt động độc lập
- ✅ Kích thước: ~315KB

**Cách dùng:** Double-click để mở bằng trình duyệt

### 2. DOCUMENTATION.html
- Cần file `content_data.js` cùng thư mục
- File nhẹ hơn (~22KB)
- Cần tạo lại `content_data.js` nếu cập nhật markdown

**Cách dùng:** 
1. Đảm bảo `content_data.js` tồn tại
2. Mở `DOCUMENTATION.html` bằng trình duyệt

---

## 🔄 Tạo Lại File HTML

Nếu bạn cập nhật các file markdown và muốn tạo lại file HTML:

```bash
python3 generate_standalone_html.py
```

Script sẽ:
- Đọc tất cả 19 file markdown
- Tạo file `DOCUMENTATION_STANDALONE.html` mới
- Embed tất cả nội dung trực tiếp

---

## ✅ Kiểm Tra

Sau khi mở file HTML, bạn sẽ thấy:
- ✅ Navigation menu bên trái
- ✅ Mindmap cấu trúc
- ✅ Nội dung đầy đủ khi click vào các mục menu
- ✅ Styling đẹp, responsive

---

## 🆘 Nếu Không Hiển Thị

1. **Kiểm tra console (F12)** để xem lỗi
2. **Thử file DOCUMENTATION_STANDALONE.html** thay vì DOCUMENTATION.html
3. **Kiểm tra kết nối internet** (cần để load Mermaid.js và marked.js)
4. **Thử trình duyệt khác** (Chrome, Firefox, Safari, Edge)

---

**Xem chi tiết trong file `HUONG_DAN_SU_DUNG_HTML.md`**
