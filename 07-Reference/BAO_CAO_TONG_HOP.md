# BÁO CÁO TỔNG HỢP - JIRA SYSTEM

Tài liệu này tổng hợp các báo cáo và metrics quan trọng trong hệ thống Jira.

---

## 📋 MỤC LỤC

1. [Báo cáo Agile/Development](#1-báo-cáo-agiledevelopment)
2. [Báo cáo ITIL/Service Management](#2-báo-cáo-itilservice-management)
3. [Báo cáo Effort Tracking](#3-báo-cáo-effort-tracking)
4. [Báo cáo Performance](#4-báo-cáo-performance)
5. [Báo cáo Management](#5-báo-cáo-management)

---

## 1. BÁO CÁO AGILE/DEVELOPMENT

### 1.1. Velocity Report

**Mục đích**: Track team velocity qua các sprint

**JQL Query**:
```jql
project = PROJ AND type = Story AND sprint in openSprints()
```

**Metrics**:
- Story Points completed per sprint
- Velocity trend
- Velocity average

**Dashboard**: Development Dashboard

---

### 1.2. Sprint Burndown

**Mục đích**: Track progress trong sprint

**JQL Query**:
```jql
project = PROJ AND sprint = "Sprint 1" AND type in (Story, Task, Bug)
```

**Metrics**:
- Remaining story points
- Burndown rate
- Forecast completion

**Dashboard**: Development Dashboard

---

### 1.3. Epic Progress

**Mục đích**: Track progress của Epic

**JQL Query**:
```jql
project = PROJ AND type = Epic AND status != Done
```

**Metrics**:
- Epic completion %
- Stories completed
- Remaining effort

**Dashboard**: Product Owner Dashboard

---

## 2. BÁO CÁO ITIL/SERVICE MANAGEMENT

### 2.1. Incident Report

**Mục đích**: Track incidents và resolution time

**JQL Query**:
```jql
project = PROJ AND type = Incident AND created >= -30d
```

**Metrics**:
- Total incidents
- Resolution time (average, median)
- Incidents by severity
- Incidents by status

**Dashboard**: Support Dashboard

---

### 2.2. SLA Compliance

**Mục đích**: Track SLA compliance

**JQL Query**:
```jql
project = PROJ AND type = Incident AND "SLA Status" = "Breached"
```

**Metrics**:
- SLA compliance %
- Breached SLAs
- Average resolution time vs SLA

**Dashboard**: Support Dashboard, SLA Management Dashboard

---

### 2.3. Change Request Report

**Mục đích**: Track change requests

**JQL Query**:
```jql
project = PROJ AND type = "Change Request" AND created >= -30d
```

**Metrics**:
- Total change requests
- Approved vs Rejected
- Implementation success rate
- Average implementation time

**Dashboard**: Support Dashboard

---

## 3. BÁO CÁO EFFORT TRACKING

### 3.1. Effort Summary by Phase

**Mục đích**: Tổng hợp effort theo phase

**JQL Query**:
```jql
project = PROJ AND "Total Effort" > 0
```

**Metrics**:
- Total effort by phase (Research, Development, Testing, Deployment, Operations, Review, Documentation, Coordination)
- Effort distribution %
- Effort trend over time

**Dashboard**: Effort Summary Dashboard

---

### 3.2. Effort by Issue Type

**Mục đích**: Effort breakdown theo issue type

**JQL Query**:
```jql
project = PROJ AND "Total Effort" > 0
```

**Metrics**:
- Average effort per issue type
- Total effort per issue type
- Effort distribution by issue type

**Dashboard**: Effort Summary Dashboard

---

### 3.3. Effort Variance Report

**Mục đích**: So sánh Estimated vs Actual effort

**JQL Query**:
```jql
project = PROJ AND "Effort Variance" is not EMPTY
```

**Metrics**:
- Effort variance %
- Over-estimation vs Under-estimation
- Variance trend

**Dashboard**: Advanced Effort Dashboard

---

### 3.4. Effort by Customer/Product

**Mục đích**: Effort breakdown theo customer/product

**JQL Query**:
```jql
project = PROJ AND "Work Type" = Project AND Customer is not EMPTY AND "Total Effort" > 0
```

**Metrics**:
- Total effort per customer
- Average effort per customer
- Effort distribution by customer

**Dashboard**: Effort Summary Dashboard

---

## 4. BÁO CÁO PERFORMANCE

**Xem chi tiết**: [05-Effort-Tracking/DANH_GIA_STORY_POINT_PERFORMANCE.md](../05-Effort-Tracking/DANH_GIA_STORY_POINT_PERFORMANCE.md)

### 4.1. Team Performance

**Mục đích**: Đánh giá performance của team

**Metrics**:
- Velocity (Story Points per sprint)
- Throughput (Story Points per hour)
- Cycle time per Story Point
- Sprint Goal Achievement
- Epic Completion Rate

**Dashboard**: Development Dashboard, Executive Dashboard

---

### 4.2. Individual Performance

**Mục đích**: Đánh giá performance của team members

**Metrics**:
- Individual Velocity (Story Points per sprint)
- SP/Hour (Story Points per hour)
- Bug Rate (Bugs per Story Point)
- Estimation Accuracy
- Contribution %

**Dashboard**: Individual Performance Dashboard

---

### 4.3. Quality Metrics

**Mục đích**: Track quality metrics

**Metrics**:
- Bug rate (bugs per Story Point)
- Bug resolution time
- Defect leakage rate
- Code review quality

**Dashboard**: Development Dashboard

---

## 5. BÁO CÁO MANAGEMENT

### 5.1. Executive Summary

**Mục đích**: Tổng quan cho management

**Metrics**:
- Total issues
- Issues by status
- Issues by priority
- Effort summary
- Key metrics trends

**Dashboard**: Executive Dashboard

---

### 5.2. Resource Utilization

**Mục đích**: Track resource utilization

**Metrics**:
- Effort by team member
- Effort by role
- Utilization rate
- Capacity vs Actual

**Dashboard**: Executive Dashboard

---

## 📊 DASHBOARD CONFIGURATION

### Executive Dashboard

**Gadgets**:
1. Issue Statistics
2. Created vs Resolved Chart
3. Effort Summary Chart
4. Priority Distribution
5. Status Distribution

---

### Development Dashboard

**Gadgets**:
1. Sprint Burndown
2. Velocity Chart
3. Epic Progress
4. Effort by Phase
5. Bug Rate

---

### Support Dashboard

**Gadgets**:
1. Incident Statistics
2. SLA Compliance
3. Resolution Time
4. Change Request Status
5. Service Request Fulfillment

---

### Effort Summary Dashboard

**Gadgets**:
1. Effort by Phase (Pie Chart)
2. Effort Trend (Line Chart)
3. Effort by Issue Type
4. Effort by Customer/Product
5. Effort Variance

---

## 📈 REPORTING SCHEDULE

### Daily Reports
- Incident summary
- Active issues

### Weekly Reports
- Sprint progress
- Effort summary
- SLA compliance

### Monthly Reports
- Velocity report
- Effort analysis
- Performance metrics
- Executive summary

### Quarterly Reports
- Comprehensive analysis
- Trends analysis
- Improvement recommendations

---

**Các báo cáo này giúp track progress, identify issues, và make data-driven decisions.**
