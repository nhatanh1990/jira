# TROUBLESHOOTING & FAQ - JIRA SYSTEM

Tài liệu này giải đáp các câu hỏi thường gặp và hướng dẫn xử lý sự cố.

---

## 📋 MỤC LỤC

1. [FAQ - Câu hỏi thường gặp](#1-faq---câu-hỏi-thường-gặp)
2. [Troubleshooting - Xử lý sự cố](#2-troubleshooting---xử-lý-sự-cố)
3. [Best Practices](#3-best-practices)
4. [Performance Optimization](#4-performance-optimization)
5. [Security Considerations](#5-security-considerations)
6. [Backup & Recovery](#6-backup--recovery)

---

## 1. FAQ - CÂU HỎI THƯỜNG GẶP

### 1.1. General Questions

**Q: Tôi nên chọn phiên bản nào?**
- **A**: 
  - **Cơ Bản**: Team < 50 users, cần triển khai nhanh (3 tuần), yêu cầu đơn giản
  - **Nâng Cao**: Team > 100 users, có thể triển khai 3 tháng, yêu cầu đầy đủ ITIL + Quản trị
  - Xem [01-Phien-Ban/PHIEN_BAN_CO_BAN.md](../01-Phien-Ban/PHIEN_BAN_CO_BAN.md) và [01-Phien-Ban/PHIEN_BAN_NANG_CAO.md](../01-Phien-Ban/PHIEN_BAN_NANG_CAO.md)

**Q: Tại sao loại bỏ Product Research, Product Development, Project Deployment, Project Operations?**
- **A**: Các issue types này trùng lặp với Epic/Story/Task. Thay vào đó, sử dụng Epic/Story/Task với custom fields (Work Type, Phase, Customer). Xem [01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md](../01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md)

**Q: Làm sao để track effort cho Product Research?**
- **A**: Tạo Epic/Story với Work Type=Product, Phase=Research, sau đó log Research Effort. Xem [05-Effort-Tracking/EFFORT_TRACKING_HOAN_THIEN.md](../05-Effort-Tracking/EFFORT_TRACKING_HOAN_THIEN.md)

---

### 1.2. Effort Tracking Questions

**Q: Tại sao cần 8 effort fields?**
- **A**: Để track đầy đủ các phase: Research, Development, Testing, Deployment, Operations, Review, Documentation, Coordination. Giúp phân tích chính xác effort distribution.

**Q: Khi nào log effort?**
- **A**: Log effort hàng ngày, không để cuối tuần. Log chính xác, không làm tròn quá nhiều.

**Q: Total Effort được tính như thế nào?**
- **A**: Total Effort = Research + Development + Testing + Deployment + Operations + Review + Documentation + Coordination (tự động tính)

**Q: Epic effort được tính như thế nào?**
- **A**: Epic effort = Tổng effort của tất cả children issues (tự động tính)

---

### 1.3. Workflow Questions

**Q: Tôi không thể chuyển status?**
- **A**: 
  - Kiểm tra permissions: Bạn có quyền transition không?
  - Kiểm tra workflow: Status hiện tại có thể transition sang status đó không?
  - Kiểm tra conditions: Có điều kiện nào block không?
  - Liên hệ Jira Admin

**Q: Làm sao để skip một status trong workflow?**
- **A**: Không nên skip. Workflow được thiết kế để đảm bảo process đúng. Nếu cần, liên hệ Jira Admin để điều chỉnh workflow.

**Q: Tôi muốn thêm status mới?**
- **A**: Liên hệ Jira Admin. Cần đánh giá impact và update workflow.

---

### 1.4. Permission Questions

**Q: Tôi không thấy issue được assign cho tôi?**
- **A**: 
  - Kiểm tra filter: Có thể đang filter theo project khác
  - Kiểm tra Dashboard: Vào "My Open Issues"
  - Kiểm tra permissions: Bạn có quyền view project không?
  - Liên hệ Jira Admin

**Q: Tôi không thể edit issue?**
- **A**: 
  - Kiểm tra permissions: Bạn có quyền edit không?
  - Kiểm tra issue status: Một số status có thể restrict edit
  - Kiểm tra assignee: Bạn có phải assignee không?
  - Liên hệ Jira Admin

---

### 1.5. Integration Questions

**Q: GitLab integration không hoạt động?**
- **A**: 
  - Kiểm tra GitLab plugin đã được cài đặt chưa
  - Kiểm tra GitLab URL và token
  - Kiểm tra permissions
  - Xem logs trong Jira Admin

**Q: Làm sao để link MR với Jira issue?**
- **A**: 
  - Mention issue key trong MR description (ví dụ: PROJ-123)
  - Hoặc comment trên issue với link MR
  - Nếu có integration, MR sẽ tự động link

---

## 2. TROUBLESHOOTING - XỬ LÝ SỰ CỐ

### 2.1. Issue Creation Problems

**Problem**: Không thể tạo issue
- **Check**: 
  - Permissions (Create Issues)
  - Project active
  - Required fields
- **Solution**: 
  - Kiểm tra permissions
  - Liên hệ Jira Admin

**Problem**: Issue không hiển thị sau khi tạo
- **Check**: 
  - Filter settings
  - Project permissions
  - Issue visibility
- **Solution**: 
  - Clear filters
  - Kiểm tra permissions
  - Refresh page

---

### 2.2. Workflow Problems

**Problem**: Không thể transition
- **Check**: 
  - Permissions
  - Workflow conditions
  - Required fields
  - Validators
- **Solution**: 
  - Kiểm tra error message
  - Điền đầy đủ required fields
  - Liên hệ Jira Admin

**Problem**: Status không đúng
- **Check**: 
  - Workflow configuration
  - Automation rules
- **Solution**: 
  - Kiểm tra workflow
  - Liên hệ Jira Admin

---

### 2.3. Effort Tracking Problems

**Problem**: Total Effort không tự động tính
- **Check**: 
  - Automation rules
  - Calculated field configuration
- **Solution**: 
  - Kiểm tra automation rules
  - Liên hệ Jira Admin

**Problem**: Epic effort không cập nhật
- **Check**: 
  - Children issues có effort không
  - Automation rules
- **Solution**: 
  - Log effort cho children issues
  - Kiểm tra automation rules
  - Liên hệ Jira Admin

---

### 2.4. Performance Problems

**Problem**: Jira chạy chậm
- **Check**: 
  - Số lượng issues
  - JQL queries phức tạp
  - Dashboards có quá nhiều gadgets
  - Server resources
- **Solution**: 
  - Optimize JQL queries
  - Giảm số gadgets trong dashboard
  - Archive old issues
  - Liên hệ Jira Admin để kiểm tra server

**Problem**: Dashboard load chậm
- **Check**: 
  - Số lượng gadgets
  - JQL queries phức tạp
  - Data volume
- **Solution**: 
  - Giảm số gadgets
  - Optimize JQL queries
  - Sử dụng filters thay vì queries phức tạp

---

### 2.5. Integration Problems

**Problem**: GitLab integration không hoạt động
- **Check**: 
  - Plugin installed
  - GitLab URL và token
  - Network connectivity
  - Permissions
- **Solution**: 
  - Reinstall plugin
  - Update GitLab URL và token
  - Kiểm tra network
  - Liên hệ Jira Admin

---

## 3. BEST PRACTICES

### 3.1. Issue Creation

**DO**:
- ✅ Viết Summary rõ ràng, mô tả ngắn gọn
- ✅ Điền đầy đủ Description
- ✅ Viết Acceptance Criteria cho Story
- ✅ Gán đúng assignee
- ✅ Set priority phù hợp
- ✅ Sử dụng Labels và Components

**DON'T**:
- ❌ Tạo issue với Summary mơ hồ
- ❌ Bỏ trống Description
- ❌ Gán issue cho người không liên quan
- ❌ Set priority không đúng

---

### 3.2. Effort Tracking

**DO**:
- ✅ Log effort hàng ngày
- ✅ Log chính xác, không làm tròn quá nhiều
- ✅ Phân chia effort theo phase đúng
- ✅ Log cả coordination effort (meetings, standups)

**DON'T**:
- ❌ Để cuối tuần mới log
- ❌ Làm tròn quá nhiều
- ❌ Bỏ qua coordination effort
- ❌ Log effort không chính xác

---

### 3.3. Workflow

**DO**:
- ✅ Follow workflow đúng thứ tự
- ✅ Update status thường xuyên
- ✅ Comment khi có thay đổi quan trọng
- ✅ Assign đúng người

**DON'T**:
- ❌ Skip steps trong workflow
- ❌ Để issue ở một status quá lâu
- ❌ Không comment khi có thay đổi
- ❌ Assign cho người không liên quan

---

### 3.4. Communication

**DO**:
- ✅ Sử dụng @mention để tag người khác
- ✅ Comment khi cần hỏi/trả lời
- ✅ Update status khi có thay đổi
- ✅ Attach files khi cần

**DON'T**:
- ❌ Comment không cần thiết
- ❌ Không tag người liên quan
- ❌ Không update status
- ❌ Attach files quá lớn

---

## 4. PERFORMANCE OPTIMIZATION

### 4.1. JQL Queries

**Best Practices**:
- Sử dụng indexes fields (Project, Issue Type, Status, Assignee, etc.)
- Tránh functions phức tạp
- Limit kết quả (maxResults)
- Sử dụng filters thay vì queries phức tạp

**Example**:
```jql
# Good
project = PROJ AND status = "In Progress" AND assignee = currentUser()

# Bad
project = PROJ AND text ~ "test" AND updatedDate >= -30d
```

---

### 4.2. Dashboards

**Best Practices**:
- Giới hạn số gadgets (5-10 gadgets)
- Sử dụng filters thay vì queries phức tạp
- Cache results khi có thể
- Archive old data

---

### 4.3. Issues Management

**Best Practices**:
- Archive old issues (> 1 year)
- Close issues không cần thiết
- Sử dụng components và labels để organize
- Regular cleanup

---

## 5. SECURITY CONSIDERATIONS

### 5.1. Permissions

**Best Practices**:
- Principle of least privilege
- Regular review permissions
- Remove unused users
- Audit permissions định kỳ

---

### 5.2. Data Protection

**Best Practices**:
- Encrypt sensitive data
- Backup định kỳ
- Access control
- Audit logs

---

### 5.3. Integration Security

**Best Practices**:
- Sử dụng tokens thay vì passwords
- Rotate tokens định kỳ
- Limit integration permissions
- Monitor integration activities

---

## 6. BACKUP & RECOVERY

### 6.1. Backup Strategy

**Daily Backup**:
- Database backup
- Configuration backup
- Attachments backup

**Weekly Backup**:
- Full system backup
- Test restore

**Monthly Backup**:
- Archive old backups
- Review backup strategy

---

### 6.2. Recovery Procedures

**Data Recovery**:
1. Identify data loss
2. Determine backup point
3. Restore from backup
4. Verify data
5. Notify users

**Configuration Recovery**:
1. Export current configuration
2. Restore from backup
3. Verify configuration
4. Test system

---

## 📞 SUPPORT

Nếu bạn gặp vấn đề không được giải quyết trong tài liệu này:

1. **Xem tài liệu**: Đọc các file markdown trong project
2. **Hỏi team**: Hỏi đồng nghiệp hoặc team lead
3. **Liên hệ Jira Admin**: Nếu cần quyền hoặc cấu hình
4. **Log issue**: Tạo issue trong Jira để track

---

**Tài liệu này sẽ được cập nhật thường xuyên dựa trên feedback và issues mới.**
