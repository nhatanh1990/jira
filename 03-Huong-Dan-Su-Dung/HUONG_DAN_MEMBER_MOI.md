# HƯỚNG DẪN CHO THÀNH VIÊN MỚI - JIRA SYSTEM

Chào mừng bạn đến với hệ thống Jira! Tài liệu này sẽ hướng dẫn bạn các bước đầu tiên để sử dụng Jira hiệu quả.

---

## 📋 MỤC LỤC

1. [Bắt đầu](#1-bắt-đầu)
2. [Hiểu về Jira](#2-hiểu-về-jira)
3. [Hướng dẫn theo Role](#3-hướng-dẫn-theo-role)
4. [Các thao tác cơ bản](#4-các-thao-tác-cơ-bản)
5. [Effort Tracking](#5-effort-tracking)
6. [Tips & Best Practices](#6-tips--best-practices)
7. [FAQ](#7-faq)

---

## 1. BẮT ĐẦU

### 1.1. Đăng nhập

1. Truy cập URL Jira của công ty (ví dụ: `https://jira.company.com`)
2. Đăng nhập bằng tài khoản được cấp
3. Nếu chưa có tài khoản, liên hệ Jira Admin

### 1.2. Làm quen với giao diện

**Các thành phần chính**:
- **Top Navigation**: Menu chính (Projects, Dashboards, Issues, etc.)
- **Sidebar**: Quick links, filters
- **Main Content**: Danh sách issues, dashboards, etc.

**Dashboard mặc định**:
- Khi đăng nhập, bạn sẽ thấy Dashboard
- Dashboard hiển thị issues được assign cho bạn, issues bạn đang theo dõi, etc.

### 1.3. Cấu hình profile

1. Click vào avatar (góc trên bên phải) → **Profile**
2. Cập nhật thông tin:
   - Avatar
   - Email
   - Timezone
   - Language
3. Cấu hình notifications:
   - Email notifications
   - In-app notifications

---

## 2. HIỂU VỀ JIRA

### 2.1. Các khái niệm cơ bản

**Project**: 
- Một project là nơi chứa các issues
- Ví dụ: "Product A", "Internal Tools", "Support"

**Issue**:
- Một issue là một công việc, task, bug, hoặc request
- Có nhiều loại issue: Epic, Story, Task, Bug, Incident, Change Request, etc.

**Workflow**:
- Workflow mô tả các trạng thái (status) mà issue có thể chuyển qua
- Ví dụ: To Do → In Progress → Done

**Status**:
- Trạng thái hiện tại của issue
- Ví dụ: To Do, In Progress, Done, Closed

**Assignee**:
- Người được gán để làm issue đó
- Có thể là bạn hoặc người khác

**Reporter**:
- Người tạo issue

### 2.2. Các loại Issue Types

**Agile Issue Types**:
- **Epic**: Tính năng lớn, chứa nhiều Story
- **Story**: Yêu cầu chức năng từ góc độ người dùng
- **Task**: Công việc cụ thể cần thực hiện
- **Bug**: Lỗi cần được sửa

**ITIL Issue Types**:
- **Incident**: Sự cố cần xử lý
- **Change Request**: Yêu cầu thay đổi hệ thống
- **Service Request**: Yêu cầu dịch vụ
- **Service Order**: Đơn hàng dịch vụ

### 2.3. Custom Fields quan trọng

**Effort Tracking Fields**:
- **Research Effort**: Công sức nghiên cứu (hours)
- **Development Effort**: Công sức phát triển (hours)
- **Testing Effort**: Công sức testing (hours)
- **Deployment Effort**: Công sức triển khai (hours)
- **Operations Effort**: Công sức vận hành (hours)
- **Review Effort**: Công sức review (hours)
- **Documentation Effort**: Công sức documentation (hours)
- **Coordination Effort**: Công sức coordination (hours)
- **Total Effort**: Tổng effort (tự động tính)

**Classification Fields**:
- **Work Type**: Product, Project, Support, ITIL
- **Phase**: Research, Development, Testing, Deployment, Operations
- **Customer**: Khách hàng (cho Project issues)

---

## 3. HƯỚNG DẪN THEO ROLE

### 3.1. Developer

#### Công việc hàng ngày:

1. **Xem issues được assign**:
   - Vào Dashboard → **My Open Issues**
   - Hoặc: Issues → **Assigned to Me**

2. **Bắt đầu làm việc**:
   - Mở issue (Story/Task/Bug)
   - Đọc Description và Acceptance Criteria
   - Transition: **To Do → In Progress**

3. **Log effort**:
   - Khi làm việc, log effort vào issue
   - Click **Log Work** → Điền effort theo phase
   - Ví dụ: Development Effort = 4 hours

4. **Tạo GitLab branch** (nếu có integration):
   - Click **Create Branch** trên issue
   - Branch sẽ tự động link với issue

5. **Tạo Merge Request**:
   - Sau khi code xong, tạo MR trên GitLab
   - Link MR vào Jira issue (comment hoặc link field)

6. **Chuyển status**:
   - Sau khi tạo MR → Transition: **In Progress → Code Review**
   - Sau khi code được review → Transition: **Code Review → Testing**

#### Best Practices:
- ✅ Luôn log effort khi làm việc
- ✅ Update status thường xuyên
- ✅ Comment khi có thay đổi quan trọng
- ✅ Link MR với issue

---

### 3.2. QA/Tester

#### Công việc hàng ngày:

1. **Xem issues cần test**:
   - Vào Dashboard → **Issues in Testing**
   - Hoặc filter: `status = "Testing"`

2. **Test issue**:
   - Mở Story/Bug
   - Đọc Acceptance Criteria
   - Test theo criteria
   - Ghi lại kết quả test

3. **Tạo Bug nếu có lỗi**:
   - Click **Create Issue** → **Bug**
   - Điền thông tin:
     - Summary: Mô tả ngắn gọn
     - Description: Chi tiết
     - Steps to Reproduce: Các bước để reproduce
     - Priority: High/Medium/Low
   - Link Bug với Story gốc

4. **Log testing effort**:
   - Vào Story → **Log Work**
   - **Testing Effort**: Số giờ test

5. **Chuyển status**:
   - Nếu pass → Transition: **Testing → Ready for Release**
   - Nếu fail → Transition: **Testing → In Progress** (để Developer fix)

#### Best Practices:
- ✅ Test kỹ theo Acceptance Criteria
- ✅ Ghi lại kết quả test rõ ràng
- ✅ Tạo Bug với đầy đủ thông tin
- ✅ Log testing effort

---

### 3.3. Product Owner

#### Công việc hàng ngày:

1. **Tạo Epic và Story**:
   - Vào Project → **Create Issue**
   - Chọn **Epic** hoặc **Story**
   - Điền thông tin đầy đủ:
     - Summary, Description
     - Acceptance Criteria (cho Story)
     - Story Points (cho Story)
     - Work Type, Phase

2. **Quản lý Backlog**:
   - Vào Project → **Backlog**
   - Sắp xếp priority
   - Gán Story cho Developer

3. **Review và Approve**:
   - Review Story ở status "Ready for Release"
   - Approve hoặc request changes
   - Transition: **Ready for Release → Done**

4. **Xem Dashboards**:
   - Vào Dashboard → **Product Owner Dashboard**
   - Xem progress, effort, velocity

#### Best Practices:
- ✅ Viết Acceptance Criteria rõ ràng
- ✅ Gán Story Points hợp lý
- ✅ Review thường xuyên
- ✅ Track effort của Epic

---

### 3.4. Support

#### Công việc hàng ngày:

1. **Tạo Service Request**:
   - Vào Project → **Create Issue** → **Service Request**
   - Điền thông tin:
     - Summary: Yêu cầu của khách hàng
     - Description: Chi tiết
     - Requestor: Khách hàng
     - Priority

2. **Xử lý Service Request**:
   - Transition: **New → In Progress**
   - Thực hiện yêu cầu
   - Log effort: **Operations Effort**

3. **Tạo Incident** (nếu có sự cố):
   - Vào Project → **Create Issue** → **Incident**
   - Điền thông tin:
     - Summary: Mô tả sự cố
     - Severity: SEV1/SEV2/SEV3/SEV4
     - Priority
     - Affected Users

4. **Xử lý Incident**:
   - Transition: **New → Acknowledged → Investigating**
   - Tìm nguyên nhân
   - Giải quyết
   - Transition: **Investigating → Resolved → Closed**

#### Best Practices:
- ✅ Phản hồi nhanh chóng
- ✅ Log effort đầy đủ
- ✅ Update status thường xuyên
- ✅ Comment khi có thay đổi

---

### 3.5. SRE/DevOps

#### Công việc hàng ngày:

1. **Xử lý Incident SEV1/SEV2**:
   - Nhận Incident từ Support hoặc monitoring
   - Transition: **New → Investigating**
   - Tìm root cause
   - Mitigate/Resolve
   - Log effort

2. **Xử lý Change Request**:
   - Review Change Request
   - Approve (nếu là deployment)
   - Implement change
   - Transition: **Approved → Implementation → Completed**

3. **Deploy**:
   - Chạy GitLab pipeline
   - Monitor deployment
   - Log deployment effort

#### Best Practices:
- ✅ Ưu tiên Incident SEV1
- ✅ Log effort đầy đủ
- ✅ Document root cause
- ✅ Follow change management process

---

## 4. CÁC THAO TÁC CƠ BẢN

### 4.1. Tạo Issue

1. Vào Project → Click **Create** (góc trên bên phải)
2. Chọn Issue Type
3. Điền thông tin:
   - **Summary**: Tiêu đề (bắt buộc)
   - **Description**: Mô tả chi tiết
   - **Assignee**: Người được gán (có thể để trống)
   - **Priority**: Độ ưu tiên
   - **Custom Fields**: Work Type, Phase, etc.
4. Click **Create**

### 4.2. Tìm Issue

**Cách 1: Quick Search**:
- Click vào search box (top navigation)
- Gõ issue key (ví dụ: PROJ-123) hoặc summary

**Cách 2: Advanced Search (JQL)**:
- Click **Issues** → **Search for issues**
- Sử dụng JQL:
  ```
  project = PROJ AND assignee = currentUser() AND status != Done
  ```

**Cách 3: Filters**:
- Vào **Issues** → **My Filters**
- Sử dụng filter có sẵn hoặc tạo filter mới

### 4.3. Chuyển Status (Transition)

1. Mở issue
2. Click **Workflow** (góc trên bên phải)
3. Chọn status mới
4. Điền thông tin (nếu cần):
   - Comment
   - Assignee (nếu cần thay đổi)
5. Click **Transition**

### 4.4. Comment

1. Mở issue
2. Scroll xuống phần **Comments**
3. Gõ comment
4. Click **Add**

**Tips**:
- Sử dụng @mention để tag người khác: `@username`
- Attach files nếu cần

### 4.5. Attach Files

1. Mở issue
2. Click **Attach** (góc trên bên phải)
3. Chọn file
4. Click **Attach**

### 4.6. Link Issues

1. Mở issue
2. Scroll xuống phần **Linked Issues**
3. Click **Link**
4. Chọn link type (Relates, Blocks, etc.)
5. Tìm issue cần link
6. Click **Link**

---

## 5. EFFORT TRACKING

### 5.1. Tại sao cần log effort?

- ✅ Track công sức thực tế
- ✅ Đánh giá performance
- ✅ Planning chính xác hơn
- ✅ Báo cáo cho management

### 5.2. Cách log effort

1. Mở issue
2. Click **Log Work** (góc trên bên phải)
3. Điền thông tin:
   - **Time Spent**: Số giờ (ví dụ: 4h, 2h 30m)
   - **Date**: Ngày làm việc
   - **Effort Fields**: Chọn effort type
     - Research Effort
     - Development Effort
     - Testing Effort
     - Deployment Effort
     - Operations Effort
     - Review Effort
     - Documentation Effort
     - Coordination Effort
4. Click **Log**

### 5.3. Ví dụ log effort

**Developer làm Story**:
- Day 1: Research Effort = 2h (nghiên cứu API)
- Day 2: Development Effort = 4h (code)
- Day 3: Development Effort = 2h (code tiếp)
- Day 3: Review Effort = 1h (code review)
- Day 4: Testing Effort = 1h (unit test)

**Total Effort**: 10 hours (tự động tính)

### 5.4. Best Practices

- ✅ Log effort hàng ngày (không để cuối tuần)
- ✅ Log chính xác (không làm tròn quá nhiều)
- ✅ Phân chia effort theo phase
- ✅ Log cả coordination effort (meetings, standups)

---

## 6. TIPS & BEST PRACTICES

### 6.1. General Tips

**Viết Summary rõ ràng**:
- ❌ Bad: "Fix bug"
- ✅ Good: "Fix login error when user enters special characters"

**Viết Description đầy đủ**:
- Mô tả chi tiết
- Steps to reproduce (cho Bug)
- Expected vs Actual behavior (cho Bug)
- Acceptance Criteria (cho Story)

**Update status thường xuyên**:
- Không để issue ở một status quá lâu
- Update khi có thay đổi

**Comment khi cần**:
- Comment khi có thay đổi quan trọng
- Comment khi cần hỏi/trả lời
- Sử dụng @mention để tag người khác

### 6.2. Workflow Tips

**Follow workflow**:
- Không skip steps
- Chuyển status đúng thứ tự

**Assign đúng người**:
- Gán issue cho người có khả năng xử lý
- Unassign nếu không thể xử lý

### 6.3. Effort Tracking Tips

**Log effort thường xuyên**:
- Log hàng ngày, không để cuối tuần
- Log chính xác, không làm tròn

**Phân chia effort đúng**:
- Research Effort: Nghiên cứu, đọc docs
- Development Effort: Code, implement
- Testing Effort: Test, QA
- Review Effort: Code review, design review
- Documentation Effort: Viết docs
- Coordination Effort: Meetings, standups

### 6.4. Communication Tips

**Sử dụng @mention**:
- `@username` để tag người khác
- Họ sẽ nhận notification

**Sử dụng emoji** (nếu phù hợp):
- ✅ Done
- ⚠️ Warning
- ❌ Blocked
- 🔄 In Progress

---

## 7. FAQ

### Q1: Tôi không thấy issue được assign cho tôi?

**A**: 
- Kiểm tra filter: Có thể đang filter theo project khác
- Kiểm tra Dashboard: Vào "My Open Issues"
- Liên hệ Jira Admin nếu vẫn không thấy

### Q2: Tôi không thể chuyển status?

**A**:
- Kiểm tra permissions: Bạn có quyền transition không?
- Kiểm tra workflow: Status hiện tại có thể transition sang status đó không?
- Liên hệ Jira Admin nếu cần

### Q3: Tôi không thấy field "Effort"?

**A**:
- Kiểm tra issue type: Một số issue types có thể không có effort fields
- Kiểm tra screen: Field có thể bị ẩn
- Liên hệ Jira Admin nếu cần

### Q4: Làm sao để tìm issue cũ?

**A**:
- Sử dụng Advanced Search (JQL):
  ```
  project = PROJ AND created >= -30d
  ```
- Sử dụng filters
- Vào Project → Issues → Tất cả issues

### Q5: Tôi muốn nhận email notification?

**A**:
1. Click avatar → **Profile**
2. Vào **Email Preferences**
3. Cấu hình notifications

### Q6: Làm sao để tạo filter?

**A**:
1. Vào **Issues** → **Search for issues**
2. Tạo JQL query
3. Click **Save as** → Đặt tên filter
4. Filter sẽ xuất hiện trong "My Filters"

### Q7: Tôi muốn xem dashboard của team?

**A**:
- Vào **Dashboards** → Chọn dashboard
- Hoặc vào Project → **Dashboards**

### Q8: Làm sao để link GitLab MR với Jira issue?

**A**:
- Nếu có GitLab integration: MR sẽ tự động link khi bạn mention issue key trong MR description
- Hoặc: Comment trên issue với link MR

---

## 📞 HỖ TRỢ

Nếu bạn có câu hỏi hoặc cần hỗ trợ:

1. **Xem tài liệu**: Đọc các file markdown trong project
2. **Hỏi team**: Hỏi đồng nghiệp hoặc team lead
3. **Liên hệ Jira Admin**: Nếu cần quyền hoặc cấu hình

---

## ✅ CHECKLIST CHO THÀNH VIÊN MỚI

- [ ] Đã đăng nhập và làm quen với giao diện
- [ ] Đã cấu hình profile và notifications
- [ ] Đã đọc hướng dẫn theo role của mình
- [ ] Đã thử tạo issue
- [ ] Đã thử log effort
- [ ] Đã thử chuyển status
- [ ] Đã xem dashboard
- [ ] Đã đọc FAQ

---

**Chúc bạn sử dụng Jira hiệu quả! 🚀**
