# PHIÊN BẢN CƠ BẢN - QUẢN TRỊ JIRA

## 🎯 MỤC TIÊU

- ✅ Triển khai nhanh
- ✅ Dễ sử dụng, training tối thiểu
- ✅ Tích hợp tốt với GitLab
- ✅ Vận hành đơn giản
- ✅ Đáp ứng chất lượng cao
- ✅ Track effort đầy đủ (8 fields: Research, Development, Testing, Deployment, Operations, Review, Documentation, Coordination)

---

## 📋 PHẠM VI TRIỂN KHAI

### 1. ISSUE TYPES (8 types)

#### Agile (4 types):
1. **Epic** - Quản lý tính năng lớn (có thể dùng cho Research, Development, Deployment)
2. **Story** - Yêu cầu chức năng (dùng cho Development)
3. **Task** - Công việc cụ thể (dùng cho Deployment, Operations)
4. **Bug** - Lỗi cần sửa

#### ITIL Cơ Bản (4 types):
5. **Incident** - Sự cố (SEV1-SEV4) - **Có SLA**: First Response (15 phút - 1 ngày), Resolution (4 giờ - 3 ngày)
6. **Change Request** - Yêu cầu thay đổi - **Có SLA**: Review (2 giờ - 2 ngày), Approval (4 giờ - 3 ngày), Implementation (1-5 ngày)
7. **Service Request** - Yêu cầu dịch vụ (có thể dùng cho Operations) - **Có SLA**: Response (1-4 giờ), Fulfillment (4 giờ - 5 ngày)
8. **Service Order** - Đơn hàng dịch vụ - **Có SLA**: Processing (2 giờ), Payment (1 ngày), Production (1 ngày), Delivery (theo terms)

**Lưu ý**: Product Research, Product Development, Project Deployment, Project Operations được thay thế bằng Epic/Story/Task với custom fields (Work Type, Phase, Customer). Xem PHAN_TICH_ISSUE_TYPES.md để biết chi tiết.

---

### 2. CUSTOM FIELDS - EFFORT TRACKING

#### Effort Fields (Time Tracking):
- **Research Effort** - Công sức nghiên cứu (hours)
- **Development Effort** - Công sức phát triển (hours)
- **Testing Effort** - Công sức testing (hours)
- **Deployment Effort** - Công sức triển khai (hours)
- **Operations Effort** - Công sức vận hành (hours)
- **Review Effort** - Công sức review (hours)
- **Documentation Effort** - Công sức documentation (hours)
- **Coordination Effort** - Công sức coordination (hours)

#### Calculated Fields:
- **Total Effort** - Tổng effort (Research + Development + Testing + Deployment + Operations + Review + Documentation + Coordination)
- **Research Effort %** - % effort nghiên cứu
- **Development Effort %** - % effort phát triển
- **Testing Effort %** - % effort testing
- **Deployment Effort %** - % effort triển khai
- **Operations Effort %** - % effort vận hành
- **Review Effort %** - % effort review
- **Documentation Effort %** - % effort documentation
- **Coordination Effort %** - % effort coordination

#### Classification Fields:
- **Work Type**: Product, Project, Support, ITIL (QUAN TRỌNG - dùng để phân biệt loại công việc)
- **Phase**: Research, Development, Testing, Deployment, Operations (QUAN TRỌNG - dùng để phân biệt phase)
- **Customer** (cho Project issues): User Picker
- **Research Phase** (cho Research): Market Research, User Research, Requirements Analysis, Architecture Design
- **Development Phase** (cho Development): Design, Development, Testing, Integration
- **Deployment Phase** (cho Deployment): Planning, Setup, Data Migration, Training, Go-live
- **Operations Type** (cho Operations): Maintenance, Support, Optimization, Monitoring

---

### 3. WORKFLOWS

#### Agile Workflow (Story/Task/Bug):
```
To Do → In Progress → Code Review → Testing → Ready for Release → Done
```

#### Epic Workflow:
```
To Do → In Progress → Done
```

#### Incident Workflow (ITIL):
```
New → Acknowledged → Investigating → Resolved → Closed
```

#### Change Request Workflow (ITIL):
```
Draft → Submitted → Approved → Implementation → Completed → Closed
```

#### Service Request Workflow:
```
New → In Progress → Fulfilled → Closed
```

#### Service Order Workflow:
```
Order Received → Processing → In Production → Delivered → Closed
```

**Lưu ý**: Product Research, Product Development, Project Deployment, Project Operations được quản lý bằng Epic/Story/Task với workflows tương ứng:

- **Product Research**: Dùng Epic/Story với Work Type=Product, Phase=Research
- **Product Development**: Dùng Story với Work Type=Product, Phase=Development
- **Project Deployment**: Dùng Epic/Story/Task với Work Type=Project, Phase=Deployment
- **Project Operations**: Dùng Task/Service Request với Work Type=Project, Phase=Operations

---

### 4. ROLES & PERMISSIONS (7 roles)

1. **Product Owner** - Quản lý backlog, approve changes
2. **Developer** - Phát triển, code review
3. **QA/Tester** - Testing, tạo bugs
4. **Support** - Xử lý service requests, incidents
5. **SRE/DevOps** - Xử lý incidents, deploy changes
6. **CAB** - Approve change requests
7. **Jira Admin** - Quản trị hệ thống

---

### 5. DASHBOARDS (5 dashboards)

1. **Executive Dashboard**
   - Total Effort by Phase (Research, Development, Deployment, Operations)
   - Effort Trend
   - Effort by Issue Type

2. **Product Owner Dashboard**
   - Sprint Progress
   - Backlog Management
   - Product Effort Summary

3. **Development Dashboard**
   - My Work
   - Sprint Board
   - Development Effort Tracking

4. **Support Dashboard**
   - Service Request Queue
   - Incident Management
   - Operations Effort

5. **Effort Summary Dashboard**
   - Total Effort by Phase (Pie Chart)
   - Effort Trend (Line Chart)
   - Effort by Issue Type (Bar Chart)
   - Effort by Customer (Bar Chart - cho Project)

---

### 6. INTEGRATIONS

- ✅ **GitLab** - Branch, MR, pipeline integration
- ✅ **Email Notifications** - Mặc định Jira

---

### 7. AUTOMATION (Cơ bản)

- Auto-assign incidents theo severity
- Auto-transition khi MR merged
- Auto-calculate Total Effort từ các effort fields
- Auto-calculate Effort % fields
- SLA reminders

---

## 📊 EFFORT TRACKING

### Issue Types với Effort Fields:

#### Epic:
- Total Research Effort (calculated từ children)
- Total Development Effort (calculated từ children)
- Total Testing Effort (calculated từ children)
- Total Deployment Effort (calculated từ children)
- Total Operations Effort (calculated từ children)
- Total Review Effort (calculated từ children)
- Total Documentation Effort (calculated từ children)
- Total Coordination Effort (calculated từ children)
- Total Effort (calculated)

#### Story/Task:
- Research Effort (Time Tracking)
- Development Effort (Time Tracking)
- Testing Effort (Time Tracking)
- Deployment Effort (Time Tracking)
- Operations Effort (Time Tracking)
- Review Effort (Time Tracking)
- Documentation Effort (Time Tracking)
- Coordination Effort (Time Tracking)
- Total Effort (calculated)

**Lưu ý**: Effort tracking cho Product Research, Product Development, Project Deployment, Project Operations được thực hiện thông qua Epic/Story/Task:

- **Epic/Story với Work Type=Product, Phase=Research**: Track Research Effort
- **Story với Work Type=Product, Phase=Development**: Track Research + Development Effort
- **Epic/Story/Task với Work Type=Project, Phase=Deployment**: Track Research + Development + Deployment Effort
- **Task/Service Request với Work Type=Project, Phase=Operations**: Track Operations Effort

---

## 📈 REPORTS

1. **Effort Summary Report**
   - Total effort by phase
   - Effort by issue type
   - Effort trends

2. **Product Effort Report**
   - Research effort
   - Development effort
   - Total effort

3. **Project Effort Report**
   - Effort per customer
   - Deployment effort
   - Operations effort

---

## ✅ CHECKLIST TRIỂN KHAI

### Phase 1: Setup Cơ Bản
- [ ] Tạo Project
- [ ] Tạo 8 Issue Types (Epic, Story, Task, Bug, Incident, Change Request, Service Request, Service Order)
- [ ] Tạo Effort Fields (Research, Development, Testing, Deployment, Operations, Review, Documentation, Coordination)
- [ ] Tạo Calculated Fields (Total Effort, Effort %)
- [ ] Tạo Classification Fields (Work Type, Phase, Customer, Research Phase, Development Phase, Deployment Phase, Operations Type)

### Phase 2: Workflows
- [ ] Setup Agile workflows (Epic, Story, Task, Bug)
- [ ] Setup ITIL workflows (Incident, Change Request, Service Request, Service Order)
- [ ] Configure Epic/Story/Task để support Work Type và Phase fields

### Phase 3: Permissions & Screens
- [ ] Cấu hình 7 roles
- [ ] Setup permission schemes
- [ ] Tạo screens cho từng issue type

### Phase 4: Dashboards & Reports
- [ ] Tạo 5 dashboards
- [ ] Setup effort tracking reports
- [ ] Configure JQL queries

### Phase 5: Automation
- [ ] Auto-calculate Total Effort
- [ ] Auto-calculate Effort %
- [ ] Auto-assign rules
- [ ] Auto-transition rules

### Phase 6: Integration
- [ ] GitLab integration
- [ ] Email notifications

### Phase 7: Testing & Training
- [ ] Test workflows
- [ ] Test effort tracking
- [ ] User training
- [ ] Go-live

---

## 🎯 BEST PRACTICES

1. **Effort Tracking**:
   - Log effort vào đúng phase field
   - Update effort thường xuyên (daily/weekly)
   - Review effort accuracy định kỳ

2. **Agile**:
   - Sử dụng Story Points cho estimation
   - Track velocity
   - Review sprint effort

3. **ITIL**:
   - Follow incident severity guidelines
   - Track SLA compliance
   - Document changes

4. **Reporting**:
   - Review effort reports hàng tuần
   - Compare actual vs estimated effort
   - Identify effort trends

---

**Xem chi tiết trong HUONG_DAN_TRIEN_KHAI_JIRA.md, QUAN_TRI_EFFORT_JIRA.md và PHAN_TICH_ISSUE_TYPES.md**
