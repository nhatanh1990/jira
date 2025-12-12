# JQL QUERIES - THƯ VIỆN TRUY VẤN JIRA

## 1. AGILE QUERIES

### Sprint & Backlog
```jql
-- Tất cả issues trong sprint hiện tại
project = PROJ AND sprint in openSprints() AND type in (Story, Task, Bug)

-- Backlog chưa được assign sprint
project = PROJ AND type in (Story, Task) AND sprint is EMPTY

-- Epic với tất cả stories
project = PROJ AND type = Epic AND "Epic Link" is not EMPTY
```

### My Work
```jql
-- Issues được assign cho tôi
assignee = currentUser() AND status != Done AND status != Closed

-- Issues tôi đang làm
assignee = currentUser() AND status = "In Progress"

-- Issues tôi đã tạo
reporter = currentUser() AND created >= -7d
```

### Story & Task Management
```jql
-- Stories chưa có story points
type = Story AND "Story Points" is EMPTY

-- Tasks quá estimate
type = Task AND "Time Spent" > "Original Estimate"

-- Stories liên quan đến AI
type = Story AND "AI Feature Type" is not EMPTY

-- Issues liên quan đến Manufacturing
"Manufacturing Process" is not EMPTY AND status != Done
```

### Bug Tracking
```jql
-- Bugs chưa fix
type = Bug AND status != Done AND status != Closed

-- Critical bugs
type = Bug AND severity = Critical

-- Bugs trong production
type = Bug AND environment = Production

-- Bugs liên quan đến AI Model
type = Bug AND "Bug Type" = "AI Model"
```

### Code Review & Testing
```jql
-- Issues đang chờ code review
status = "Code Review"

-- Issues đang testing
status = Testing

-- Issues ready for release
status = "Ready for Release"
```

---

## 2. ITIL QUERIES

### Incident Management
```jql
-- Tất cả incidents đang mở
type = Incident AND status != Closed

-- Critical incidents (SEV1)
type = Incident AND severity = SEV1 AND status != Closed

-- Incidents vượt SLA
type = Incident AND "First Response Time" > 60 AND status != Closed

-- Incidents liên quan đến AI Service
type = Incident AND "Incident Category" = "AI Service"

-- Incidents cần escalation
type = Incident AND status = Escalated

-- Incidents đã resolved nhưng chưa closed
type = Incident AND status = Resolved
```

### Change Management
```jql
-- Change Requests pending approval
type = "Change Request" AND "CAB Approval" = Pending

-- Emergency changes
type = "Change Request" AND "Change Type" = Emergency

-- High risk changes
type = "Change Request" AND "Risk Level" in (High, Critical)

-- Changes liên quan đến AI Model Update
type = "Change Request" AND "Change Category" = "AI Model Update"

-- Changes đang implementation
type = "Change Request" AND status = Implementation

-- Failed changes
type = "Change Request" AND status = Rejected
```

### Service Request
```jql
-- Service Requests đang mở
type = "Service Request" AND status != Closed

-- Service Requests cần approval
type = "Service Request" AND status = "Pending Approval"

-- Service Requests sắp hết SLA
type = "Service Request" AND "SLA Target" <= now() AND status != Closed

-- Access Requests
type = "Service Request" AND "Request Type" = "Access Request"
```

### Service Order
```jql
-- Service Orders đang xử lý
type = "Service Order" AND status in (Processing, "In Production")

-- Service Orders chờ thanh toán
type = "Service Order" AND "Payment Status" = Pending

-- Service Orders đã giao
type = "Service Order" AND status = Delivered
```

---

## 3. PERFORMANCE & METRICS QUERIES

### Effort Tracking
```jql
-- Issues có effort variance cao (>20%)
type in (Task, Story) AND "Effort Variance" > 20

-- Issues chưa có estimate
type in (Task, Story) AND "Original Estimate" is EMPTY

-- Issues đã log work nhưng chưa done
type in (Task, Story) AND "Time Spent" > 0 AND status != Done
```

### Velocity & Sprint
```jql
-- Story points completed trong sprint
project = PROJ AND sprint in closedSprints() AND type = Story AND status = Done

-- Issues completed trong sprint hiện tại
project = PROJ AND sprint in openSprints() AND status = Done

-- Velocity trend (last 5 sprints)
project = PROJ AND type = Story AND status = Done AND sprint in closedSprints() ORDER BY sprint DESC

-- Individual velocity
project = PROJ AND type = Story AND assignee = "john.doe" AND status = Done AND sprint = "Sprint 1"

-- Team velocity comparison
project = PROJ AND type = Story AND status = Done AND sprint in closedSprints() ORDER BY assignee, sprint DESC
```

### Quality Metrics
```jql
-- Bugs found trong sprint
project = PROJ AND sprint in openSprints() AND type = Bug

-- Bugs trong production
type = Bug AND environment = Production AND created >= -30d

-- Defect leakage (bugs found in production)
type = Bug AND environment = Production AND created >= -30d
```

---

## 4. AI & MANUFACTURING QUERIES

### AI Features
```jql
-- Tất cả AI features
"AI Feature Type" is not EMPTY

-- AI Model features
type = Story AND "AI Feature Type" = "ML Model"

-- AI-related bugs
type = Bug AND "Bug Type" = "AI Model"

-- AI incidents
type = Incident AND "Incident Category" = "AI Service"
```

### Manufacturing
```jql
-- Issues liên quan đến Manufacturing
"Manufacturing Process" is not EMPTY

-- Manufacturing issues theo process
"Manufacturing Process" = Assembly AND status != Done

-- Service Orders trong production
type = "Service Order" AND status = "In Production"
```

---

## 5. TEAM MANAGEMENT QUERIES

### Team Workload
```jql
-- Workload của team member
assignee = "user@example.com" AND status != Done AND status != Closed

-- Issues không có assignee
assignee is EMPTY AND status != Done

-- Issues assigned nhưng chưa bắt đầu
assignee is not EMPTY AND status = "To Do"
```

### Component-based
```jql
-- Issues theo component
component = "Frontend" AND status != Done

-- Issues không có component
component is EMPTY AND type in (Story, Task, Bug)
```

---

## 6. TIME-BASED QUERIES

### Recent Activity
```jql
-- Issues tạo trong 7 ngày qua
created >= -7d

-- Issues updated trong 24 giờ
updated >= -24h

-- Issues resolved trong tuần này
resolved >= startOfWeek() AND resolved <= endOfWeek()

-- Issues overdue
duedate < now() AND status != Done AND status != Closed
```

### Historical Analysis
```jql
-- Issues completed trong tháng này
status = Done AND resolved >= startOfMonth() AND resolved <= endOfMonth()

-- Issues tạo trong quý này
created >= startOfQuarter() AND created <= endOfQuarter()
```

---

## 7. COMPLEX QUERIES

### Cross-type Analysis
```jql
-- Incidents liên quan đến Change Requests
type = Incident AND "Related Change Request" is not EMPTY

-- Change Requests liên quan đến Incidents
type = "Change Request" AND "Related Incident" is not EMPTY

-- Bugs từ stories đã release
type = Bug AND issueFunction in linkedIssuesOf("type = Story AND status = Done")
```

### Priority & Severity
```jql
-- High priority issues chưa done
priority in (Highest, High) AND status != Done AND status != Closed

-- Critical issues (any type)
(severity = Critical OR priority = Highest) AND status != Done
```

### Blocked Issues
```jql
-- Issues đang blocked
status = Blocked

-- Issues blocked lâu (>3 ngày)
status = Blocked AND updated <= -3d
```

---

## 8. DASHBOARD QUERIES

### Executive Summary
```jql
-- Tổng số issues đang mở
status != Done AND status != Closed

-- Critical issues tổng hợp
(severity = SEV1 OR priority = Highest) AND status != Closed

-- Issues completed tháng này
status = Done AND resolved >= startOfMonth()
```

### Team Performance
```jql
-- Issues completed bởi team member
assignee = "user@example.com" AND status = Done AND resolved >= -30d

-- Average cycle time (cần tính toán trong dashboard)
status = Done AND resolved >= -30d
```

---

## 9. ADVANCED JQL FUNCTIONS

### Issue Functions
```jql
-- Issues có linked issues
issueFunction in hasLinks()

-- Issues trong Epic
issueFunction in issuesInEpic("PROJ-123")

-- Issues với sub-tasks
issueFunction in subtasksOf("PROJ-123")
```

### Text Search
```jql
-- Tìm kiếm trong summary
summary ~ "authentication"

-- Tìm kiếm trong description
description ~ "bug fix"

-- Tìm kiếm trong comments
comment ~ "approved"
```

### Date Functions
```jql
-- Issues due trong tuần này
duedate >= startOfWeek() AND duedate <= endOfWeek()

-- Issues created trong tháng này
created >= startOfMonth() AND created <= endOfMonth()

-- Issues resolved trong 30 ngày qua
resolved >= -30d
```

---

## 10. QUERIES CHO TỪNG ROLE

### Product Owner
```jql
-- Epic progress
type = Epic AND status != Done

-- Stories cần review
type = Story AND status = "Ready for Release"

-- Change Requests cần approval
type = "Change Request" AND "CAB Approval" = Pending AND assignee = currentUser()
```

### Developer
```jql
-- My assigned issues
assignee = currentUser() AND status != Done

-- Code review queue
status = "Code Review" AND component in (myComponents())

-- My bugs
type = Bug AND assignee = currentUser() AND status != Done
```

### QA/Tester
```jql
-- Issues ready for testing
status = Testing AND component in (myComponents())

-- Bugs tôi tạo
type = Bug AND reporter = currentUser()

-- Test results cần update
status = Testing AND "Testing Results" is EMPTY
```

### Support
```jql
-- My Service Requests
type = "Service Request" AND assignee = currentUser() AND status != Closed

-- My Incidents
type = Incident AND assignee = currentUser() AND status != Closed

-- Incidents cần response
type = Incident AND status = New AND "First Response Time" is EMPTY
```

### SRE/DevOps
```jql
-- SEV1/SEV2 Incidents
type = Incident AND severity in (SEV1, SEV2) AND status != Closed

-- Change Requests cần implement
type = "Change Request" AND status = Implementation AND assignee = currentUser()

-- Ops Tasks
type = "Ops Task" AND status != Done
```

---

## LƯU Ý SỬ DỤNG

1. **Thay thế PROJECT KEY**: Thay `PROJ` bằng project key thực tế
2. **Custom Fields**: Đảm bảo custom field names khớp với cấu hình
3. **Status Names**: Điều chỉnh status names theo workflow thực tế
4. **User References**: Thay `currentUser()` hoặc email cụ thể
5. **Date Ranges**: Điều chỉnh theo nhu cầu (d = days, w = weeks, m = months)

---

## TIPS

- Lưu filters thường dùng để tái sử dụng
- Combine queries với AND/OR cho logic phức tạp
- Sử dụng parentheses để group conditions
- Export results sang CSV để phân tích ngoài Jira
- Sử dụng JQL trong dashboards và reports
