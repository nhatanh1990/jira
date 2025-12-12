# BỔ SUNG ITIL & QUẢN TRỊ TOÀN DIỆN

## MỤC LỤC
1. [ITIL Processes Bổ Sung](#1-itil-processes-bổ-sung)
2. [Phương Pháp Quản Trị](#2-phương-pháp-quản-trị)
3. [Quản Lý Kinh Doanh](#3-quản-lý-kinh-doanh)
4. [Governance & Compliance](#4-governance--compliance)
5. [Advanced Features](#5-advanced-features)
6. [Issue Types Bổ Sung](#6-issue-types-bổ-sung)
7. [Workflows Bổ Sung](#7-workflows-bổ-sung)
8. [Custom Fields Bổ Sung](#8-custom-fields-bổ-sung)
9. [Dashboards Bổ Sung](#9-dashboards-bổ-sung)
10. [Reports Bổ Sung](#10-reports-bổ-sung)

---

## 1. ITIL PROCESSES BỔ SUNG

### 1.1. Problem Management

**Mục đích**: Tìm và giải quyết nguyên nhân gốc rễ của incidents, ngăn chặn incidents tái diễn.

#### Issue Type: Problem
- **Workflow**: 
```
New → Investigating → Root Cause Identified → Workaround Available → Resolved → Closed
                              ↓
                         Known Error
```

#### Custom Fields:
- **Problem Category**: Hardware, Software, Network, AI Service, Manufacturing, Process, Other
- **Root Cause Analysis**: Text Area (chi tiết RCA)
- **Workaround Available**: Yes/No
- **Workaround Description**: Text Area
- **Permanent Fix**: Text Area
- **Known Error**: Yes/No
- **Related Incidents**: Multi-select (link nhiều incidents)
- **Related Change Request**: Issue Link
- **Problem Priority**: P1-P4 (tính từ Impact của related incidents)
- **Investigation Team**: Multi-user picker
- **Resolution Date**: Date Picker
- **Mean Time to Resolve (MTTR)**: Number (hours)

#### Workflow Details:
- **New → Investigating**: Problem Manager assigns team
- **Investigating → Root Cause Identified**: Team xác định root cause
- **Root Cause Identified → Workaround Available**: Tạo workaround tạm thời
- **Workaround Available → Resolved**: Permanent fix được implement
- **Resolved → Closed**: Problem Manager xác nhận
- **Root Cause Identified → Known Error**: Nếu không thể fix ngay, tạo Known Error

#### Automation:
- Tự động tạo Problem khi có 3+ incidents cùng pattern trong 30 ngày
- Link incidents liên quan vào Problem
- Tự động tạo Change Request khi có permanent fix

#### Reports:
- Problem trends
- Top problems by category
- MTTR by problem category
- Known Error database

---

### 1.2. Knowledge Management

**Mục đích**: Quản lý, chia sẻ và tái sử dụng knowledge trong tổ chức.

#### Issue Type: Knowledge Article
- **Workflow**:
```
Draft → Under Review → Published → Archived
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Article Type**: How-to, FAQ, Troubleshooting, Best Practice, Reference, Policy
- **Category**: Technical, Process, Business, AI/ML, Manufacturing, Other
- **Tags**: Multi-select (Labels)
- **Author**: User Picker
- **Reviewer**: User Picker
- **Review Date**: Date Picker
- **Published Date**: Date Picker
- **Last Updated**: Date Picker
- **View Count**: Number (auto-increment)
- **Helpful Count**: Number
- **Related Issues**: Multi-select (link incidents, problems, changes)
- **Search Keywords**: Text (comma-separated)
- **Content**: Rich Text Area
- **Attachments**: Files, Images, Videos

#### Workflow Details:
- **Draft → Under Review**: Author submits for review
- **Under Review → Published**: Knowledge Manager approves
- **Under Review → Rejected**: Knowledge Manager rejects với feedback
- **Published → Archived**: Khi content outdated
- **Archived → Draft**: Khi cần update

#### Integration:
- Link Knowledge Articles từ Incident resolution
- Link từ Problem resolution
- Link từ Change Request documentation
- Search trong Jira Service Management portal

#### Reports:
- Most viewed articles
- Articles by category
- Articles needing update
- Knowledge base coverage

---

### 1.3. Service Level Management (SLA Management)

**Mục đích**: Đảm bảo dịch vụ đáp ứng SLA đã thỏa thuận với khách hàng.

#### Custom Fields (cho Service):
- **Service Name**: Text
- **Service Owner**: User Picker
- **Service Level Agreement**: Text Area
- **SLA Targets**: 
  - First Response Time (minutes)
  - Resolution Time (hours)
  - Availability Target (%)
  - Uptime Target (%)
- **Service Hours**: Business Hours, 24/7, Custom
- **Priority Matrix**: Text Area (Impact × Urgency = Priority)
- **Escalation Rules**: Text Area
- **Service Status**: Active, Inactive, Deprecated
- **Customer**: User Picker / Customer field

#### SLA Tracking:
- **SLA Status**: On Track, At Risk, Breached
- **SLA Compliance Rate**: % (calculated)
- **SLA Breach Count**: Number
- **Average Resolution Time**: Number (hours)
- **Average First Response Time**: Number (minutes)

#### Issue Type: SLA Review
- **Workflow**:
```
Scheduled → In Review → Action Items Created → Completed → Closed
```

#### Custom Fields:
- **Review Period**: Monthly, Quarterly, Annually
- **SLA Performance**: Text Area
- **Breach Analysis**: Text Area
- **Improvement Actions**: Text Area
- **Next Review Date**: Date Picker

#### Reports:
- SLA compliance dashboard
- SLA breach analysis
- Service performance trends
- Customer satisfaction vs SLA

---

### 1.4. Service Catalog Management

**Mục đích**: Quản lý catalog dịch vụ, đảm bảo thông tin chính xác và cập nhật.

#### Issue Type: Service Catalog Item
- **Workflow**:
```
Draft → Under Review → Approved → Published → Deprecated
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Service Name**: Text
- **Service Description**: Rich Text Area
- **Service Category**: Infrastructure, Application, Business Process, AI Service, Manufacturing
- **Service Owner**: User Picker
- **Service Type**: Standard, Premium, Custom
- **Delivery Time**: Text (e.g., "2 business days")
- **Cost**: Number
- **Approval Required**: Yes/No
- **Approval Workflow**: Text Area
- **Prerequisites**: Text Area
- **Related Services**: Multi-select
- **Service Level**: Text Area
- **Available To**: All Users, Specific Groups, Specific Customers
- **Published Date**: Date Picker
- **Last Updated**: Date Picker

#### Integration:
- Link với Service Request
- Link với Service Order
- Display trong Service Portal

---

### 1.5. Availability Management

**Mục đích**: Đảm bảo dịch vụ đáp ứng mức độ sẵn sàng yêu cầu.

#### Issue Type: Availability Incident
- **Workflow**:
```
Detected → Investigating → Mitigated → Resolved → Closed
```

#### Custom Fields:
- **Service Affected**: Service Catalog Item
- **Downtime Start**: Date/Time
- **Downtime End**: Date/Time
- **Total Downtime**: Number (minutes, auto-calculated)
- **Availability Impact**: % (calculated)
- **Root Cause**: Text Area
- **Preventive Actions**: Text Area

#### Availability Metrics:
- **Service Availability**: % (calculated)
- **MTBF (Mean Time Between Failures)**: Number (hours)
- **MTTR (Mean Time To Restore)**: Number (hours)
- **Planned Downtime**: Number (hours)
- **Unplanned Downtime**: Number (hours)

#### Reports:
- Service availability dashboard
- Availability trends
- Downtime analysis
- MTBF/MTTR trends

---

### 1.6. Capacity Management

**Mục đích**: Đảm bảo đủ capacity để đáp ứng nhu cầu hiện tại và tương lai.

#### Issue Type: Capacity Request
- **Workflow**:
```
Requested → Under Review → Approved → Provisioned → Completed → Closed
                ↓
            Rejected → Closed
```

#### Custom Fields:
- **Resource Type**: Compute, Storage, Network, Database, AI/ML Resources, Manufacturing Equipment
- **Current Capacity**: Number
- **Requested Capacity**: Number
- **Justification**: Text Area
- **Business Impact**: High, Medium, Low
- **Urgency**: Critical, High, Medium, Low
- **Estimated Cost**: Number
- **Approval Required**: Yes/No
- **Provisioning Date**: Date Picker
- **Related Service**: Service Catalog Item

#### Capacity Metrics:
- **Utilization Rate**: % (current usage / total capacity)
- **Capacity Trend**: Chart
- **Forecasted Demand**: Number
- **Capacity Gap**: Number (forecasted - current)

#### Reports:
- Capacity utilization dashboard
- Capacity forecast
- Resource allocation
- Cost per resource

---

### 1.7. IT Service Continuity Management

**Mục đích**: Đảm bảo khả năng phục hồi sau thảm họa.

#### Issue Type: Disaster Recovery Plan
- **Workflow**:
```
Draft → Under Review → Approved → Tested → Active → Archived
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Plan Name**: Text
- **Service Covered**: Service Catalog Item
- **RTO (Recovery Time Objective)**: Number (hours)
- **RPO (Recovery Point Objective)**: Number (hours)
- **Recovery Strategy**: Text Area
- **Test Date**: Date Picker
- **Test Results**: Text Area
- **Next Test Date**: Date Picker
- **Plan Owner**: User Picker
- **Status**: Draft, Approved, Active, Archived

#### Issue Type: Disaster Recovery Test
- **Workflow**:
```
Scheduled → In Progress → Completed → Review → Closed
```

#### Custom Fields:
- **Test Type**: Full, Partial, Tabletop
- **Test Date**: Date Picker
- **Test Results**: Text Area
- **Issues Found**: Text Area
- **Improvement Actions**: Text Area
- **Next Test Date**: Date Picker

---

### 1.8. Information Security Management

**Mục đích**: Quản lý bảo mật thông tin và tuân thủ security policies.

#### Issue Type: Security Incident
- **Workflow**:
```
Detected → Classified → Investigating → Contained → Resolved → Closed
              ↓
          Escalated
```

#### Custom Fields:
- **Security Category**: Data Breach, Unauthorized Access, Malware, Phishing, DDoS, Insider Threat, Other
- **Severity**: Critical, High, Medium, Low
- **Data Affected**: Text Area
- **Users Affected**: Number
- **Containment Actions**: Text Area
- **Remediation Actions**: Text Area
- **Compliance Impact**: Text Area
- **Notification Required**: Yes/No
- **Regulatory Reporting**: Yes/No

#### Issue Type: Security Assessment
- **Workflow**:
```
Scheduled → In Progress → Findings → Remediation → Verified → Closed
```

#### Custom Fields:
- **Assessment Type**: Vulnerability Scan, Penetration Test, Security Audit, Compliance Review
- **Scope**: Text Area
- **Findings**: Text Area
- **Risk Level**: Critical, High, Medium, Low
- **Remediation Plan**: Text Area
- **Due Date**: Date Picker
- **Compliance Status**: Compliant, Non-Compliant, Partial

---

### 1.9. Supplier Management

**Mục đích**: Quản lý nhà cung cấp và hợp đồng dịch vụ.

#### Issue Type: Supplier
- **Workflow**:
```
Onboarding → Active → Under Review → Suspended → Terminated
```

#### Custom Fields:
- **Supplier Name**: Text
- **Supplier Type**: Vendor, Partner, Contractor, Consultant
- **Contact Information**: Text Area
- **Services Provided**: Text Area
- **Contract Start Date**: Date Picker
- **Contract End Date**: Date Picker
- **SLA with Supplier**: Text Area
- **Performance Rating**: Excellent, Good, Average, Poor
- **Risk Level**: Low, Medium, High
- **Compliance Status**: Compliant, Non-Compliant

#### Issue Type: Supplier Performance Review
- **Workflow**:
```
Scheduled → In Progress → Completed → Action Items → Closed
```

#### Custom Fields:
- **Review Period**: Monthly, Quarterly, Annually
- **SLA Compliance**: % (calculated)
- **Performance Metrics**: Text Area
- **Issues**: Text Area
- **Improvement Actions**: Text Area
- **Next Review Date**: Date Picker

---

### 1.10. Asset Management

**Mục đích**: Quản lý tài sản IT và lifecycle.

#### Issue Type: IT Asset
- **Workflow**:
```
Procured → In Use → Maintenance → Retired → Disposed
```

#### Custom Fields:
- **Asset Type**: Hardware, Software, License, Cloud Resource, AI/ML Model, Manufacturing Equipment
- **Asset Name**: Text
- **Asset Tag/ID**: Text
- **Manufacturer/Vendor**: Text
- **Model/Version**: Text
- **Serial Number**: Text
- **Purchase Date**: Date Picker
- **Purchase Cost**: Number
- **Warranty Expiry**: Date Picker
- **Location**: Text
- **Assigned To**: User Picker
- **Status**: In Use, In Stock, Maintenance, Retired, Disposed
- **Depreciation**: Number
- **Current Value**: Number

#### Issue Type: Asset Request
- **Workflow**:
```
Requested → Approved → Procured → Deployed → Closed
            ↓
         Rejected → Closed
```

#### Custom Fields:
- **Asset Type**: Hardware, Software, License, Cloud Resource
- **Justification**: Text Area
- **Estimated Cost**: Number
- **Urgency**: Critical, High, Medium, Low
- **Approval Required**: Yes/No

---

### 1.11. Configuration Management (CMDB)

**Mục đích**: Quản lý cấu hình và mối quan hệ giữa các CI (Configuration Items).

#### Issue Type: Configuration Item (CI)
- **Workflow**:
```
Planned → In Development → In Production → Retired → Archived
```

#### Custom Fields:
- **CI Type**: Server, Database, Application, Network Device, Service, AI Model, Manufacturing System
- **CI Name**: Text
- **CI ID**: Text (unique identifier)
- **Version**: Text
- **Status**: Planned, In Development, In Production, Retired, Archived
- **Owner**: User Picker
- **Location**: Text
- **Dependencies**: Multi-select (link other CIs)
- **Related Services**: Multi-select (Service Catalog Items)
- **Configuration Details**: Text Area
- **Last Updated**: Date Picker

#### CI Relationships:
- **Depends On**: Link CIs that this CI depends on
- **Used By**: Link CIs that use this CI
- **Part Of**: Link parent CI
- **Contains**: Link child CIs

---

### 1.12. Release Management

**Mục đích**: Quản lý releases và deployments một cách có kiểm soát.

#### Issue Type: Release
- **Workflow**:
```
Planned → In Development → Testing → Approved → Deployed → Closed
                                    ↓
                                Rejected → In Development
```

#### Custom Fields:
- **Release Name**: Text
- **Release Type**: Major, Minor, Patch, Emergency
- **Release Date**: Date Picker
- **Release Manager**: User Picker
- **Related Version**: Version field
- **Change Requests**: Multi-select
- **Deployment Plan**: Text Area
- **Rollback Plan**: Text Area
- **Test Results**: Text Area
- **Deployment Status**: Not Started, In Progress, Completed, Failed, Rolled Back
- **Deployment Date**: Date Picker
- **Post-Deployment Review**: Text Area

#### Release Metrics:
- **Release Frequency**: Number (releases per month)
- **Release Success Rate**: % (successful / total)
- **Average Deployment Time**: Number (hours)
- **Rollback Rate**: % (rolled back / total)

---

## 2. PHƯƠNG PHÁP QUẢN TRỊ

### 2.1. Kanban

**Mục đích**: Quản lý công việc theo phương pháp Kanban, tập trung vào flow và WIP limits.

#### Kanban Board Configuration:
- **Columns**: Backlog, To Do, In Progress, Code Review, Testing, Done
- **WIP Limits**: 
  - In Progress: 3-5 items per person
  - Code Review: 2-3 items
  - Testing: 2-3 items
- **Swimlanes**: By Priority, By Component, By Team Member

#### Custom Fields:
- **Kanban Board**: Select List
- **WIP Status**: In WIP, Blocked, Waiting
- **Blocked Reason**: Text Area
- **Flow Efficiency**: % (value-add time / total time)

#### Metrics:
- **Cycle Time**: Average time từ To Do → Done
- **Lead Time**: Average time từ tạo issue → Done
- **Throughput**: Số issues completed per week
- **Cumulative Flow Diagram**: Visualize work in progress
- **Flow Efficiency**: % time spent on value-add activities

---

### 2.2. DevOps Practices

**Mục đích**: Tích hợp Development và Operations, tự động hóa pipeline.

#### Issue Type: Deployment
- **Workflow**:
```
Scheduled → In Progress → Testing → Approved → Deployed → Verified → Closed
                                    ↓
                                Failed → Rollback → Closed
```

#### Custom Fields:
- **Environment**: Development, Staging, Production
- **Deployment Type**: Blue-Green, Canary, Rolling, All-at-once
- **Deployment Pipeline**: Text (CI/CD pipeline name)
- **Deployment Time**: Date/Time
- **Rollback Required**: Yes/No
- **Rollback Reason**: Text Area
- **Deployment Logs**: Text Area
- **Health Check Status**: Pass, Fail, Warning

#### DevOps Metrics:
- **Deployment Frequency**: Deployments per day/week
- **Lead Time for Changes**: Time từ commit → production
- **Mean Time to Recovery (MTTR)**: Average time to recover from failure
- **Change Failure Rate**: % of deployments causing incidents

---

### 2.3. Lean Principles

**Mục đích**: Loại bỏ waste, tối ưu hóa flow, tăng giá trị.

#### Waste Categories:
- **Overproduction**: Làm quá nhiều, quá sớm
- **Waiting**: Chờ đợi không cần thiết
- **Transportation**: Di chuyển không cần thiết
- **Over-processing**: Xử lý quá mức
- **Inventory**: Work in progress quá nhiều
- **Motion**: Di chuyển không hiệu quả
- **Defects**: Bugs, rework

#### Custom Fields:
- **Waste Type**: Select from categories above
- **Value Stream**: Text (process flow)
- **Value-Add Time**: Number (hours)
- **Non-Value-Add Time**: Number (hours)
- **Process Efficiency**: % (value-add / total time)

#### Lean Metrics:
- **Value Stream Efficiency**: % value-add time
- **Waste Reduction**: Track waste over time
- **Process Cycle Efficiency**: Value-add time / total lead time

---

### 2.4. Risk Management

**Mục đích**: Nhận diện, đánh giá và quản lý rủi ro.

#### Issue Type: Risk
- **Workflow**:
```
Identified → Assessed → Mitigation Planned → Mitigated → Closed
              ↓
          Accepted → Closed
```

#### Custom Fields:
- **Risk Category**: Technical, Business, Operational, Security, Compliance, Financial
- **Risk Description**: Text Area
- **Probability**: Very High, High, Medium, Low, Very Low
- **Impact**: Critical, High, Medium, Low, Very Low
- **Risk Score**: Number (Probability × Impact, auto-calculated)
- **Risk Owner**: User Picker
- **Mitigation Strategy**: Text Area
- **Mitigation Actions**: Text Area
- **Residual Risk**: Number (after mitigation)
- **Status**: Identified, Assessed, Mitigation Planned, Mitigated, Accepted, Closed

#### Risk Register:
- Track all risks in one place
- Risk heat map (Probability × Impact)
- Risk trends over time
- Top risks dashboard

#### Risk Reports:
- Risk register
- Risk heat map
- Risk trends
- Mitigation status

---

### 2.5. Portfolio Management

**Mục đích**: Quản lý portfolio dự án, tối ưu hóa đầu tư.

#### Issue Type: Portfolio Item
- **Workflow**:
```
Proposed → Under Review → Approved → In Progress → Completed → Closed
              ↓
          Rejected → Closed
```

#### Custom Fields:
- **Portfolio Category**: Strategic, Tactical, Operational, Maintenance
- **Business Value**: Number (1-10)
- **Strategic Alignment**: High, Medium, Low
- **Estimated Cost**: Number
- **Estimated ROI**: Number (%)
- **Resource Requirements**: Text Area
- **Dependencies**: Multi-select (other portfolio items)
- **Risk Level**: High, Medium, Low
- **Priority**: P1-P4
- **Status**: Proposed, Under Review, Approved, In Progress, On Hold, Completed, Cancelled

#### Portfolio Metrics:
- **Portfolio Value**: Total business value
- **Resource Utilization**: % resources allocated
- **ROI by Portfolio**: ROI per category
- **Strategic Alignment Score**: Average alignment score

---

## 3. QUẢN LÝ KINH DOANH

### 3.1. Financial Management

**Mục đích**: Quản lý tài chính IT, cost allocation, budgeting.

#### Custom Fields (cho tất cả issues):
- **Cost Center**: Select List
- **Budget Code**: Text
- **Estimated Cost**: Number
- **Actual Cost**: Number
- **Cost Variance**: Number (Actual - Estimated, auto-calculated)
- **Cost Category**: Labor, Infrastructure, Software, Hardware, Services, Training, Other
- **Chargeback**: Yes/No
- **Customer/Department**: User Picker / Department field

#### Issue Type: Budget
- **Workflow**:
```
Draft → Under Review → Approved → Active → Closed
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Budget Period**: Monthly, Quarterly, Annually
- **Budget Amount**: Number
- **Allocated Amount**: Number
- **Spent Amount**: Number (auto-calculated)
- **Remaining Budget**: Number (auto-calculated)
- **Budget Owner**: User Picker
- **Budget Category**: Select List

#### Financial Reports:
- Budget vs Actual
- Cost by category
- Cost by project
- Cost by department/customer
- ROI analysis
- Chargeback reports

---

### 3.2. Business Relationship Management

**Mục đích**: Quản lý mối quan hệ với khách hàng, đảm bảo satisfaction.

#### Issue Type: Customer
- **Custom Fields**:
- **Customer Name**: Text
- **Customer Type**: Internal, External, Partner
- **Industry**: Text
- **Contact Information**: Text Area
- **Account Manager**: User Picker
- **Customer Status**: Active, Inactive, Prospect
- **SLA Agreement**: Text Area
- **Satisfaction Score**: Number (1-10)

#### Issue Type: Customer Feedback
- **Workflow**:
```
Received → Acknowledged → Action Items → Resolved → Closed
```

#### Custom Fields:
- **Feedback Type**: Complaint, Suggestion, Compliment, Question
- **Customer**: Customer field
- **Satisfaction Rating**: Number (1-10)
- **Feedback Details**: Text Area
- **Action Items**: Text Area
- **Resolution**: Text Area

#### Customer Metrics:
- **Customer Satisfaction (CSAT)**: Average satisfaction score
- **Net Promoter Score (NPS)**: % promoters - % detractors
- **Customer Retention Rate**: % customers retained
- **Response Time**: Average time to respond to feedback

---

### 3.3. Demand Management

**Mục đích**: Dự báo và quản lý nhu cầu dịch vụ.

#### Issue Type: Demand Forecast
- **Workflow**:
```
Draft → Under Review → Approved → Active → Closed
```

#### Custom Fields:
- **Forecast Period**: Monthly, Quarterly, Annually
- **Service**: Service Catalog Item
- **Forecasted Demand**: Number
- **Historical Demand**: Number
- **Growth Rate**: % (calculated)
- **Confidence Level**: High, Medium, Low
- **Assumptions**: Text Area

#### Demand Metrics:
- **Forecast Accuracy**: % (actual vs forecasted)
- **Demand Trends**: Chart over time
- **Peak Demand Periods**: Identify high-demand times
- **Capacity Planning**: Based on demand forecast

---

### 3.4. Business Intelligence & Analytics

**Mục đích**: Phân tích dữ liệu để đưa ra quyết định kinh doanh.

#### Analytics Dashboards:
- **Executive Dashboard**: 
  - KPIs tổng hợp
  - Business metrics
  - Financial overview
  - Strategic initiatives progress

- **Operational Dashboard**:
  - Service performance
  - Team productivity
  - Quality metrics
  - Cost efficiency

- **Predictive Analytics**:
  - Demand forecasting
  - Capacity planning
  - Risk prediction
  - Trend analysis

#### Custom Fields:
- **KPI Target**: Number
- **KPI Actual**: Number
- **KPI Variance**: % (auto-calculated)
- **Trend**: Improving, Stable, Declining
- **Benchmark**: Industry standard or internal target

---

## 4. GOVERNANCE & COMPLIANCE

### 4.1. Governance Framework

**Mục đích**: Đảm bảo tuân thủ policies, standards, và best practices.

#### Issue Type: Policy
- **Workflow**:
```
Draft → Under Review → Approved → Published → Under Review → Archived
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Policy Name**: Text
- **Policy Type**: Security, Quality, Process, Compliance, Other
- **Policy Owner**: User Picker
- **Effective Date**: Date Picker
- **Review Date**: Date Picker
- **Compliance Required**: Yes/No
- **Related Standards**: Text Area (ISO, ITIL, etc.)
- **Policy Content**: Rich Text Area

#### Issue Type: Compliance Audit
- **Workflow**:
```
Scheduled → In Progress → Findings → Remediation → Verified → Closed
```

#### Custom Fields:
- **Audit Type**: Internal, External, Regulatory
- **Compliance Standard**: ISO 27001, ISO 20000, GDPR, SOC 2, Other
- **Scope**: Text Area
- **Findings**: Text Area
- **Non-Compliance Items**: Text Area
- **Remediation Plan**: Text Area
- **Compliance Status**: Compliant, Non-Compliant, Partial
- **Next Audit Date**: Date Picker

---

### 4.2. Audit Trail & Change History

**Mục đích**: Track mọi thay đổi để audit và compliance.

#### Audit Fields:
- **Created By**: User (auto)
- **Created Date**: Date/Time (auto)
- **Updated By**: User (auto)
- **Updated Date**: Date/Time (auto)
- **Change History**: Auto-logged
- **Approval History**: Auto-logged
- **Comment History**: Auto-logged

#### Audit Reports:
- Change history by user
- Change history by date range
- Approval audit trail
- Compliance audit report

---

## 5. ADVANCED FEATURES

### 5.1. Dependency Management

**Mục đích**: Quản lý dependencies giữa các issues, projects, services.

#### Custom Fields:
- **Dependencies**: Multi-select (link issues)
- **Dependency Type**: Blocks, Is Blocked By, Relates To, Duplicates
- **Dependency Status**: Resolved, Unresolved
- **Critical Path**: Yes/No (for project management)

#### Dependency Visualization:
- Dependency graph
- Critical path analysis
- Impact analysis (nếu issue bị delay)

---

### 5.2. Requirements Management

**Mục đích**: Quản lý requirements từ business đến technical.

#### Issue Type: Requirement
- **Workflow**:
```
Draft → Under Review → Approved → In Development → Implemented → Verified → Closed
            ↓
         Rejected → Draft
```

#### Custom Fields:
- **Requirement Type**: Functional, Non-Functional, Business, Technical
- **Priority**: Must Have, Should Have, Could Have, Won't Have (MoSCoW)
- **Source**: Business Stakeholder, Customer, Regulatory, Internal
- **Acceptance Criteria**: Text Area
- **Related Stories**: Multi-select
- **Traceability**: Link to business need, design, test cases

---

### 5.3. Test Management

**Mục đích**: Quản lý test cases, test execution, test results.

#### Issue Type: Test Case
- **Workflow**:
```
Draft → Approved → Ready → In Progress → Passed → Closed
                                    ↓
                                Failed → In Progress
```

#### Custom Fields:
- **Test Type**: Unit, Integration, System, UAT, Performance, Security
- **Test Priority**: Critical, High, Medium, Low
- **Preconditions**: Text Area
- **Test Steps**: Text Area
- **Expected Result**: Text Area
- **Actual Result**: Text Area
- **Test Status**: Pass, Fail, Blocked, Not Executed
- **Related Story/Bug**: Issue Link
- **Test Environment**: Text

#### Test Execution:
- **Test Run**: Group of test cases
- **Test Results**: Pass/Fail/Blocked
- **Defects Found**: Link to bugs
- **Test Coverage**: % (tested / total)

---

## 6. ISSUE TYPES BỔ SUNG - TÓM TẮT

### ITIL Issue Types:
1. **Problem** - Root cause analysis
2. **Knowledge Article** - Knowledge management
3. **SLA Review** - Service level management
4. **Service Catalog Item** - Service catalog
5. **Availability Incident** - Availability management
6. **Capacity Request** - Capacity management
7. **Disaster Recovery Plan** - ITSCM
8. **Disaster Recovery Test** - ITSCM
9. **Security Incident** - Security management
10. **Security Assessment** - Security management
11. **Supplier** - Supplier management
12. **Supplier Performance Review** - Supplier management
13. **IT Asset** - Asset management
14. **Asset Request** - Asset management
15. **Configuration Item (CI)** - CMDB
16. **Release** - Release management

### Quản Trị Issue Types:
17. **Deployment** - DevOps
18. **Risk** - Risk management
19. **Portfolio Item** - Portfolio management
20. **Budget** - Financial management
21. **Customer** - Business relationship
22. **Customer Feedback** - Business relationship
23. **Demand Forecast** - Demand management
24. **Policy** - Governance
25. **Compliance Audit** - Compliance
26. **Requirement** - Requirements management
27. **Test Case** - Test management

---

## 7. WORKFLOWS BỔ SUNG - TÓM TẮT

Xem chi tiết workflows trong các sections trên. Tất cả workflows đều có:
- Status transitions
- Conditions
- Validators
- Post-functions
- Automation rules

---

## 8. CUSTOM FIELDS BỔ SUNG - TÓM TẮT

### Financial Fields:
- Cost Center, Budget Code, Estimated Cost, Actual Cost, Cost Variance, Cost Category, Chargeback

### Risk Fields:
- Risk Category, Probability, Impact, Risk Score, Mitigation Strategy, Residual Risk

### Compliance Fields:
- Compliance Standard, Compliance Status, Audit Type, Findings, Remediation Plan

### Performance Fields:
- KPI Target, KPI Actual, KPI Variance, Trend, Benchmark

### Relationship Fields:
- Dependencies, Related Services, Related CIs, Customer, Supplier

---

## 9. DASHBOARDS BỔ SUNG

### Problem Management Dashboard:
- Problem trends
- Top problems by category
- MTTR by category
- Known Error database

### Knowledge Management Dashboard:
- Most viewed articles
- Articles by category
- Articles needing update
- Knowledge base coverage

### SLA Management Dashboard:
- SLA compliance
- SLA breach analysis
- Service performance trends
- Customer satisfaction vs SLA

### Financial Dashboard:
- Budget vs Actual
- Cost by category
- Cost by project
- ROI analysis
- Chargeback reports

### Risk Management Dashboard:
- Risk register
- Risk heat map
- Risk trends
- Mitigation status

### Compliance Dashboard:
- Compliance status by standard
- Audit findings
- Remediation progress
- Policy compliance

### Portfolio Dashboard:
- Portfolio value
- Resource utilization
- ROI by portfolio
- Strategic alignment

---

## 10. REPORTS BỔ SUNG

### ITIL Reports:
- Problem Management Report
- Knowledge Management Report
- SLA Performance Report
- Availability Report
- Capacity Report
- Security Incident Report
- Supplier Performance Report
- Asset Management Report
- CMDB Report
- Release Management Report

### Business Reports:
- Financial Report
- Customer Satisfaction Report
- Demand Forecast Report
- ROI Report
- Cost Allocation Report

### Governance Reports:
- Compliance Audit Report
- Policy Compliance Report
- Risk Register Report
- Audit Trail Report

---

## IMPLEMENTATION PRIORITY

### Phase 1 (Critical - Implement First):
1. Problem Management
2. Knowledge Management
3. Service Level Management
4. Risk Management
5. Financial Management

### Phase 2 (Important - Implement Next):
6. Service Catalog Management
7. Availability Management
8. Capacity Management
9. Release Management
10. Compliance & Governance

### Phase 3 (Enhancement - Implement Later):
11. IT Service Continuity
12. Security Management
13. Supplier Management
14. Asset Management
15. CMDB
16. Advanced Analytics

---

## NOTES

- Tất cả issue types, workflows, và fields này cần được customize dựa trên nhu cầu cụ thể
- Implement theo priority, không cần implement tất cả cùng lúc
- Test thoroughly trước khi deploy
- Train users về các processes mới
- Document mọi thay đổi
- Continuous improvement dựa trên feedback

---

**Tài liệu này bổ sung cho HUONG_DAN_TRIEN_KHAI_JIRA.md để tạo hệ thống quản lý toàn diện.**
