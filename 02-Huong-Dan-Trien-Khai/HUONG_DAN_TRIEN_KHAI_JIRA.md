# HƯỚNG DẪN TRIỂN KHAI JIRA - HỆ THỐNG QUẢN LÝ DỰ ÁN & ITIL

## MỤC LỤC
1. [Tổng quan hệ thống](#1-tổng-quan-hệ-thống)
2. [Issue Types](#2-issue-types)
3. [Workflows](#3-workflows)
4. [Permission Schemes](#4-permission-schemes)
5. [Custom Fields](#5-custom-fields)
6. [Screens & Field Configuration](#6-screens--field-configuration)
7. [Dashboards](#7-dashboards)
8. [Quản lý Team & Performance](#8-quản-lý-team--performance)
9. [Cấu hình ITIL](#9-cấu-hình-itil)
10. [Tích hợp GitLab](#10-tích-hợp-gitlab)

---

## 1. TỔNG QUAN HỆ THỐNG

### 1.1. Cấu trúc Project
- **Project Type**: Software Development (Agile) + Service Management (ITIL)
- **Project Template**: Scrum + IT Service Management
- **Issue Types**: Epic, Story, Task, Bug, Service Request, Service Order, Incident, Change Request

### 1.2. Các Role chính
1. Product Owner (PO)
2. Developer Team
3. QA / Tester
4. Support / Customer Service
5. SRE / DevOps
6. Change Advisory Board (CAB)
7. Jira Admin

---

## 2. ISSUE TYPES

### 2.1. Agile Issue Types

#### **Epic**
- **Mục đích**: Quản lý các tính năng lớn, chứa nhiều Story
- **Custom Fields**:
  - Epic Name (mặc định)
  - Epic Link (mặc định)
  - Business Value
  - Target Release
  - AI Impact Level (High/Medium/Low)
  - Manufacturing Impact (Yes/No)

#### **Story**
- **Mục đích**: Yêu cầu chức năng từ góc độ người dùng
- **Custom Fields**:
  - Story Points (1, 2, 3, 5, 8, 13, 21)
  - Acceptance Criteria (Text Area)
  - Priority (Highest, High, Medium, Low, Lowest)
  - Component
  - Labels
  - AI Feature Type (ML Model, Data Pipeline, API, UI/UX, Other)
  - Manufacturing Process (Assembly, Quality Control, Inventory, Logistics, Other)

#### **Task**
- **Mục đích**: Công việc cụ thể cần thực hiện
- **Custom Fields**:
  - Original Estimate (hours)
  - Time Spent (hours)
  - Remaining Estimate (hours)
  - Assignee
  - Component
  - Labels

#### **Bug**
- **Mục đích**: Lỗi cần được sửa
- **Custom Fields**:
  - Severity (Critical, High, Medium, Low)
  - Environment (Production, Staging, Development)
  - Steps to Reproduce (Text Area)
  - Expected Result (Text Area)
  - Actual Result (Text Area)
  - Bug Type (Functional, Performance, Security, UI/UX, Data, AI Model)

### 2.2. ITIL Issue Types

#### **Service Request (SR)**
- **Mục đích**: Yêu cầu dịch vụ tiêu chuẩn từ người dùng
- **Custom Fields**:
  - Request Type (Access Request, Information Request, Service Provisioning, Other)
  - Requested By (User Picker)
  - Requested Date (Date Picker)
  - Service Catalog Item
  - SLA Target (Date)
  - Priority (P1-P4)
  - Approval Status (Pending, Approved, Rejected)

#### **Service Order (SO)**
- **Mục đích**: Đơn hàng dịch vụ có tính phí
- **Custom Fields**:
  - Order Number
  - Customer (User Picker)
  - Order Date (Date Picker)
  - Service Items (Text Area)
  - Total Cost (Number)
  - Payment Status (Pending, Paid, Cancelled)
  - Delivery Date (Date Picker)
  - Manufacturing Line (Text)

#### **Incident**
- **Mục đích**: Sự cố cần xử lý theo ITIL
- **Custom Fields**:
  - Severity (SEV1, SEV2, SEV3, SEV4)
  - Impact (Critical, High, Medium, Low)
  - Urgency (Critical, High, Medium, Low)
  - Priority (P1-P4) - Auto-calculated từ Impact + Urgency
  - Incident Category (Hardware, Software, Network, AI Service, Manufacturing System, Other)
  - Root Cause (Text Area)
  - Resolution (Text Area)
  - Resolution Time (hours) - Auto-calculated
  - First Response Time (minutes) - Auto-calculated
  - Affected Services (Multi-select)
  - Related Change Request (Issue Link)

#### **Change Request (CR)**
- **Mục đích**: Yêu cầu thay đổi hệ thống theo ITIL
- **Custom Fields**:
  - Change Type (Standard, Normal, Emergency)
  - Change Category (Infrastructure, Application, Security, AI Model Update, Manufacturing Process)
  - Risk Level (Low, Medium, High, Critical)
  - Change Reason (Text Area)
  - Implementation Plan (Text Area)
  - Rollback Plan (Text Area)
  - CAB Approval (Approved, Rejected, Pending)
  - Implementation Date (Date Picker)
  - Post-Implementation Review (Text Area)
  - Related Incident (Issue Link)

---

## 3. WORKFLOWS

### 3.1. Agile Workflow (Story/Task/Bug)

```
To Do → In Progress → Code Review → Testing → Ready for Release → Done
         ↓                              ↑
         └────────── Blocked ───────────┘
```

**Transitions**:
- **To Do → In Progress**: Developer
- **In Progress → Code Review**: Developer (sau khi tạo MR)
- **Code Review → Testing**: Code Reviewer/Dev Lead
- **Testing → Ready for Release**: QA/Tester
- **Testing → In Progress**: Nếu có bug
- **Ready for Release → Done**: PO/Release Manager
- **Any → Blocked**: Bất kỳ ai (cần lý do)

### 3.2. Epic Workflow

```
To Do → In Progress → Done
```

### 3.3. Service Request Workflow

```
New → In Progress → Pending Approval → Approved → Fulfilled → Closed
                    ↓
                 Rejected → Closed
```

**Transitions**:
- **New → In Progress**: Support/Customer Service
- **In Progress → Pending Approval**: Support (nếu cần approval)
- **Pending Approval → Approved**: PO/Manager
- **Pending Approval → Rejected**: PO/Manager
- **Approved → Fulfilled**: Support/DevOps
- **Fulfilled → Closed**: Support/Customer Service

### 3.4. Service Order Workflow

```
Order Received → Processing → Payment Pending → In Production → Shipped → Delivered → Closed
                                    ↓
                              Payment Failed → Cancelled
```

### 3.5. Incident Workflow (ITIL)

```
New → Acknowledged → Investigating → Mitigated → Resolved → Closed
      ↓                ↓
   On Hold         Escalated
```

**Transitions**:
- **New → Acknowledged**: Support/SRE (trong SLA)
- **Acknowledged → Investigating**: SRE/DevOps
- **Investigating → Mitigated**: SRE/DevOps (workaround)
- **Mitigated → Resolved**: SRE/DevOps (fix hoàn chỉnh)
- **Resolved → Closed**: Support (sau khi xác nhận)
- **Any → Escalated**: Nếu vượt SLA hoặc SEV1
- **Any → On Hold**: Chờ thông tin từ bên ngoài

**SLA Rules**:
- **SEV1**: First Response 15 phút, Resolution 4 giờ
- **SEV2**: First Response 1 giờ, Resolution 8 giờ
- **SEV3**: First Response 4 giờ, Resolution 24 giờ
- **SEV4**: First Response 1 ngày, Resolution 3 ngày

### 3.6. Change Request Workflow (ITIL)

```
Draft → Submitted → Under Review → CAB Review → Approved → Implementation → Testing → Completed → Closed
                        ↓              ↓
                    Rejected      Rejected → Closed
```

**Transitions**:
- **Draft → Submitted**: Developer/SRE
- **Submitted → Under Review**: Change Manager
- **Under Review → CAB Review**: Change Manager (nếu Normal/Emergency)
- **CAB Review → Approved**: CAB Members
- **CAB Review → Rejected**: CAB Members
- **Approved → Implementation**: SRE/DevOps
- **Implementation → Testing**: SRE/DevOps
- **Testing → Completed**: QA/SRE
- **Completed → Closed**: Change Manager

**Emergency Change**: Bỏ qua CAB Review, cần approval từ 2 CAB members

---

## 4. PERMISSION SCHEMES

### 4.1. Product Owner (PO)

**Permissions**:
- Browse Projects: ✅
- Create Issues: ✅
- Edit Issues: ✅
- Delete Issues: ❌
- Transition Issues: ✅ (tất cả)
- Assign Issues: ✅
- Assignable User: ✅
- Manage Components: ✅
- Manage Versions: ✅
- Edit Version/Release Notes: ✅
- View Read-Only Workflow: ✅
- Create Attachments: ✅
- Delete All Attachments: ❌
- Delete Own Attachments: ✅
- Work On Issues: ✅
- View Voters and Watchers: ✅
- Manage Watchers: ✅
- Add Comments: ✅
- Edit All Comments: ✅
- Edit Own Comments: ✅
- Delete All Comments: ❌
- Delete Own Comments: ✅
- Administer Projects: ❌
- Close Issues: ✅
- Modify Reporter: ✅
- Move Issues: ✅
- Resolve Issues: ✅
- Schedule Issues: ✅
- Set Issue Security: ❌
- View Change History: ✅

**Issue Type Restrictions**: Không có

**Approval Permissions**:
- Approve Change Request: ✅

### 4.2. Developer Team

**Permissions**:
- Browse Projects: ✅
- Create Issues: ✅ (Story, Task, Bug)
- Edit Issues: ✅ (Story, Task, Bug)
- Delete Issues: ❌
- Transition Issues: ✅ (chỉ trong luồng Dev: To Do → In Progress → Code Review)
- Assign Issues: ✅ (chỉ assign cho mình)
- Assignable User: ✅
- Create Attachments: ✅
- Delete Own Attachments: ✅
- Work On Issues: ✅ (Log Work)
- Add Comments: ✅
- Edit Own Comments: ✅
- View Change History: ✅
- View Incident: ✅ (read-only)
- View Change Request: ✅ (read-only)
- Create GitLab Branch: ✅
- Create Merge Request: ✅

**Issue Type Restrictions**:
- Cannot create: Epic, Service Request, Service Order, Incident, Change Request (ops scope)

### 4.3. QA / Tester

**Permissions**:
- Browse Projects: ✅
- Create Issues: ✅ (Bug)
- Edit Issues: ✅ (chỉ phần Testing results)
- Transition Issues: ✅ (Testing → Ready for Release, Testing → In Progress)
- Work On Issues: ✅ (Log Work)
- Add Comments: ✅
- Edit Own Comments: ✅
- View Change History: ✅

**Issue Type Restrictions**:
- Cannot create: Epic, Story, Task (dev), Service Request, Service Order, Incident, Change Request

### 4.4. Support / Customer Service

**Permissions**:
- Browse Projects: ✅
- Create Issues: ✅ (Service Request, Incident SEV2-SEV3)
- Edit Issues: ✅ (Service Request, Incident)
- Transition Issues: ✅ (trong workflow SR và Incident)
- Work On Issues: ✅ (Log Work)
- Add Comments: ✅
- Upload Attachments: ✅
- View Change History: ✅

**Issue Type Restrictions**:
- Cannot create: Epic, Story, Task, Bug, Change Request
- Cannot create: Incident SEV1 (chỉ SRE/DevOps)

### 4.5. SRE / DevOps

**Permissions**:
- Browse Projects: ✅
- Create Issues: ✅ (Incident SEV1-SEV2, Change Request, Ops Task)
- Edit Issues: ✅ (Incident, Change Request, Ops Task)
- Transition Issues: ✅ (Incident: Investigating → Mitigated → Resolved, Change Request: Implementation → Testing)
- Approve Change Request: ✅ (deployment)
- Work On Issues: ✅
- View Logs & Alerts: ✅
- Manage Environments: ✅ (Prod/Staging)
- Run GitLab Pipeline: ✅
- Add Comments: ✅
- Edit Own Comments: ✅
- View Change History: ✅

**Issue Type Restrictions**:
- Cannot create: Epic, Story (dev), Bug

### 4.6. Change Advisory Board (CAB)

**Permissions**:
- Browse Projects: ✅
- View Issues: ✅ (tất cả)
- Edit Issues: ✅ (Change Request - chỉ phần approval)
- Transition Issues: ✅ (CAB Review → Approved/Rejected)
- Add Comments: ✅ (required fields)
- View Change History: ✅
- View Logs & RCA: ✅

**Issue Type Restrictions**:
- Chỉ xử lý Change Request

### 4.7. Jira Admin

**Permissions**: Tất cả quyền quản trị
- Administer Projects: ✅
- Manage Workflows: ✅
- Create Projects: ✅
- Manage Permission Schemes: ✅
- Create Custom Fields: ✅
- Global Configuration: ✅

**Restriction**: KHÔNG tham gia vận hành sản phẩm

---

## 5. CUSTOM FIELDS

### 5.1. Agile Custom Fields

| Field Name | Field Type | Context | Description |
|------------|------------|---------|-------------|
| Story Points | Select List (1,2,3,5,8,13,21) | Story | Ước lượng độ phức tạp |
| Original Estimate | Time Tracking | Task, Story | Thời gian ước tính ban đầu |
| Time Spent | Time Tracking | Task, Story, Bug | Thời gian đã sử dụng |
| Remaining Estimate | Time Tracking | Task, Story | Thời gian còn lại |
| Acceptance Criteria | Text Area | Story | Tiêu chí chấp nhận |
| AI Feature Type | Select List | Story, Bug | Loại tính năng AI |
| Manufacturing Process | Select List | Story, Bug | Quy trình sản xuất liên quan |
| Bug Type | Select List | Bug | Loại bug |
| Environment | Select List | Bug | Môi trường phát hiện bug |

### 5.2. ITIL Custom Fields

| Field Name | Field Type | Context | Description |
|------------|------------|---------|-------------|
| Severity | Select List (SEV1-SEV4) | Incident | Mức độ nghiêm trọng |
| Impact | Select List | Incident | Mức độ ảnh hưởng |
| Urgency | Select List | Incident | Mức độ khẩn cấp |
| Priority | Select List (P1-P4) | Incident, SR | Độ ưu tiên (auto-calc) |
| Incident Category | Select List | Incident | Phân loại sự cố |
| Root Cause | Text Area | Incident | Nguyên nhân gốc rễ |
| Resolution Time | Number | Incident | Thời gian xử lý (hours) |
| First Response Time | Number | Incident | Thời gian phản hồi đầu tiên (minutes) |
| Change Type | Select List | Change Request | Loại thay đổi |
| Change Category | Select List | Change Request | Phân loại thay đổi |
| Risk Level | Select List | Change Request | Mức độ rủi ro |
| CAB Approval | Select List | Change Request | Trạng thái phê duyệt CAB |
| Request Type | Select List | Service Request | Loại yêu cầu |
| Service Catalog Item | Text | Service Request | Mục catalog dịch vụ |
| SLA Target | Date | Service Request | Mục tiêu SLA |
| Order Number | Text | Service Order | Số đơn hàng |
| Total Cost | Number | Service Order | Tổng chi phí |
| Payment Status | Select List | Service Order | Trạng thái thanh toán |

### 5.3. Performance & Effort Tracking Fields

| Field Name | Field Type | Context | Description |
|------------|------------|---------|-------------|
| Team Member | User Picker | All | Thành viên team |
| Sprint | Select List | Story, Task, Bug | Sprint hiện tại |
| Velocity | Number | Epic | Vận tốc team |
| Effort Variance | Number | Task, Story | Chênh lệch effort (actual vs estimate) |
| Performance Score | Number | All | Điểm đánh giá hiệu suất |
| Quality Metrics | Text Area | Bug | Chỉ số chất lượng |
| AI Model Performance | Text Area | Story, Bug | Hiệu suất model AI |
| Manufacturing Efficiency | Number | Story, Task | Hiệu quả sản xuất |

---

## 6. SCREENS & FIELD CONFIGURATION

### 6.1. Screen Schemes

**Agile Screen Scheme**:
- Create Screen: Epic Create, Story Create, Task Create, Bug Create
- Edit Screen: Epic Edit, Story Edit, Task Edit, Bug Edit
- View Screen: Epic View, Story View, Task View, Bug View
- Transition Screen: Agile Transition

**ITIL Screen Scheme**:
- Create Screen: SR Create, SO Create, Incident Create, CR Create
- Edit Screen: SR Edit, SO Edit, Incident Edit, CR Edit
- View Screen: SR View, SO View, Incident View, CR View
- Transition Screen: ITIL Transition

### 6.2. Field Configuration Schemes

**Agile Field Configuration**:
- Required: Story Points (Story), Original Estimate (Task), Severity (Bug)
- Hidden: Resolution Time (Agile issues), Change Type (Agile issues)
- Optional: Tất cả custom fields khác

**ITIL Field Configuration**:
- Required: Severity (Incident), Change Type (CR), Request Type (SR)
- Hidden: Story Points (ITIL issues), Sprint (ITIL issues)
- Optional: Tất cả custom fields khác

---

## 7. DASHBOARDS

### 7.1. Executive Dashboard (C-Level)

**Gadgets**:
1. **Portfolio Summary**
   - Tổng số Epic đang thực hiện
   - Tổng số Story Points đã hoàn thành
   - Velocity trend (3 tháng)

2. **ITIL Service Health**
   - Số lượng Incident theo Severity (pie chart)
   - MTTR (Mean Time To Resolve) trend
   - SLA Compliance Rate
   - Change Success Rate

3. **AI Projects Overview**
   - Số lượng AI features đang phát triển
   - AI Model Performance metrics
   - AI-related incidents

4. **Manufacturing Impact**
   - Số lượng issues liên quan đến sản xuất
   - Manufacturing efficiency metrics
   - Service Orders status

5. **Team Performance**
   - Velocity by team
   - Effort variance
   - Quality metrics (bug rate)

6. **Financial Overview**
   - Service Order revenue
   - Project costs
   - ROI by project

### 7.2. Product Owner Dashboard

**Gadgets**:
1. **Sprint Progress**
   - Burndown chart
   - Story Points completed vs planned
   - Issues by status

2. **Backlog Management**
   - Epic progress
   - Story prioritization
   - Dependencies

3. **Release Planning**
   - Version progress
   - Release notes
   - Change Requests pending approval

4. **Team Velocity**
   - Velocity chart (last 5 sprints)
   - Forecast completion

5. **Quality Metrics**
   - Bug rate
   - Test coverage
   - Defect density

### 7.3. Development Team Dashboard

**Gadgets**:
1. **My Work**
   - Assigned issues
   - In Progress issues
   - Code Review queue

2. **Sprint Board**
   - Kanban board
   - Story progress
   - Blocked issues

3. **GitLab Integration**
   - Active branches
   - Merge Requests status
   - Pipeline status

4. **Time Tracking**
   - Time spent this sprint
   - Remaining estimate
   - Effort variance

### 7.4. QA Dashboard

**Gadgets**:
1. **Testing Queue**
   - Issues ready for testing
   - Test execution status
   - Bug reports

2. **Quality Metrics**
   - Bugs found vs fixed
   - Test coverage
   - Defect leakage

3. **Test Results**
   - Pass/fail rate
   - Environment status
   - Regression tests

### 7.5. Support Dashboard

**Gadgets**:
1. **Service Request Queue**
   - Open SRs
   - SLA status
   - Pending approvals

2. **Incident Management**
   - Active incidents
   - SLA compliance
   - Escalated issues

3. **Customer Satisfaction**
   - Response time
   - Resolution time
   - Customer feedback

### 7.6. SRE/DevOps Dashboard

**Gadgets**:
1. **Incident Management**
   - Active SEV1/SEV2 incidents
   - MTTR trend
   - Incident trends

2. **Change Management**
   - Change Requests in progress
   - Deployment pipeline
   - Rollback status

3. **Infrastructure Health**
   - System alerts
   - Environment status
   - Performance metrics

4. **AI Service Monitoring**
   - AI model performance
   - API response times
   - Error rates

### 7.7. Manufacturing Dashboard

**Gadgets**:
1. **Production Issues**
   - Issues by manufacturing process
   - Critical issues
   - Resolution time

2. **Service Orders**
   - Orders in production
   - Delivery status
   - Payment status

3. **Efficiency Metrics**
   - Manufacturing efficiency
   - Process improvements
   - Quality metrics

4. **AI in Manufacturing**
   - AI features in production
   - Model performance
   - Automation impact

### 7.8. ITIL Service Management Dashboard

**Gadgets**:
1. **Service Health**
   - Incident trends
   - Service availability
   - SLA compliance

2. **Change Management**
   - Change success rate
   - Failed changes
   - CAB approvals

3. **Service Catalog**
   - Service Request trends
   - Popular services
   - Fulfillment time

4. **Problem Management**
   - Root cause analysis
   - Recurring incidents
   - Known errors

---

## 8. QUẢN LÝ TEAM & PERFORMANCE

### 8.1. Team Structure

**Project Teams**:
- Development Team (Frontend, Backend, AI/ML)
- QA Team
- DevOps/SRE Team
- Support Team
- Manufacturing Team

**Component Assignment**:
- Frontend Components → Frontend Team
- Backend Components → Backend Team
- AI/ML Components → AI/ML Team
- Infrastructure → DevOps Team

### 8.2. Effort Tracking

**Time Tracking Configuration**:
- Enable time tracking cho tất cả issue types
- Default unit: Hours
- Work log visibility: Team members có thể xem work logs của nhau

**Effort Metrics**:
- **Original Estimate**: Ước lượng ban đầu
- **Time Spent**: Thời gian thực tế
- **Remaining Estimate**: Thời gian còn lại
- **Effort Variance**: (Time Spent - Original Estimate) / Original Estimate * 100%

**Reports**:
- Time Tracking Report: Xem time spent theo team member, issue type, component
- Effort Variance Report: So sánh estimate vs actual

### 8.3. Performance Evaluation

**Performance Metrics**:

1. **Velocity**
   - Story Points completed per sprint
   - Track 5 sprints để có baseline
   - Forecast dựa trên velocity trung bình

2. **Quality Metrics**
   - Bug rate: Số bugs / Story Points
   - Defect leakage: Bugs found in production / Total bugs
   - Test coverage: % code được test

3. **Efficiency Metrics**
   - Effort variance: Độ chính xác của estimate
   - Cycle time: Thời gian từ To Do → Done
   - Lead time: Thời gian từ tạo issue → Done

4. **AI-Specific Metrics**
   - Model accuracy
   - Inference time
   - Data quality score
   - Model drift detection

5. **Manufacturing Metrics**
   - Production efficiency
   - Quality rate
   - Downtime reduction
   - Process improvement impact

**Performance Dashboard**:
- Team velocity chart
- Effort variance by team member
- Quality metrics trend
- Cycle time distribution
- AI model performance over time
- Manufacturing efficiency trends

### 8.4. Sprint Planning

**Sprint Configuration**:
- Sprint duration: 2 weeks
- Sprint goal: Định nghĩa mục tiêu sprint
- Capacity planning: Dựa trên velocity và availability

**Sprint Ceremonies Tracking**:
- Sprint Planning: Tạo Epic/Story trong sprint
- Daily Standup: Update status, log work
- Sprint Review: Demo completed stories
- Sprint Retrospective: Tạo action items

---

## 9. CẤU HÌNH ITIL

### 9.1. Incident Management

**Severity Levels**:
- **SEV1 (Critical)**: Hệ thống down, ảnh hưởng toàn bộ users
- **SEV2 (High)**: Chức năng chính bị ảnh hưởng, nhiều users
- **SEV3 (Medium)**: Chức năng phụ bị ảnh hưởng, ít users
- **SEV4 (Low)**: Vấn đề nhỏ, workaround có sẵn

**Priority Calculation**:
- P1: Impact=Critical AND Urgency=Critical
- P2: (Impact=Critical OR High) AND (Urgency=High OR Critical)
- P3: (Impact=Medium) OR (Urgency=Medium)
- P4: Impact=Low AND Urgency=Low

**SLA Configuration**:
- SEV1: First Response 15 phút, Resolution 4 giờ
- SEV2: First Response 1 giờ, Resolution 8 giờ
- SEV3: First Response 4 giờ, Resolution 24 giờ
- SEV4: First Response 1 ngày, Resolution 3 ngày

**Automation Rules**:
- Auto-assign SEV1 → SRE team
- Auto-escalate nếu vượt SLA
- Auto-create Change Request nếu cần fix permanent

### 9.2. Change Management

**Change Types**:
- **Standard Change**: Pre-approved, low risk, thường xuyên
- **Normal Change**: Cần CAB approval
- **Emergency Change**: Urgent, cần 2 CAB members approval

**CAB Composition**:
- Product Owner
- Dev Lead / Tech Lead
- SRE Lead
- PM / VP Engineering (tùy công ty)

**Change Risk Assessment**:
- **Low**: Không ảnh hưởng production, có rollback plan
- **Medium**: Ảnh hưởng một phần, rollback plan rõ ràng
- **High**: Ảnh hưởng lớn, rollback phức tạp
- **Critical**: Ảnh hưởng toàn hệ thống, rollback khó

**Post-Implementation Review**:
- Review sau 1 tuần implementation
- Đánh giá success/failure
- Lessons learned
- Update documentation

### 9.3. Service Request Management

**Request Types**:
- Access Request: Yêu cầu quyền truy cập
- Information Request: Yêu cầu thông tin
- Service Provisioning: Cung cấp dịch vụ mới
- Other: Yêu cầu khác

**Approval Workflow**:
- Access Request → Manager approval
- Service Provisioning → PO/Manager approval
- Information Request → Auto-approve

**SLA Targets**:
- Access Request: 1 ngày
- Information Request: 4 giờ
- Service Provisioning: 3 ngày

### 9.4. Service Order Management

**Order Lifecycle**:
1. Order Received
2. Processing (validation)
3. Payment Pending
4. In Production
5. Shipped
6. Delivered
7. Closed

**Integration Points**:
- Link với Service Request (nếu có)
- Link với Manufacturing process
- Link với Delivery system

---

## 10. TÍCH HỢP GITLAB

### 10.1. GitLab Integration Setup

**Configuration**:
1. Install GitLab for Jira app
2. Connect GitLab instance
3. Link Jira project với GitLab project

**Features**:
- Tạo branch từ Jira issue
- Tạo Merge Request từ Jira
- View commits, MRs trong Jira
- Auto-transition issue khi MR merged
- View pipeline status

### 10.2. Branch Naming Convention

**Format**: `{issue-type}/{issue-key}-{short-description}`

**Examples**:
- `feature/PROJ-123-add-user-authentication`
- `bugfix/PROJ-456-fix-login-error`
- `hotfix/PROJ-789-critical-security-patch`

### 10.3. Auto-transition Rules

**When MR Created**:
- Story/Task: Transition to "Code Review"

**When MR Merged**:
- Story/Task: Transition to "Testing"
- Bug: Transition to "Testing"

**When Pipeline Passes**:
- Story/Task: Auto-assign to QA team

**When Pipeline Fails**:
- Notify assignee
- Add comment to issue

---

## 11. CẤU HÌNH BỔ SUNG

### 11.1. Automation Rules

**Auto-assignment Rules**:
- Bug → Assign to QA team lead
- Incident SEV1 → Assign to SRE on-call
- Service Request → Assign to Support team
- Change Request → Assign to Change Manager

**Notification Rules**:
- SEV1 Incident → Notify SRE team + Management
- Change Request approved → Notify implementation team
- SLA breach → Escalate to manager

**Field Auto-population**:
- Priority (Incident) → Auto-calculate từ Impact + Urgency
- Resolution Time → Auto-calculate từ timestamps
- First Response Time → Auto-calculate từ timestamps

### 11.2. JQL Queries Thường Dùng

**My Open Issues**:
```jql
assignee = currentUser() AND status != Done AND status != Closed
```

**Sprint Backlog**:
```jql
project = PROJ AND sprint in openSprints() AND type in (Story, Task, Bug)
```

**Critical Incidents**:
```jql
type = Incident AND severity in (SEV1, SEV2) AND status != Closed
```

**Change Requests Pending Approval**:
```jql
type = "Change Request" AND "CAB Approval" = Pending
```

**AI Features in Progress**:
```jql
type = Story AND "AI Feature Type" is not EMPTY AND status != Done
```

**Manufacturing Issues**:
```jql
"Manufacturing Process" is not EMPTY AND status != Done
```

### 11.3. Reports

**Agile Reports**:
- Sprint Report
- Burndown Chart
- Velocity Chart
- Cumulative Flow Diagram
- Epic Report
- Version Report

**ITIL Reports**:
- Incident Report
- Change Management Report
- SLA Report
- Service Request Report
- Problem Management Report

**Performance Reports**:
- Time Tracking Report
- Effort Variance Report
- Team Performance Report
- Quality Metrics Report

---

## 12. CHECKLIST TRIỂN KHAI

### Phase 1: Setup Cơ Bản
- [ ] Tạo Project với template phù hợp
- [ ] Tạo tất cả Issue Types
- [ ] Tạo Custom Fields
- [ ] Tạo Workflows
- [ ] Tạo Permission Schemes
- [ ] Tạo Screen Schemes
- [ ] Tạo Field Configuration Schemes

### Phase 2: Cấu hình ITIL
- [ ] Cấu hình Incident Management
- [ ] Cấu hình Change Management
- [ ] Cấu hình Service Request
- [ ] Cấu hình Service Order
- [ ] Setup SLA rules
- [ ] Tạo CAB group

### Phase 3: Tích hợp & Automation
- [ ] Tích hợp GitLab
- [ ] Setup Automation rules
- [ ] Cấu hình Notifications
- [ ] Setup Auto-assignment

### Phase 4: Dashboards & Reports
- [ ] Tạo Executive Dashboard
- [ ] Tạo Team Dashboards
- [ ] Tạo ITIL Dashboards
- [ ] Tạo Performance Reports
- [ ] Setup JQL filters

### Phase 5: Testing & Training
- [ ] Test workflows với test users
- [ ] Verify permissions
- [ ] Training cho các teams
- [ ] Document processes
- [ ] Go-live

---

## 13. BEST PRACTICES

### 13.1. Issue Management
- Luôn link Epic với Stories
- Sử dụng Components để phân loại
- Sử dụng Labels để tag và filter
- Update status thường xuyên
- Log work hàng ngày

### 13.2. ITIL Practices
- Follow incident severity guidelines
- Document root cause cho mọi incident
- Review change requests kỹ trước khi approve
- Track SLA compliance
- Conduct post-implementation reviews

### 13.3. Performance Tracking
- Track velocity consistently
- Review effort variance hàng sprint
- Monitor quality metrics
- Adjust estimates dựa trên historical data

### 13.4. Team Collaboration
- Sử dụng comments để communicate
- Attach relevant files/logs
- Link related issues
- Update stakeholders thường xuyên

---

## 14. TÀI LIỆU THAM KHẢO

- Jira Administration Guide
- ITIL 4 Foundation
- Agile/Scrum Guide
- GitLab Integration Documentation

---

**Lưu ý**: Tài liệu này là hướng dẫn tổng quan. Cần điều chỉnh chi tiết dựa trên nhu cầu cụ thể của tổ chức và cấu hình Jira instance.
