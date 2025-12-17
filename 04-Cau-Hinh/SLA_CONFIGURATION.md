# CẤU HÌNH SLA - ITIL CƠ BẢN

## TỔNG QUAN

Tài liệu này định nghĩa chi tiết Service Level Agreement (SLA) cho tất cả 4 issue types ITIL Cơ Bản:
1. **Incident** - Sự cố
2. **Change Request** - Yêu cầu thay đổi
3. **Service Request** - Yêu cầu dịch vụ
4. **Service Order** - Đơn hàng dịch vụ

---

## 1. INCIDENT - SLA CONFIGURATION

### 1.1. Severity Levels & SLA Targets

| Severity | Mô tả | First Response Time | Resolution Time | Escalation Time |
|----------|-------|---------------------|-----------------|-----------------|
| **SEV1 (Critical)** | Hệ thống down, ảnh hưởng toàn bộ users, không có workaround | **15 phút** | **4 giờ** | 30 phút (nếu chưa acknowledged) |
| **SEV2 (High)** | Chức năng chính bị ảnh hưởng, nhiều users, có workaround tạm | **1 giờ** | **8 giờ** | 2 giờ (nếu chưa acknowledged) |
| **SEV3 (Medium)** | Chức năng phụ bị ảnh hưởng, ít users, workaround có sẵn | **4 giờ** | **24 giờ** | 8 giờ (nếu chưa acknowledged) |
| **SEV4 (Low)** | Vấn đề nhỏ, không ảnh hưởng chức năng chính, workaround rõ ràng | **1 ngày (8 giờ làm việc)** | **3 ngày** | 2 ngày (nếu chưa acknowledged) |

### 1.2. Custom Fields cho SLA Tracking

#### SLA Fields:
- **SLA Status**: Select List (On Track, At Risk, Breached)
- **First Response Time Target**: Number (minutes) - Auto-set dựa trên Severity
- **First Response Time Actual**: Number (minutes) - Auto-calculated
- **Resolution Time Target**: Number (hours) - Auto-set dựa trên Severity
- **Resolution Time Actual**: Number (hours) - Auto-calculated
- **SLA Breach**: Yes/No - Auto-set khi vượt SLA
- **Escalation Level**: Select List (None, Level 1, Level 2, Level 3)
- **Escalation Reason**: Text Area

#### Time Tracking Fields:
- **Created Time**: DateTime (auto)
- **Acknowledged Time**: DateTime (khi transition to Acknowledged)
- **First Response Time**: Number (minutes) - Calculated: Acknowledged Time - Created Time
- **Resolved Time**: DateTime (khi transition to Resolved)
- **Resolution Time**: Number (hours) - Calculated: Resolved Time - Created Time
- **Closed Time**: DateTime (khi transition to Closed)

### 1.3. SLA Calculation Rules

#### First Response Time:
- **Start**: Khi issue được tạo (Created Time)
- **End**: Khi issue được transition sang "Acknowledged"
- **Target**: Dựa trên Severity (15 phút, 1 giờ, 4 giờ, 1 ngày)
- **At Risk**: 80% của target time
- **Breached**: Vượt quá target time

#### Resolution Time:
- **Start**: Khi issue được tạo (Created Time)
- **End**: Khi issue được transition sang "Resolved"
- **Target**: Dựa trên Severity (4 giờ, 8 giờ, 24 giờ, 3 ngày)
- **At Risk**: 80% của target time
- **Breached**: Vượt quá target time

### 1.4. Automation Rules

#### Auto-assignment:
- **SEV1**: Auto-assign → SRE on-call team
- **SEV2**: Auto-assign → Support team lead
- **SEV3-SEV4**: Auto-assign → Support team (round-robin)

#### Auto-escalation:
- **SEV1**: 
  - Escalate to Level 1 (SRE Lead) nếu chưa acknowledged sau 15 phút
  - Escalate to Level 2 (VP Engineering) nếu chưa resolved sau 2 giờ
  - Escalate to Level 3 (C-level) nếu chưa resolved sau 3 giờ
- **SEV2**:
  - Escalate to Level 1 (Support Manager) nếu chưa acknowledged sau 1 giờ
  - Escalate to Level 2 (SRE Lead) nếu chưa resolved sau 6 giờ
- **SEV3**:
  - Escalate to Level 1 (Support Lead) nếu chưa acknowledged sau 4 giờ
- **SEV4**: Không auto-escalate

#### Auto-notification:
- **SEV1**: Notify SRE team, Support Manager, VP Engineering ngay khi tạo
- **SEV2**: Notify Support team, SRE team khi tạo
- **SEV3-SEV4**: Notify Support team khi tạo
- **SLA Breach**: Notify Support Manager, SRE Lead
- **Escalation**: Notify escalation level tương ứng

#### Auto-status update:
- **SLA Status = At Risk**: Khi đạt 80% target time
- **SLA Status = Breached**: Khi vượt target time
- **Escalation Level**: Auto-update khi escalate

### 1.5. Business Hours

- **SEV1-SEV2**: 24/7 (tất cả thời gian)
- **SEV3-SEV4**: Business Hours (8:00-18:00, Monday-Friday)

**Lưu ý**: SLA timer chỉ chạy trong business hours cho SEV3-SEV4.

---

## 2. CHANGE REQUEST - SLA CONFIGURATION

### 2.1. Change Types & SLA Targets

| Change Type | Mô tả | Review Time | Approval Time | Implementation Time | Total SLA |
|-------------|-------|-------------|---------------|---------------------|-----------|
| **Standard Change** | Pre-approved, low risk, thường xuyên | N/A (pre-approved) | N/A | **2 ngày** | **2 ngày** |
| **Normal Change** | Cần CAB approval, medium risk | **2 ngày** | **3 ngày** | **5 ngày** | **10 ngày** |
| **Emergency Change** | Urgent, cần 2 CAB members approval | **2 giờ** | **4 giờ** | **1 ngày** | **1.5 ngày** |

### 2.2. Custom Fields cho SLA Tracking

#### SLA Fields:
- **SLA Status**: Select List (On Track, At Risk, Breached)
- **Review Time Target**: Number (hours/days) - Dựa trên Change Type
- **Review Time Actual**: Number (hours/days) - Auto-calculated
- **Approval Time Target**: Number (hours/days) - Dựa trên Change Type
- **Approval Time Actual**: Number (hours/days) - Auto-calculated
- **Implementation Time Target**: Number (days) - Dựa trên Change Type
- **Implementation Time Actual**: Number (days) - Auto-calculated
- **Total SLA Target**: Number (days) - Dựa trên Change Type
- **Total SLA Actual**: Number (days) - Auto-calculated
- **SLA Breach**: Yes/No - Auto-set khi vượt SLA

#### Time Tracking Fields:
- **Submitted Time**: DateTime (khi transition to Submitted)
- **Under Review Time**: DateTime (khi transition to Under Review)
- **CAB Review Time**: DateTime (khi transition to CAB Review)
- **Approved Time**: DateTime (khi transition to Approved)
- **Implementation Start Time**: DateTime (khi transition to Implementation)
- **Completed Time**: DateTime (khi transition to Completed)
- **Review Duration**: Number (hours) - Calculated
- **Approval Duration**: Number (hours) - Calculated
- **Implementation Duration**: Number (days) - Calculated

### 2.3. SLA Calculation Rules

#### Standard Change:
- **Review Time**: N/A (pre-approved)
- **Approval Time**: N/A (pre-approved)
- **Implementation Time**: 2 ngày từ khi Submitted
- **Total SLA**: 2 ngày

#### Normal Change:
- **Review Time**: 2 ngày từ Submitted → Under Review
- **Approval Time**: 3 ngày từ Under Review → Approved (bao gồm CAB Review)
- **Implementation Time**: 5 ngày từ Approved → Completed
- **Total SLA**: 10 ngày (2 + 3 + 5)

#### Emergency Change:
- **Review Time**: 2 giờ từ Submitted → Under Review
- **Approval Time**: 4 giờ từ Under Review → Approved (cần 2 CAB members)
- **Implementation Time**: 1 ngày từ Approved → Completed
- **Total SLA**: 1.5 ngày (2 giờ + 4 giờ + 1 ngày)

### 2.4. Automation Rules

#### Auto-assignment:
- **Standard Change**: Auto-assign → SRE/DevOps team
- **Normal Change**: Auto-assign → Change Manager
- **Emergency Change**: Auto-assign → Change Manager + SRE Lead

#### Auto-escalation:
- **Normal Change**:
  - Escalate nếu Review Time > 2 ngày
  - Escalate nếu Approval Time > 3 ngày
  - Escalate nếu Implementation Time > 5 ngày
- **Emergency Change**:
  - Escalate nếu Review Time > 2 giờ
  - Escalate nếu Approval Time > 4 giờ
  - Escalate nếu Implementation Time > 1 ngày

#### Auto-notification:
- **Normal Change**: Notify CAB members khi vào CAB Review
- **Emergency Change**: Notify 2 CAB members + SRE Lead ngay khi tạo
- **SLA Breach**: Notify Change Manager, CAB Lead
- **Approval Required**: Remind CAB members mỗi 12 giờ nếu chưa approve

#### Auto-status update:
- **SLA Status = At Risk**: Khi đạt 80% target time
- **SLA Status = Breached**: Khi vượt target time

### 2.5. Business Hours

- **Standard Change**: Business Hours (8:00-18:00, Monday-Friday)
- **Normal Change**: Business Hours (8:00-18:00, Monday-Friday)
- **Emergency Change**: 24/7 (tất cả thời gian)

---

## 3. SERVICE REQUEST - SLA CONFIGURATION

### 3.1. Request Types & SLA Targets

| Request Type | Mô tả | Response Time | Fulfillment Time | Total SLA |
|--------------|-------|---------------|------------------|-----------|
| **Access Request** | Yêu cầu quyền truy cập | **2 giờ** | **1 ngày** | **1 ngày** |
| **Information Request** | Yêu cầu thông tin | **1 giờ** | **4 giờ** | **4 giờ** |
| **Service Provisioning** | Cung cấp dịch vụ mới | **4 giờ** | **3 ngày** | **3 ngày** |
| **Other** | Yêu cầu khác | **4 giờ** | **5 ngày** | **5 ngày** |

### 3.2. Custom Fields cho SLA Tracking

#### SLA Fields:
- **SLA Status**: Select List (On Track, At Risk, Breached)
- **Response Time Target**: Number (hours) - Dựa trên Request Type
- **Response Time Actual**: Number (hours) - Auto-calculated
- **Fulfillment Time Target**: Number (hours/days) - Dựa trên Request Type
- **Fulfillment Time Actual**: Number (hours/days) - Auto-calculated
- **Total SLA Target**: Number (hours/days) - Dựa trên Request Type
- **Total SLA Actual**: Number (hours/days) - Auto-calculated
- **SLA Breach**: Yes/No - Auto-set khi vượt SLA
- **SLA Target Date**: Date - Auto-calculated từ Created Date + SLA Target

#### Time Tracking Fields:
- **Created Time**: DateTime (auto)
- **In Progress Time**: DateTime (khi transition to In Progress)
- **Response Time**: Number (hours) - Calculated: In Progress Time - Created Time
- **Fulfilled Time**: DateTime (khi transition to Fulfilled)
- **Fulfillment Time**: Number (hours/days) - Calculated: Fulfilled Time - In Progress Time
- **Closed Time**: DateTime (khi transition to Closed)

### 3.3. SLA Calculation Rules

#### Access Request:
- **Response Time**: 2 giờ từ Created → In Progress
- **Fulfillment Time**: 1 ngày từ In Progress → Fulfilled
- **Total SLA**: 1 ngày

#### Information Request:
- **Response Time**: 1 giờ từ Created → In Progress
- **Fulfillment Time**: 4 giờ từ In Progress → Fulfilled
- **Total SLA**: 4 giờ

#### Service Provisioning:
- **Response Time**: 4 giờ từ Created → In Progress
- **Fulfillment Time**: 3 ngày từ In Progress → Fulfilled
- **Total SLA**: 3 ngày

#### Other:
- **Response Time**: 4 giờ từ Created → In Progress
- **Fulfillment Time**: 5 ngày từ In Progress → Fulfilled
- **Total SLA**: 5 ngày

### 3.4. Automation Rules

#### Auto-assignment:
- **Access Request**: Auto-assign → Support team (Access Management)
- **Information Request**: Auto-assign → Support team (round-robin)
- **Service Provisioning**: Auto-assign → Support team lead
- **Other**: Auto-assign → Support team (round-robin)

#### Auto-escalation:
- **Access Request**: Escalate nếu Response Time > 2 giờ hoặc Fulfillment Time > 1 ngày
- **Information Request**: Escalate nếu Response Time > 1 giờ hoặc Fulfillment Time > 4 giờ
- **Service Provisioning**: Escalate nếu Response Time > 4 giờ hoặc Fulfillment Time > 3 ngày
- **Other**: Escalate nếu Response Time > 4 giờ hoặc Fulfillment Time > 5 ngày

#### Auto-notification:
- **All Types**: Notify Support team khi tạo
- **SLA Breach**: Notify Support Manager
- **Approval Required**: Notify approver (Manager/PO) khi vào Pending Approval

#### Auto-status update:
- **SLA Status = At Risk**: Khi đạt 80% target time
- **SLA Status = Breached**: Khi vượt target time
- **SLA Target Date**: Auto-calculate và set

### 3.5. Business Hours

- **Tất cả Request Types**: Business Hours (8:00-18:00, Monday-Friday)

---

## 4. SERVICE ORDER - SLA CONFIGURATION

### 4.1. Order Types & SLA Targets

| Order Stage | Mô tả | SLA Target | Notes |
|-------------|-------|------------|-------|
| **Order Received → Processing** | Xác nhận đơn hàng | **2 giờ** | Business hours |
| **Processing → Payment Pending** | Xử lý đơn hàng, chờ thanh toán | **1 ngày** | Business hours |
| **Payment Pending → In Production** | Xác nhận thanh toán, bắt đầu sản xuất | **1 ngày** | Sau khi payment confirmed |
| **In Production → Shipped** | Sản xuất và giao hàng | **Theo Delivery Date** | Dựa trên order terms |
| **Shipped → Delivered** | Giao hàng đến khách hàng | **Theo Delivery Date** | Dựa trên shipping terms |

### 4.2. Custom Fields cho SLA Tracking

#### SLA Fields:
- **SLA Status**: Select List (On Track, At Risk, Breached)
- **Processing Time Target**: Number (hours) - 2 giờ
- **Processing Time Actual**: Number (hours) - Auto-calculated
- **Payment Confirmation Time Target**: Number (days) - 1 ngày
- **Payment Confirmation Time Actual**: Number (days) - Auto-calculated
- **Production Start Time Target**: Number (days) - 1 ngày sau payment
- **Production Start Time Actual**: Number (days) - Auto-calculated
- **Delivery Date**: Date - Từ order terms
- **Delivery SLA Status**: Select List (On Track, At Risk, Breached)
- **SLA Breach**: Yes/No - Auto-set khi vượt SLA

#### Time Tracking Fields:
- **Order Received Time**: DateTime (khi transition to Order Received)
- **Processing Start Time**: DateTime (khi transition to Processing)
- **Payment Pending Time**: DateTime (khi transition to Payment Pending)
- **Payment Confirmed Time**: DateTime (khi payment status = Paid)
- **In Production Time**: DateTime (khi transition to In Production)
- **Shipped Time**: DateTime (khi transition to Shipped)
- **Delivered Time**: DateTime (khi transition to Delivered)
- **Processing Duration**: Number (hours) - Calculated
- **Payment Confirmation Duration**: Number (days) - Calculated
- **Production Duration**: Number (days) - Calculated

### 4.3. SLA Calculation Rules

#### Order Processing:
- **Processing Time**: 2 giờ từ Order Received → Processing
- **Payment Confirmation**: 1 ngày từ Processing → Payment Confirmed
- **Production Start**: 1 ngày từ Payment Confirmed → In Production
- **Delivery**: Dựa trên Delivery Date trong order terms

### 4.4. Automation Rules

#### Auto-assignment:
- **Order Received**: Auto-assign → Support team (Order Management)
- **Payment Pending**: Auto-assign → Finance team (nếu có)
- **In Production**: Auto-assign → Manufacturing team (nếu có)

#### Auto-escalation:
- **Processing**: Escalate nếu Processing Time > 2 giờ
- **Payment**: Escalate nếu Payment Confirmation > 1 ngày
- **Production**: Escalate nếu Production Start > 1 ngày sau payment
- **Delivery**: Escalate nếu Delivery Date đã qua và chưa Shipped

#### Auto-notification:
- **Order Received**: Notify Support team, Customer
- **Payment Pending**: Notify Finance team, Customer
- **Payment Confirmed**: Notify Manufacturing team, Customer
- **Shipped**: Notify Customer với tracking info
- **Delivered**: Notify Customer, Support team
- **SLA Breach**: Notify Support Manager, Customer

#### Auto-status update:
- **SLA Status = At Risk**: Khi đạt 80% target time
- **SLA Status = Breached**: Khi vượt target time
- **Delivery SLA Status**: Dựa trên Delivery Date

### 4.5. Business Hours

- **Tất cả stages**: Business Hours (8:00-18:00, Monday-Friday)
- **Delivery**: Có thể ngoài business hours tùy shipping terms

---

## 5. SLA CUSTOM FIELDS TỔNG HỢP

### 5.1. Common SLA Fields (cho tất cả ITIL issue types)

| Field Name | Field Type | Description | Auto-calculated |
|------------|------------|-------------|-----------------|
| **SLA Status** | Select List | On Track, At Risk, Breached | ✅ Yes |
| **SLA Breach** | Yes/No | Có vượt SLA không | ✅ Yes |
| **SLA Target Date** | Date | Ngày target hoàn thành | ✅ Yes |
| **Created Time** | DateTime | Thời gian tạo issue | ✅ Yes |
| **First Response Time** | Number | Thời gian phản hồi đầu tiên | ✅ Yes |
| **Resolution/Fulfillment Time** | Number | Thời gian xử lý/hoàn thành | ✅ Yes |

### 5.2. Issue Type Specific Fields

#### Incident:
- First Response Time Target (minutes)
- First Response Time Actual (minutes)
- Resolution Time Target (hours)
- Resolution Time Actual (hours)
- Escalation Level
- Escalation Reason

#### Change Request:
- Review Time Target (hours/days)
- Review Time Actual (hours/days)
- Approval Time Target (hours/days)
- Approval Time Actual (hours/days)
- Implementation Time Target (days)
- Implementation Time Actual (days)

#### Service Request:
- Response Time Target (hours)
- Response Time Actual (hours)
- Fulfillment Time Target (hours/days)
- Fulfillment Time Actual (hours/days)

#### Service Order:
- Processing Time Target (hours)
- Processing Time Actual (hours)
- Payment Confirmation Time Target (days)
- Payment Confirmation Time Actual (days)
- Production Start Time Target (days)
- Production Start Time Actual (days)
- Delivery Date
- Delivery SLA Status

---

## 6. SLA AUTOMATION RULES

### 6.1. Common Automation Rules

#### SLA Status Calculation:
```
IF (Current Time - Start Time) >= (Target Time * 0.8) AND (Current Time - Start Time) < Target Time:
    SLA Status = "At Risk"
ELSE IF (Current Time - Start Time) >= Target Time:
    SLA Status = "Breached"
    SLA Breach = Yes
ELSE:
    SLA Status = "On Track"
```

#### Auto-escalation:
- **At Risk**: Notify assignee, team lead
- **Breached**: Notify manager, escalate to next level

#### Auto-notification:
- **SLA At Risk**: Email/Slack notification 2 giờ trước khi breach
- **SLA Breached**: Email/Slack notification ngay khi breach
- **Daily SLA Report**: Gửi báo cáo SLA compliance hàng ngày

### 6.2. Issue Type Specific Automation

#### Incident:
- Auto-assign dựa trên Severity
- Auto-escalate dựa trên Severity và time
- Auto-create Change Request nếu cần permanent fix

#### Change Request:
- Auto-assign dựa trên Change Type
- Auto-notify CAB members khi vào CAB Review
- Auto-remind CAB members nếu chưa approve sau 12 giờ

#### Service Request:
- Auto-assign dựa trên Request Type
- Auto-approve Information Request
- Auto-notify approver khi cần approval

#### Service Order:
- Auto-assign dựa trên stage
- Auto-notify customer ở mỗi stage
- Auto-escalate nếu delivery date sắp đến

---

## 7. SLA REPORTING & DASHBOARDS

### 7.1. SLA Metrics

#### Incident:
- SLA Compliance Rate (%)
- Average First Response Time (minutes)
- Average Resolution Time (hours)
- SLA Breach Count
- Breach Rate by Severity

#### Change Request:
- SLA Compliance Rate (%)
- Average Review Time
- Average Approval Time
- Average Implementation Time
- SLA Breach Count by Change Type

#### Service Request:
- SLA Compliance Rate (%)
- Average Response Time
- Average Fulfillment Time
- SLA Breach Count by Request Type

#### Service Order:
- SLA Compliance Rate (%)
- Average Processing Time
- Average Payment Confirmation Time
- Average Production Start Time
- On-time Delivery Rate (%)

### 7.2. SLA Dashboards

#### Support Dashboard (cho Incident & Service Request):
- SLA Compliance Rate (Gauge)
- SLA Breach Count (Bar Chart)
- Average Response/Resolution Time (Line Chart)
- SLA Status Distribution (Pie Chart)
- Top Breached Issues (Table)

#### Change Management Dashboard:
- Change SLA Compliance Rate (Gauge)
- Average Review/Approval/Implementation Time (Bar Chart)
- SLA Breach by Change Type (Bar Chart)
- Change Request Aging (Table)

#### Service Order Dashboard:
- Order SLA Compliance Rate (Gauge)
- Average Processing Time (Bar Chart)
- On-time Delivery Rate (Gauge)
- Orders at Risk (Table)

---

## 8. JQL QUERIES CHO SLA

### 8.1. Incident SLA Queries

```jql
# Incidents đang At Risk
project = "PROJECT" AND issuetype = Incident AND "SLA Status" = "At Risk"

# Incidents đã Breached
project = "PROJECT" AND issuetype = Incident AND "SLA Status" = "Breached"

# SEV1 Incidents chưa acknowledged sau 15 phút
project = "PROJECT" AND issuetype = Incident AND Severity = SEV1 AND status != "Acknowledged" AND created <= -15m

# Incidents vượt Resolution SLA
project = "PROJECT" AND issuetype = Incident AND "SLA Status" = "Breached" AND "SLA Breach" = Yes
```

### 8.2. Change Request SLA Queries

```jql
# Change Requests đang At Risk
project = "PROJECT" AND issuetype = "Change Request" AND "SLA Status" = "At Risk"

# Change Requests chờ CAB approval quá 3 ngày
project = "PROJECT" AND issuetype = "Change Request" AND status = "CAB Review" AND updated <= -3d

# Emergency Changes chưa approved sau 4 giờ
project = "PROJECT" AND issuetype = "Change Request" AND "Change Type" = "Emergency" AND status = "CAB Review" AND updated <= -4h
```

### 8.3. Service Request SLA Queries

```jql
# Service Requests đang At Risk
project = "PROJECT" AND issuetype = "Service Request" AND "SLA Status" = "At Risk"

# Access Requests chưa fulfilled sau 1 ngày
project = "PROJECT" AND issuetype = "Service Request" AND "Request Type" = "Access Request" AND status != "Fulfilled" AND created <= -1d

# Service Requests đã Breached
project = "PROJECT" AND issuetype = "Service Request" AND "SLA Status" = "Breached"
```

### 8.4. Service Order SLA Queries

```jql
# Service Orders đang At Risk
project = "PROJECT" AND issuetype = "Service Order" AND "SLA Status" = "At Risk"

# Orders chưa processed sau 2 giờ
project = "PROJECT" AND issuetype = "Service Order" AND status = "Order Received" AND created <= -2h

# Orders sắp đến delivery date
project = "PROJECT" AND issuetype = "Service Order" AND "Delivery Date" <= +3d AND status != "Delivered"
```

---

## 9. IMPLEMENTATION CHECKLIST

### 9.1. Custom Fields Setup
- [ ] Tạo SLA Status field (Select List)
- [ ] Tạo SLA Breach field (Yes/No)
- [ ] Tạo SLA Target Date field (Date)
- [ ] Tạo time tracking fields cho từng issue type
- [ ] Tạo calculated fields cho actual times

### 9.2. Automation Rules Setup
- [ ] Auto-calculate SLA Status
- [ ] Auto-set SLA Breach
- [ ] Auto-assignment rules
- [ ] Auto-escalation rules
- [ ] Auto-notification rules

### 9.3. SLA Configuration
- [ ] Configure Incident SLA (SEV1-SEV4)
- [ ] Configure Change Request SLA (Standard, Normal, Emergency)
- [ ] Configure Service Request SLA (Access, Information, Provisioning, Other)
- [ ] Configure Service Order SLA (Processing, Payment, Production, Delivery)

### 9.4. Dashboards & Reports
- [ ] Tạo SLA Compliance Dashboard
- [ ] Tạo SLA Breach Report
- [ ] Tạo SLA Metrics Report
- [ ] Setup daily SLA reports

---

## 10. BEST PRACTICES

### 10.1. SLA Definition
- ✅ Định nghĩa SLA rõ ràng, có thể đo lường được
- ✅ Phân biệt business hours và 24/7
- ✅ Có escalation path rõ ràng
- ✅ Review và điều chỉnh SLA định kỳ

### 10.2. SLA Monitoring
- ✅ Monitor SLA status real-time
- ✅ Alert khi At Risk (80% target)
- ✅ Escalate khi Breached
- ✅ Review SLA compliance hàng tuần

### 10.3. SLA Improvement
- ✅ Phân tích root cause của SLA breaches
- ✅ Cải thiện processes để đáp ứng SLA
- ✅ Training team về SLA requirements
- ✅ Điều chỉnh SLA nếu không realistic

---

**Tài liệu này cung cấp framework đầy đủ để cấu hình và quản lý SLA cho tất cả 4 ITIL issue types cơ bản.**
