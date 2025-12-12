# HỆ THỐNG QUẢN LÝ JIRA - VNPT AI

Hệ thống Jira được thiết kế để quản lý phát triển phần mềm Agile/Kanban, ITIL Service Management, và quản lý dự án trong lĩnh vực AI và Manufacturing với khả năng track effort đầy đủ.

## 📚 CẤU TRÚC TÀI LIỆU

Tài liệu được tổ chức thành các folder theo mục đích:

```
jira/
├── README.md (file này)
├── 01-Phien-Ban/              # Phiên bản và phân tích
├── 02-Huong-Dan-Trien-Khai/   # Hướng dẫn triển khai
├── 03-Huong-Dan-Su-Dung/      # Hướng dẫn sử dụng và training
├── 04-Cau-Hinh/               # Cấu hình, permissions, workflows
├── 05-Effort-Tracking/        # Effort tracking
├── 06-ITIL-Quan-Tri/          # ITIL và quản trị
└── 07-Reference/              # Tài liệu tham khảo
```

---

## ⭐ BẮT ĐẦU TỪ ĐÂY

### 1. [01-Phien-Ban/PHIEN_BAN_CO_BAN.md](./01-Phien-Ban/PHIEN_BAN_CO_BAN.md) - Phiên bản Cơ Bản
   - 8 Issue Types (tối ưu từ 12)
   - 5 Dashboards
   - Triển khai 3 tuần
   - Dễ sử dụng, vận hành nhanh

### 2. [01-Phien-Ban/PHIEN_BAN_NANG_CAO.md](./01-Phien-Ban/PHIEN_BAN_NANG_CAO.md) - Phiên bản Nâng Cao
   - 39 Issue Types (tối ưu từ 47)
   - 15+ Dashboards
   - Triển khai 12-13 tuần
   - Đầy đủ tính năng ITIL, Quản trị, Governance

### 3. [01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md](./01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md) ⭐ **QUAN TRỌNG**
   - Phân tích 4 issue types: Product Research, Product Development, Project Deployment, Project Operations
   - Đánh giá tính cần thiết
   - Khuyến nghị loại bỏ và thay thế bằng Epic/Story/Task
   - Hướng dẫn sử dụng custom fields để phân biệt

---

## 📁 CHI TIẾT TỪNG FOLDER

### 📂 01-Phien-Ban/ - Phiên bản và Phân tích

**Mục đích**: Định nghĩa các phiên bản và phân tích issue types

**Files**:
1. **PHIEN_BAN_CO_BAN.md** - Phiên bản Cơ Bản (8 issue types, 3 tuần triển khai)
2. **PHIEN_BAN_NANG_CAO.md** - Phiên bản Nâng Cao (39 issue types, 12-13 tuần triển khai)
3. **PHAN_TICH_ISSUE_TYPES.md** - Phân tích và quyết định loại bỏ issue types

---

### 📂 02-Huong-Dan-Trien-Khai/ - Hướng dẫn Triển khai

**Mục đích**: Hướng dẫn chi tiết cách triển khai hệ thống Jira

**Files**:
1. **HUONG_DAN_TRIEN_KHAI_JIRA.md** - Hướng dẫn triển khai cơ bản (Agile + ITIL cơ bản)
   - Workflows, Permissions, Custom Fields
   - Dashboards, Reports
   - GitLab integration

2. **CHECKLIST_TRIEN_KHAI.md** - Checklist chi tiết từng bước triển khai
   - 15 phases với tasks cụ thể
   - Step-by-step implementation

3. **KICH_BAN_TRIEN_KHAI.md** ⭐ **KỊCH BẢN TRIỂN KHAI**
   - Kịch bản triển khai cho các tình huống khác nhau
   - Startup/SMB, Enterprise, Migration, Multi-team, Phased Rollout
   - Timeline và checklist chi tiết

---

### 📂 03-Huong-Dan-Su-Dung/ - Hướng dẫn Sử dụng và Training

**Mục đích**: Hướng dẫn sử dụng cho users và tài liệu training

**Files**:
1. **HUONG_DAN_MEMBER_MOI.md** ⭐ **HƯỚNG DẪN**
   - Hướng dẫn cho thành viên mới
   - Các thao tác cơ bản
   - Hướng dẫn theo role (Developer, QA, PO, Support, SRE/DevOps)
   - Effort tracking
   - Tips & Best Practices
   - FAQ

2. **KICH_BAN_SU_DUNG.md** ⭐ **KỊCH BẢN**
   - Kịch bản sử dụng thực tế cho từng role
   - Use cases chi tiết (Agile, ITIL, Effort Tracking, Product Lifecycle)
   - Step-by-step hướng dẫn

3. **TAI_LIEU_TRAINING.md** ⭐ **TRAINING**
   - Tài liệu training chi tiết cho tất cả roles
   - Modules và assessment
   - Training schedule
   - Certification

---

### 📂 04-Cau-Hinh/ - Cấu hình, Permissions, Workflows

**Mục đích**: Cấu hình hệ thống, phân quyền, và workflows

**Files**:
1. **MA_TRAN_PHAN_QUYEN.md** ⭐ **QUAN TRỌNG**
   - Ma trận phân quyền Role × Issue Type
   - Chi tiết quyền hạn cho từng role
   - Phân quyền cho cả 2 phiên bản (Cơ Bản & Nâng Cao)

2. **WORKFLOW_DIAGRAMS.md** - Sơ đồ workflows
   - Workflow diagrams
   - Workflow relationships
   - Status mapping

3. **role.txt** - Định nghĩa các Role và Permissions
   - 7 roles cơ bản
   - Quyền hạn cho từng role

---

### 📂 05-Effort-Tracking/ - Effort Tracking

**Mục đích**: Effort tracking hoàn thiện cho tất cả issue types

**Files**:
1. **EFFORT_TRACKING_HOAN_THIEN.md** ⭐ **QUAN TRỌNG**
   - Effort tracking hoàn thiện cho TẤT CẢ issue types (39 types Nâng cao / 8 types Cơ bản)
   - 8 effort fields: Research, Development, Testing, Deployment, Operations, Review, Documentation, Coordination
   - Custom fields cho mỗi issue type
   - Automation rules
   - JQL queries

2. **DANH_GIA_HOAN_THIEN.md** ⭐ **ĐÁNH GIÁ**
   - Đánh giá mức độ hoàn thiện
   - Phân tích điểm mạnh/yếu
   - Khuyến nghị cải thiện

3. **DANH_GIA_STORY_POINT_PERFORMANCE.md** ⭐ **PERFORMANCE**
   - Đánh giá Story Point và Performance
   - Performance metrics cho dự án (Velocity, Throughput, Quality, Efficiency)
   - Performance metrics cho con người (Individual Velocity, SP/Hour, Bug Rate, Estimation Accuracy)
   - Velocity tracking và Performance Indicators
   - Báo cáo Performance và Dashboards
   - Custom Fields & Automation
   - JQL Queries cho Performance

---

### 📂 06-ITIL-Quan-Tri/ - ITIL và Quản trị

**Mục đích**: ITIL processes đầy đủ và các phương pháp quản trị

**Files**:
1. **BO_SUNG_ITIL_VA_QUAN_TRI.md** - ITIL & Quản trị nâng cao
   - ITIL processes đầy đủ (16 processes)
   - Phương pháp quản trị (Kanban, DevOps, Lean, Risk, Portfolio)
   - Quản lý kinh doanh (Financial, Customer, Demand)
   - Governance & Compliance

---

### 📂 07-Reference/ - Tài liệu Tham khảo

**Mục đích**: Tài liệu tham khảo, queries, troubleshooting, và báo cáo

**Files**:
1. **JQL_QUERIES.md** - Thư viện JQL queries
   - Queries cho Agile, ITIL, Effort tracking
   - Queries cho từng role

2. **TROUBLESHOOTING_FAQ.md** ⭐ **HỖ TRỢ**
   - FAQ - Câu hỏi thường gặp
   - Troubleshooting - Xử lý sự cố
   - Best Practices
   - Performance Optimization
   - Security Considerations
   - Backup & Recovery

3. **BAO_CAO_TONG_HOP.md** ⭐ **BÁO CÁO**
   - Báo cáo Agile/Development
   - Báo cáo ITIL/Service Management
   - Báo cáo Effort Tracking
   - Báo cáo Performance
   - Báo cáo Management

---

## 🎯 TỔNG QUAN

### Tính Năng Chính

#### Agile/Kanban:
- ✅ Epic, Story, Task, Bug management
- ✅ Sprint planning & tracking
- ✅ Velocity tracking
- ✅ Kanban boards với WIP limits
- ✅ Code review workflow
- ✅ GitLab integration

#### ITIL Service Management:
- ✅ Incident Management với SLA
- ✅ Change Management với CAB approval
- ✅ Service Request management
- ✅ Service Order management
- ✅ Problem Management (Nâng cao)
- ✅ Knowledge Management (Nâng cao)
- ✅ Service Level Management (Nâng cao)
- ✅ Availability, Capacity, Security Management (Nâng cao)
- ✅ Asset Management, CMDB (Nâng cao)

#### Effort Tracking:
- ✅ Research Effort (Nghiên cứu)
- ✅ Development Effort (Phát triển)
- ✅ Testing Effort (Testing)
- ✅ Deployment Effort (Triển khai)
- ✅ Operations Effort (Vận hành)
- ✅ Review Effort (Review)
- ✅ Documentation Effort (Documentation)
- ✅ Coordination Effort (Coordination)
- ✅ Total Effort (calculated - 8 fields)
- ✅ Effort % by phase
- ✅ Effort Variance (Estimated vs Actual)
- ✅ Effort Efficiency metrics

#### Quản Trị (Nâng cao):
- ✅ Risk Management
- ✅ Portfolio Management
- ✅ Financial Management
- ✅ Business Relationship Management
- ✅ Governance & Compliance

---

## 📊 SO SÁNH 2 PHIÊN BẢN

| Tiêu chí | Cơ Bản | Nâng Cao |
|----------|--------|----------|
| **Issue Types** | 8 (tối ưu) | 39 (tối ưu) |
| **Workflows** | 9 | 47 |
| **Dashboards** | 5 | 15+ |
| **Roles** | 7 | 12+ |
| **Integrations** | 2 | 6+ |
| **Thời gian triển khai** | 3 tuần | 12-13 tuần |
| **Phù hợp** | Startup, SMB | Enterprise, Large org |

---

## 🚀 QUYẾT ĐỊNH LỰA CHỌN

### Chọn Phiên Bản Cơ Bản nếu:
- ✅ Team < 50 users
- ✅ Cần triển khai nhanh (3 tuần)
- ✅ Yêu cầu đơn giản (Agile + ITIL cơ bản)
- ✅ Startup, SMB

### Chọn Phiên Bản Nâng Cao nếu:
- ✅ Team > 100 users
- ✅ Có thể triển khai trong 3 tháng
- ✅ Yêu cầu đầy đủ (ITIL + Quản trị + Governance)
- ✅ Enterprise organization

---

## 📋 CẤU TRÚC EFFORT TRACKING

### Các Giai Đoạn Effort:
1. **Research Effort** (Nghiên cứu) - Phân tích, nghiên cứu, thiết kế
2. **Development Effort** (Phát triển) - Coding, testing, cấu hình
3. **Testing Effort** (Testing) - Unit testing, integration testing, UAT
4. **Deployment Effort** (Triển khai) - Setup, migration, training
5. **Operations Effort** (Vận hành) - Maintenance, support, optimization
6. **Review Effort** (Review) - Code review, design review
7. **Documentation Effort** (Documentation) - Technical docs, user guides
8. **Coordination Effort** (Coordination) - Meetings, standups, planning

### Custom Fields:
- Research Effort (Time Tracking)
- Development Effort (Time Tracking)
- Testing Effort (Time Tracking)
- Deployment Effort (Time Tracking)
- Operations Effort (Time Tracking)
- Review Effort (Time Tracking)
- Documentation Effort (Time Tracking)
- Coordination Effort (Time Tracking)
- Total Effort (calculated - 8 fields)
- Effort % fields (calculated)
- Estimated Effort fields (Nâng cao)
- Effort Variance (Nâng cao)
- Effort Efficiency (Nâng cao)

---

## 📈 DASHBOARDS

### Phiên Bản Cơ Bản (5 dashboards):
1. Executive Dashboard
2. Product Owner Dashboard
3. Development Dashboard
4. Support Dashboard
5. Effort Summary Dashboard

### Phiên Bản Nâng Cao (15+ dashboards):
1-5. Tất cả dashboards Cơ Bản +
6. Problem Management Dashboard
7. Knowledge Management Dashboard
8. SLA Management Dashboard
9. Financial Dashboard
10. Risk Management Dashboard
11. Compliance Dashboard
12. Portfolio Dashboard
13. Security Dashboard
14. Asset Management Dashboard
15. Advanced Effort Dashboard

---

## 🔧 INTEGRATIONS

### Phiên Bản Cơ Bản:
- GitLab
- Email Notifications

### Phiên Bản Nâng Cao:
- GitLab (full integration)
- Confluence
- Email Notifications (advanced)
- Slack
- Monitoring Tools (Prometheus, Grafana)
- BI Tools (Tableau, Power BI - optional)

---

## ✅ NEXT STEPS

### Cho Admin/Manager:
1. **Chọn phiên bản**: Đọc [01-Phien-Ban/PHIEN_BAN_CO_BAN.md](./01-Phien-Ban/PHIEN_BAN_CO_BAN.md) hoặc [01-Phien-Ban/PHIEN_BAN_NANG_CAO.md](./01-Phien-Ban/PHIEN_BAN_NANG_CAO.md)
2. **Kịch bản triển khai**: Đọc [02-Huong-Dan-Trien-Khai/KICH_BAN_TRIEN_KHAI.md](./02-Huong-Dan-Trien-Khai/KICH_BAN_TRIEN_KHAI.md)
3. **Triển khai**: Follow [02-Huong-Dan-Trien-Khai/CHECKLIST_TRIEN_KHAI.md](./02-Huong-Dan-Trien-Khai/CHECKLIST_TRIEN_KHAI.md)
4. **Hiểu effort tracking**: Đọc [05-Effort-Tracking/EFFORT_TRACKING_HOAN_THIEN.md](./05-Effort-Tracking/EFFORT_TRACKING_HOAN_THIEN.md)
5. **Đánh giá performance**: Đọc [05-Effort-Tracking/DANH_GIA_STORY_POINT_PERFORMANCE.md](./05-Effort-Tracking/DANH_GIA_STORY_POINT_PERFORMANCE.md)
6. **Xem phân quyền**: Đọc [04-Cau-Hinh/MA_TRAN_PHAN_QUYEN.md](./04-Cau-Hinh/MA_TRAN_PHAN_QUYEN.md)
7. **Phân tích issue types**: Đọc [01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md](./01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md)

### Cho Users:
1. **Thành viên mới**: Đọc [03-Huong-Dan-Su-Dung/HUONG_DAN_MEMBER_MOI.md](./03-Huong-Dan-Su-Dung/HUONG_DAN_MEMBER_MOI.md)
2. **Training**: Đọc [03-Huong-Dan-Su-Dung/TAI_LIEU_TRAINING.md](./03-Huong-Dan-Su-Dung/TAI_LIEU_TRAINING.md)
3. **Kịch bản sử dụng**: Đọc [03-Huong-Dan-Su-Dung/KICH_BAN_SU_DUNG.md](./03-Huong-Dan-Su-Dung/KICH_BAN_SU_DUNG.md)
4. **Chi tiết**: Tham khảo [02-Huong-Dan-Trien-Khai/HUONG_DAN_TRIEN_KHAI_JIRA.md](./02-Huong-Dan-Trien-Khai/HUONG_DAN_TRIEN_KHAI_JIRA.md) và [06-ITIL-Quan-Tri/BO_SUNG_ITIL_VA_QUAN_TRI.md](./06-ITIL-Quan-Tri/BO_SUNG_ITIL_VA_QUAN_TRI.md)

---

## 📞 SUPPORT

- **FAQ & Troubleshooting**: Xem [07-Reference/TROUBLESHOOTING_FAQ.md](./07-Reference/TROUBLESHOOTING_FAQ.md)
- **JQL Queries**: Sử dụng [07-Reference/JQL_QUERIES.md](./07-Reference/JQL_QUERIES.md)
- **Workflows**: Tham khảo [04-Cau-Hinh/WORKFLOW_DIAGRAMS.md](./04-Cau-Hinh/WORKFLOW_DIAGRAMS.md)
- **Báo cáo**: Xem [07-Reference/BAO_CAO_TONG_HOP.md](./07-Reference/BAO_CAO_TONG_HOP.md)
- **Chi tiết**: Xem các file markdown trong từng folder

---

**Chúc bạn triển khai thành công! 🚀**
