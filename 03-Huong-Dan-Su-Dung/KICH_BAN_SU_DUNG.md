# KỊCH BẢN SỬ DỤNG - JIRA SYSTEM

Tài liệu này mô tả các kịch bản sử dụng thực tế cho từng role trong hệ thống Jira.

---

## MỤC LỤC

1. [Kịch bản Agile/Development](#1-kịch-bản-agiledevelopment)
2. [Kịch bản ITIL/Service Management](#2-kịch-bản-itilservice-management)
3. [Kịch bản Effort Tracking](#3-kịch-bản-effort-tracking)
4. [Kịch bản Product Lifecycle](#4-kịch-bản-product-lifecycle)
5. [Kịch bản Project Deployment](#5-kịch-bản-project-deployment)
6. [Kịch bản Incident Response](#6-kịch-bản-incident-response)
7. [Kịch bản Change Management](#7-kịch-bản-change-management)

---

## 1. KỊCH BẢN AGILE/DEVELOPMENT

### 1.1. Product Owner - Tạo Epic và Story

**Kịch bản**: PO cần tạo Epic cho tính năng mới "AI Chatbot Integration"

**Bước thực hiện**:
1. **Tạo Epic**:
 - Vào Project → Create Issue → Chọn **Epic**
 - Điền thông tin:
 - **Summary**: "AI Chatbot Integration"
 - **Description**: "Tích hợp AI chatbot vào hệ thống để hỗ trợ khách hàng tự động"
 - **Work Type**: Product
 - **Phase**: Development
 - **Business Value**: 8/10
 - **Target Release**: Q2 2024
 - Click **Create**

2. **Tạo Story từ Epic**:
 - Vào Epic vừa tạo → Click **Create Sub-task** hoặc **Create Issue in Epic**
 - Chọn **Story**
 - Điền thông tin:
 - **Summary**: "As a user, I want to chat with AI bot to get product information"
 - **Epic Link**: Link đến Epic "AI Chatbot Integration"
 - **Story Points**: 5
 - **Work Type**: Product
 - **Phase**: Development
 - **Acceptance Criteria**:
 - User có thể mở chat window
 - Bot trả lời câu hỏi về sản phẩm
 - Bot có thể chuyển sang human agent nếu cần
 - Click **Create**

3. **Gán Story cho Developer**:
 - Vào Story → Click **Assign** → Chọn Developer
 - Transition: **To Do → In Progress**

**Kết quả**: Epic và Story đã được tạo, Developer có thể bắt đầu làm việc.

---

### 1.2. Developer - Phát triển Story

**Kịch bản**: Developer nhận Story và bắt đầu phát triển

**Bước thực hiện**:
1. **Nhận Story**:
 - Vào Dashboard → **My Open Issues**
 - Tìm Story được assign
 - Đọc **Description** và **Acceptance Criteria**

2. **Bắt đầu làm việc**:
 - Transition: **To Do → In Progress**
 - Tạo GitLab branch từ Jira:
 - Click **Create Branch** (nếu có GitLab integration)
 - Branch name: `feature/PROJ-123-ai-chatbot-integration`
 - Bắt đầu coding

3. **Log Effort**:
 - Vào Story → Click **Log Work**
 - Điền:
 - **Development Effort**: 4 hours
 - **Research Effort**: 1 hour (nghiên cứu API)
 - **Date**: Hôm nay
 - Click **Log**

4. **Tạo Merge Request**:
 - Sau khi code xong, tạo MR trên GitLab
 - Link MR vào Jira Story (comment hoặc link field)
 - Transition: **In Progress → Code Review**

**Kết quả**: Code đã được review, sẵn sàng cho testing.

---

### 1.3. QA/Tester - Test Story

**Kịch bản**: QA nhận Story ở trạng thái "Code Review" và bắt đầu test

**Bước thực hiện**:
1. **Nhận Story để test**:
 - Vào Dashboard → **Issues in Testing**
 - Tìm Story cần test
 - Đọc **Acceptance Criteria**

2. **Test Story**:
 - Test theo Acceptance Criteria
 - Ghi lại kết quả test
 - Nếu có bug → Tạo Bug issue:
 - Click **Create Issue** → **Bug**
 - **Summary**: "Chatbot không trả lời khi user gõ tiếng Việt"
 - **Priority**: High
 - **Linked Issues**: Link đến Story gốc
 - **Steps to Reproduce**: ...
 - Transition Story: **Code Review → Testing**

3. **Log Testing Effort**:
 - Vào Story → **Log Work**
 - **Testing Effort**: 2 hours
 - Click **Log**

4. **Hoàn thành test**:
 - Nếu pass → Transition: **Testing → Ready for Release**
 - Nếu fail → Transition: **Testing → In Progress** (để Developer fix)

**Kết quả**: Story đã được test, sẵn sàng release hoặc cần fix bug.

---

### 1.4. Developer - Fix Bug

**Kịch bản**: Developer nhận Bug và fix

**Bước thực hiện**:
1. **Nhận Bug**:
 - Vào Dashboard → **My Open Issues** → Filter: **Type = Bug**
 - Đọc **Description** và **Steps to Reproduce**

2. **Fix Bug**:
 - Transition: **To Do → In Progress**
 - Tạo branch: `bugfix/PROJ-456-chatbot-vietnamese-support`
 - Fix code
 - Log effort:
 - **Research Effort**: 0.5 hours (tìm nguyên nhân)
 - **Development Effort**: 1 hour (fix code)
 - **Testing Effort**: 0.5 hours (test fix)

3. **Tạo MR và Review**:
 - Tạo MR
 - Transition: **In Progress → Code Review**

4. **Sau khi review**:
 - Transition: **Code Review → Testing** (để QA verify fix)

**Kết quả**: Bug đã được fix và verify.

---

## 2. KỊCH BẢN ITIL/SERVICE MANAGEMENT

### 2.1. Support - Xử lý Service Request

**Kịch bản**: Khách hàng yêu cầu tạo tài khoản mới

**Bước thực hiện**:
1. **Tạo Service Request**:
 - Vào Project → **Create Issue** → **Service Request**
 - Điền thông tin:
 - **Summary**: "Tạo tài khoản mới cho khách hàng ABC Company"
 - **Description**: "Khách hàng cần tài khoản với quyền Admin"
 - **Requestor**: Chọn customer/user
 - **Priority**: Medium
 - **Work Type**: Support
 - Click **Create**

2. **Xử lý Request**:
 - Transition: **New → In Progress**
 - Thực hiện tạo tài khoản
 - Log effort:
 - **Operations Effort**: 0.5 hours
 - **Coordination Effort**: 0.25 hours (liên hệ với customer)

3. **Hoàn thành**:
 - Transition: **In Progress → Fulfilled**
 - Comment: "Tài khoản đã được tạo, thông tin đăng nhập đã gửi email"
 - Transition: **Fulfilled → Closed**

**Kết quả**: Service Request đã được xử lý và đóng.

---

### 2.2. Support - Tạo Incident (SEV2)

**Kịch bản**: Khách hàng báo lỗi không đăng nhập được (SEV2 - Medium)

**Bước thực hiện**:
1. **Tạo Incident**:
 - Vào Project → **Create Issue** → **Incident**
 - Điền thông tin:
 - **Summary**: "Khách hàng không đăng nhập được vào hệ thống"
 - **Severity**: SEV2
 - **Priority**: High
 - **Affected Users**: 5 users
 - **Description**: "Khách hàng báo lỗi khi đăng nhập, hiển thị 'Invalid credentials'"
 - Click **Create**

2. **Xử lý Incident**:
 - Transition: **New → Acknowledged**
 - Comment: "Đã nhận incident, đang kiểm tra"
 - Transition: **Acknowledged → Investigating**
 - Log effort:
 - **Research Effort**: 1 hour (kiểm tra logs, database)
 - **Operations Effort**: 0.5 hours (kiểm tra hệ thống)

3. **Giải quyết**:
 - Tìm nguyên nhân: "Password expired"
 - Giải pháp: "Reset password cho user"
 - Transition: **Investigating → Resolved**
 - Comment: "Đã reset password, user có thể đăng nhập lại"

4. **Đóng Incident**:
 - Sau khi user xác nhận → Transition: **Resolved → Closed**

**Kết quả**: Incident đã được giải quyết.

---

### 2.3. SRE/DevOps - Xử lý Incident SEV1

**Kịch bản**: Hệ thống production down (SEV1 - Critical)

**Bước thực hiện**:
1. **Nhận Incident SEV1**:
 - Alert từ monitoring system
 - Tạo Incident (hoặc nhận từ Support):
 - **Summary**: "Production system down - All services unavailable"
 - **Severity**: SEV1
 - **Priority**: Highest
 - **Affected Users**: All users

2. **Xử lý ngay lập tức**:
 - Transition: **New → Investigating** (bỏ qua Acknowledged)
 - Kiểm tra:
 - Server status
 - Database connection
 - Application logs
 - Log effort:
 - **Research Effort**: 0.5 hours (tìm nguyên nhân)
 - **Operations Effort**: 1 hour (xử lý)

3. **Mitigate**:
 - Nếu tìm thấy nguyên nhân → Transition: **Investigating → Mitigated**
 - Comment: "Đã restart service, hệ thống đang hoạt động lại"
 - Monitor hệ thống

4. **Resolve**:
 - Sau khi hệ thống ổn định → Transition: **Mitigated → Resolved**
 - Comment: "Root cause: Database connection pool exhausted. Đã tăng pool size"

5. **Post-Incident Review**:
 - Tạo Problem issue để phân tích root cause sâu hơn (nếu cần)
 - Đóng Incident: **Resolved → Closed**

**Kết quả**: Incident SEV1 đã được xử lý, hệ thống hoạt động bình thường.

---

### 2.4. Change Request - Deploy Feature mới

**Kịch bản**: Deploy tính năng AI Chatbot lên production

**Bước thực hiện**:
1. **Tạo Change Request**:
 - Vào Project → **Create Issue** → **Change Request**
 - Điền thông tin:
 - **Summary**: "Deploy AI Chatbot feature to production"
 - **Change Type**: Normal
 - **Change Category**: Application
 - **Risk Level**: Medium
 - **Implementation Plan**: "Deploy via GitLab pipeline, run smoke tests"
 - **Rollback Plan**: "Rollback to previous version nếu có lỗi"
 - **Implementation Date**: Chọn ngày deploy
 - Click **Create**

2. **Submit for Approval**:
 - Transition: **Draft → Submitted**
 - CAB sẽ review

3. **CAB Approval**:
 - CAB member review Change Request
 - Nếu approve → Transition: **Submitted → Approved**
 - Comment: "Approved. Deploy during maintenance window"

4. **Implementation**:
 - SRE/DevOps thực hiện deploy:
 - Transition: **Approved → Implementation**
 - Chạy GitLab pipeline
 - Monitor deployment
 - Log effort:
 - **Deployment Effort**: 1 hour
 - **Testing Effort**: 0.5 hours (smoke tests)

5. **Complete**:
 - Nếu thành công → Transition: **Implementation → Completed**
 - Post-Implementation Review: "Deployment successful, no issues"
 - Transition: **Completed → Closed**

**Kết quả**: Change đã được deploy thành công.

---

## 3. KỊCH BẢN EFFORT TRACKING

### 3.1. Developer - Log Effort đầy đủ

**Kịch bản**: Developer làm việc trên Story và cần log effort cho các phase khác nhau

**Bước thực hiện**:
1. **Research Phase**:
 - Đọc requirements, nghiên cứu API
 - Vào Story → **Log Work**
 - **Research Effort**: 2 hours
 - **Date**: Day 1

2. **Development Phase**:
 - Code implementation
 - **Log Work**:
 - **Development Effort**: 6 hours
 - **Date**: Day 2-3

3. **Review Phase**:
 - Code review với team
 - **Log Work**:
 - **Review Effort**: 1 hour
 - **Date**: Day 3

4. **Testing Phase**:
 - Unit testing, integration testing
 - **Log Work**:
 - **Testing Effort**: 2 hours
 - **Date**: Day 4

5. **Documentation Phase**:
 - Viết technical documentation
 - **Log Work**:
 - **Documentation Effort**: 1 hour
 - **Date**: Day 4

6. **Coordination Phase**:
 - Meetings, standups, planning
 - **Log Work**:
 - **Coordination Effort**: 1 hour
 - **Date**: Day 1-4

**Kết quả**: Total Effort = 13 hours, được track đầy đủ qua 8 effort fields.

---

### 3.2. Epic - Tổng hợp Effort từ Children

**Kịch bản**: PO muốn xem tổng effort của Epic

**Bước thực hiện**:
1. **Xem Epic**:
 - Vào Epic "AI Chatbot Integration"
 - Xem **Total Effort** field (auto-calculated từ children)

2. **Breakdown by Phase**:
 - **Total Research Effort**: 5 hours (từ các Story children)
 - **Total Development Effort**: 20 hours
 - **Total Testing Effort**: 8 hours
 - **Total Deployment Effort**: 2 hours
 - **Total Operations Effort**: 1 hour
 - **Total Review Effort**: 3 hours
 - **Total Documentation Effort**: 2 hours
 - **Total Coordination Effort**: 4 hours
 - **Total Effort**: 45 hours

3. **Effort Distribution**:
 - Research: 11%
 - Development: 44%
 - Testing: 18%
 - Deployment: 4%
 - Operations: 2%
 - Review: 7%
 - Documentation: 4%
 - Coordination: 9%

**Kết quả**: PO có cái nhìn tổng quan về effort của Epic.

---

## 4. KỊCH BẢN PRODUCT LIFECYCLE

### 4.1. Product Research - Nghiên cứu tính năng mới

**Kịch bản**: PO muốn nghiên cứu tính năng "AI Recommendation Engine"

**Bước thực hiện**:
1. **Tạo Epic cho Research**:
 - Vào Project → **Create Issue** → **Epic**
 - Điền thông tin:
 - **Summary**: "Research: AI Recommendation Engine"
 - **Work Type**: Product
 - **Phase**: Research
 - **Research Phase**: Market Research, User Research
 - Click **Create**

2. **Tạo Story cho Research Tasks**:
 - Tạo Story: "Research competitor solutions"
 - **Work Type**: Product
 - **Phase**: Research
 - Log effort:
 - **Research Effort**: 8 hours
 - **Documentation Effort**: 2 hours (ghi lại findings)

3. **Tạo Story cho User Research**:
 - Tạo Story: "Conduct user interviews"
 - Log effort:
 - **Research Effort**: 10 hours
 - **Coordination Effort**: 2 hours (schedule meetings)

4. **Tổng kết Research**:
 - Tạo Story: "Compile research findings"
 - Log effort:
 - **Research Effort**: 4 hours
 - **Documentation Effort**: 6 hours (viết research report)

**Kết quả**: Research đã hoàn thành, có đầy đủ findings để quyết định phát triển.

---

### 4.2. Product Development - Phát triển tính năng

**Kịch bản**: Phát triển tính năng "AI Recommendation Engine" sau khi research

**Bước thực hiện**:
1. **Tạo Epic cho Development**:
 - **Summary**: "Development: AI Recommendation Engine"
 - **Work Type**: Product
 - **Phase**: Development

2. **Tạo Stories**:
 - Story 1: "Design recommendation algorithm"
 - **Development Effort**: 8 hours
 - **Review Effort**: 2 hours
 - Story 2: "Implement recommendation API"
 - **Development Effort**: 16 hours
 - **Testing Effort**: 4 hours
 - Story 3: "Build recommendation UI"
 - **Development Effort**: 12 hours
 - **Testing Effort**: 3 hours

3. **Track Effort**:
 - Developers log effort khi làm việc
 - Epic tự động tổng hợp effort từ children

**Kết quả**: Tính năng đã được phát triển với effort tracking đầy đủ.

---

## 5. KỊCH BẢN PROJECT DEPLOYMENT

### 5.1. Project Deployment - Triển khai cho khách hàng

**Kịch bản**: Triển khai hệ thống cho khách hàng ABC Company

**Bước thực hiện**:
1. **Tạo Epic cho Project**:
 - Vào Project → **Create Issue** → **Epic**
 - Điền thông tin:
 - **Summary**: "Deploy system for ABC Company"
 - **Work Type**: Project
 - **Phase**: Deployment
 - **Customer**: ABC Company (User Picker)

2. **Tạo Stories/Tasks cho Deployment**:
 - Task 1: "Setup infrastructure"
 - **Work Type**: Project
 - **Phase**: Deployment
 - **Deployment Phase**: Setup
 - **Deployment Effort**: 4 hours
 - Task 2: "Data migration"
 - **Deployment Effort**: 8 hours
 - **Operations Effort**: 2 hours (backup)
 - Task 3: "User training"
 - **Deployment Effort**: 4 hours
 - **Coordination Effort**: 2 hours (schedule training)

3. **Go-live**:
 - Task 4: "Go-live support"
 - **Deployment Effort**: 2 hours
 - **Operations Effort**: 4 hours (monitoring)

**Kết quả**: Project đã được triển khai thành công cho khách hàng.

---

### 5.2. Project Operations - Vận hành project

**Kịch bản**: Vận hành và support project cho khách hàng ABC Company

**Bước thực hiện**:
1. **Tạo Task cho Operations**:
 - Vào Project → **Create Issue** → **Task**
 - Điền thông tin:
 - **Summary**: "Monthly maintenance for ABC Company"
 - **Work Type**: Project
 - **Phase**: Operations
 - **Customer**: ABC Company
 - **Operations Type**: Maintenance

2. **Hoặc dùng Service Request**:
 - Nếu khách hàng yêu cầu → Tạo **Service Request**
 - **Work Type**: Project
 - **Phase**: Operations
 - **Customer**: ABC Company

3. **Log Operations Effort**:
 - **Operations Effort**: 2 hours (maintenance tasks)
 - **Coordination Effort**: 0.5 hours (liên hệ với customer)

**Kết quả**: Operations tasks được track đầy đủ.

---

## 6. KỊCH BẢN INCIDENT RESPONSE

### 6.1. Incident Escalation

**Kịch bản**: Support không giải quyết được Incident, cần escalate lên SRE

**Bước thực hiện**:
1. **Support xử lý ban đầu**:
 - Tạo Incident SEV2
 - Transition: **New → Investigating**
 - Log effort: **Research Effort**: 2 hours

2. **Escalate**:
 - Không tìm được giải pháp
 - Transition: **Investigating → Escalated**
 - Assign cho SRE team
 - Comment: "Escalated to SRE - Database connection issues"

3. **SRE xử lý**:
 - SRE nhận Incident
 - Transition: **Escalated → Investigating**
 - Tìm root cause
 - Log effort: **Research Effort**: 1 hour, **Operations Effort**: 2 hours

4. **Resolve**:
 - Transition: **Investigating → Resolved**
 - Comment: "Fixed database connection pool configuration"

**Kết quả**: Incident đã được escalate và giải quyết.

---

## 7. KỊCH BẢN CHANGE MANAGEMENT

### 7.1. Emergency Change

**Kịch bản**: Cần deploy hotfix ngay lập tức (Emergency Change)

**Bước thực hiện**:
1. **Tạo Emergency Change Request**:
 - Vào Project → **Create Issue** → **Change Request**
 - **Change Type**: Emergency
 - **Risk Level**: High
 - **Summary**: "Emergency hotfix for security vulnerability"
 - **Change Reason**: "Critical security vulnerability found, need immediate fix"

2. **Fast-track Approval**:
 - Transition: **Draft → Submitted**
 - CAB review ngay lập tức
 - Transition: **Submitted → Approved** (fast-track)

3. **Immediate Implementation**:
 - SRE deploy ngay
 - Transition: **Approved → Implementation**
 - Log effort: **Deployment Effort**: 1 hour

4. **Post-Implementation**:
 - Transition: **Implementation → Completed**
 - Post-Implementation Review: "Hotfix deployed successfully, vulnerability patched"
 - Transition: **Completed → Closed**

**Kết quả**: Emergency change đã được deploy thành công.

---

## TỔNG KẾT

Các kịch bản trên bao phủ:
- Agile/Development workflows
- ITIL Service Management
- Effort tracking đầy đủ
- Product lifecycle management
- Project deployment & operations
- Incident response
- Change management

**Lưu ý**: Tất cả kịch bản đều có effort tracking để đảm bảo thống kê đầy đủ.
