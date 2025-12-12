# EFFORT TRACKING HOÀN THIỆN - TẤT CẢ ISSUE TYPES

## TỔNG QUAN

Tài liệu này định nghĩa effort tracking fields cho TẤT CẢ issue types (39 types Nâng cao / 8 types Cơ bản), đảm bảo có thể thống kê effort đầy đủ cho mọi loại công việc.

**Lưu ý**: Product Research, Product Development, Product Deployment, Product Operations, Project Research, Project Development, Project Deployment, Project Operations đã được quyết định LOẠI BỎ và thay thế bằng Epic/Story/Task với custom fields. Xem PHAN_TICH_ISSUE_TYPES.md để biết chi tiết.

---

## CẤU TRÚC EFFORT FIELDS

### Effort Fields (Time Tracking):
1. **Research Effort** - Công sức nghiên cứu (hours)
2. **Development Effort** - Công sức phát triển (hours)
3. **Testing Effort** - Công sức testing (hours) - Bổ sung
4. **Deployment Effort** - Công sức triển khai (hours)
5. **Operations Effort** - Công sức vận hành (hours)
6. **Review Effort** - Công sức review (hours) - Bổ sung
7. **Documentation Effort** - Công sức documentation (hours) - Bổ sung
8. **Coordination Effort** - Công sức coordination (hours) - Bổ sung

### Calculated Fields:
9. **Total Effort** - Tổng effort (Research + Development + Testing + Deployment + Operations + Review + Documentation + Coordination)
10. **Research Effort %** - % effort nghiên cứu
11. **Development Effort %** - % effort phát triển
12. **Testing Effort %** - % effort testing
13. **Deployment Effort %** - % effort triển khai
14. **Operations Effort %** - % effort vận hành
15. **Review Effort %** - % effort review
16. **Documentation Effort %** - % effort documentation
17. **Coordination Effort %** - % effort coordination

### Advanced Fields (Nâng cao):
10. **Estimated Research Effort** - Ước lượng nghiên cứu
11. **Estimated Development Effort** - Ước lượng phát triển
12. **Estimated Deployment Effort** - Ước lượng triển khai
13. **Estimated Operations Effort** - Ước lượng vận hành
14. **Effort Variance** - Chênh lệch (Actual - Estimated)
15. **Effort Efficiency** - Hiệu quả effort

---

## EFFORT TRACKING CHO TẤT CẢ ISSUE TYPES

### 1. AGILE ISSUE TYPES

#### Epic:
- **Total Research Effort** (Number - calculated từ children)
- **Total Development Effort** (Number - calculated từ children)
- **Total Testing Effort** (Number - calculated từ children)
- **Total Deployment Effort** (Number - calculated từ children)
- **Total Operations Effort** (Number - calculated từ children)
- **Total Review Effort** (Number - calculated từ children)
- **Total Documentation Effort** (Number - calculated từ children)
- **Total Coordination Effort** (Number - calculated từ children)
- **Total Effort** (Number - calculated)
- **Effort Distribution** (Text - % by phase)

#### Story:
- **Research Effort** (Time Tracking) - Nghiên cứu requirements, design
- **Development Effort** (Time Tracking) - Coding
- **Testing Effort** (Time Tracking) - Unit testing, integration testing
- **Deployment Effort** (Time Tracking) - Deployment preparation
- **Operations Effort** (Time Tracking) - Post-deployment support
- **Review Effort** (Time Tracking) - Code review, design review
- **Documentation Effort** (Time Tracking) - Technical docs, user guides
- **Coordination Effort** (Time Tracking) - Meetings, standups, planning
- **Total Effort** (Number - calculated)
- **Story Points** (Number)

#### Task:
- **Research Effort** (Time Tracking) - Nghiên cứu approach
- **Development Effort** (Time Tracking) - Implementation
- **Testing Effort** (Time Tracking) - Testing tasks
- **Deployment Effort** (Time Tracking) - Deployment tasks
- **Operations Effort** (Time Tracking) - Operations tasks
- **Review Effort** (Time Tracking) - Review tasks
- **Documentation Effort** (Time Tracking) - Documentation tasks
- **Coordination Effort** (Time Tracking) - Coordination tasks
- **Total Effort** (Number - calculated)
- **Task Type**: Research, Development, Testing, Deployment, Operations

#### Bug:
- **Research Effort** (Time Tracking) - Nghiên cứu root cause
- **Development Effort** (Time Tracking) - Fix implementation
- **Testing Effort** (Time Tracking) - Regression testing, verification
- **Deployment Effort** (Time Tracking) - Fix deployment
- **Operations Effort** (Time Tracking) - Verification, monitoring
- **Review Effort** (Time Tracking) - Code review for fix
- **Total Effort** (Number - calculated)

---

### 2. ITIL ISSUE TYPES

#### Incident:
- **Research Effort** (Time Tracking) - Nghiên cứu nguyên nhân
- **Development Effort** (Time Tracking) - Fix development (nếu cần)
- **Deployment Effort** (Time Tracking) - Hotfix deployment
- **Operations Effort** (Time Tracking) - Investigation, resolution, monitoring
- **Total Effort** (Number - calculated)
- **Resolution Time** (Number - hours, auto-calculated)

#### Change Request:
- **Research Effort** (Time Tracking) - Nghiên cứu impact, risk
- **Development Effort** (Time Tracking) - Development work
- **Deployment Effort** (Time Tracking) - Implementation, deployment
- **Operations Effort** (Time Tracking) - Post-implementation review, monitoring
- **Total Effort** (Number - calculated)

#### Service Request:
- **Research Effort** (Time Tracking) - Nghiên cứu yêu cầu
- **Development Effort** (Time Tracking) - Configuration, setup
- **Deployment Effort** (Time Tracking) - Fulfillment, delivery
- **Operations Effort** (Time Tracking) - Support, follow-up
- **Total Effort** (Number - calculated)

#### Service Order:
- **Research Effort** (Time Tracking) - Nghiên cứu order requirements
- **Development Effort** (Time Tracking) - Customization (nếu cần)
- **Deployment Effort** (Time Tracking) - Production, delivery
- **Operations Effort** (Time Tracking) - Post-delivery support
- **Total Effort** (Number - calculated)

#### Problem:
- **Research Effort** (Time Tracking) - Root cause analysis
- **Development Effort** (Time Tracking) - Permanent fix development
- **Deployment Effort** (Time Tracking) - Fix deployment
- **Operations Effort** (Time Tracking) - Monitoring, verification
- **Total Effort** (Number - calculated)

#### Knowledge Article:
- **Research Effort** (Time Tracking) - Nghiên cứu, gather information
- **Development Effort** (Time Tracking) - Write, format content
- **Deployment Effort** (Time Tracking) - Publish, distribute
- **Operations Effort** (Time Tracking) - Maintain, update
- **Total Effort** (Number - calculated)

#### SLA Review:
- **Research Effort** (Time Tracking) - Nghiên cứu SLA performance
- **Development Effort** (Time Tracking) - Analysis, reporting
- **Deployment Effort** (Time Tracking) - Review meeting, presentation
- **Operations Effort** (Time Tracking) - Follow-up actions
- **Total Effort** (Number - calculated)

#### Service Catalog Item:
- **Research Effort** (Time Tracking) - Nghiên cứu service requirements
- **Development Effort** (Time Tracking) - Define, document service
- **Deployment Effort** (Time Tracking) - Publish to catalog
- **Operations Effort** (Time Tracking) - Maintain catalog item
- **Total Effort** (Number - calculated)

#### Availability Incident:
- **Research Effort** (Time Tracking) - Nghiên cứu availability issue
- **Development Effort** (Time Tracking) - Fix development (nếu cần)
- **Deployment Effort** (Time Tracking) - Fix deployment
- **Operations Effort** (Time Tracking) - Investigation, resolution, monitoring
- **Total Effort** (Number - calculated)

#### Capacity Request:
- **Research Effort** (Time Tracking) - Nghiên cứu capacity needs
- **Development Effort** (Time Tracking) - Capacity planning, design
- **Deployment Effort** (Time Tracking) - Capacity provisioning
- **Operations Effort** (Time Tracking) - Monitoring, optimization
- **Total Effort** (Number - calculated)

#### Disaster Recovery Plan:
- **Research Effort** (Time Tracking) - Nghiên cứu risks, requirements
- **Development Effort** (Time Tracking) - Plan development
- **Deployment Effort** (Time Tracking) - Plan implementation, testing
- **Operations Effort** (Time Tracking) - Plan maintenance, updates
- **Total Effort** (Number - calculated)

#### Disaster Recovery Test:
- **Research Effort** (Time Tracking) - Nghiên cứu test requirements
- **Development Effort** (Time Tracking) - Test plan development
- **Deployment Effort** (Time Tracking) - Test execution
- **Operations Effort** (Time Tracking) - Test review, improvements
- **Total Effort** (Number - calculated)

#### Security Incident:
- **Research Effort** (Time Tracking) - Nghiên cứu security issue
- **Development Effort** (Time Tracking) - Security fix development
- **Deployment Effort** (Time Tracking) - Security fix deployment
- **Operations Effort** (Time Tracking) - Investigation, containment, monitoring
- **Total Effort** (Number - calculated)

#### Security Assessment:
- **Research Effort** (Time Tracking) - Nghiên cứu security requirements
- **Development Effort** (Time Tracking) - Assessment planning, execution
- **Deployment Effort** (Time Tracking) - Assessment reporting
- **Operations Effort** (Time Tracking) - Remediation follow-up
- **Total Effort** (Number - calculated)

#### Supplier:
- **Research Effort** (Time Tracking) - Nghiên cứu supplier
- **Development Effort** (Time Tracking) - Onboarding, setup
- **Deployment Effort** (Time Tracking) - Contract, integration
- **Operations Effort** (Time Tracking) - Relationship management
- **Total Effort** (Number - calculated)

#### Supplier Performance Review:
- **Research Effort** (Time Tracking) - Nghiên cứu performance data
- **Development Effort** (Time Tracking) - Analysis, reporting
- **Deployment Effort** (Time Tracking) - Review meeting
- **Operations Effort** (Time Tracking) - Follow-up actions
- **Total Effort** (Number - calculated)

#### IT Asset:
- **Research Effort** (Time Tracking) - Nghiên cứu asset requirements
- **Development Effort** (Time Tracking) - Asset configuration
- **Deployment Effort** (Time Tracking) - Asset deployment
- **Operations Effort** (Time Tracking) - Asset maintenance, lifecycle
- **Total Effort** (Number - calculated)

#### Asset Request:
- **Research Effort** (Time Tracking) - Nghiên cứu asset needs
- **Development Effort** (Time Tracking) - Request processing
- **Deployment Effort** (Time Tracking) - Asset procurement, delivery
- **Operations Effort** (Time Tracking) - Asset setup, handover
- **Total Effort** (Number - calculated)

#### Configuration Item (CI):
- **Research Effort** (Time Tracking) - Nghiên cứu CI requirements
- **Development Effort** (Time Tracking) - CI definition, configuration
- **Deployment Effort** (Time Tracking) - CI registration, documentation
- **Operations Effort** (Time Tracking) - CI maintenance, updates
- **Total Effort** (Number - calculated)

#### Release:
- **Research Effort** (Time Tracking) - Nghiên cứu release requirements
- **Development Effort** (Time Tracking) - Release planning, coordination
- **Deployment Effort** (Time Tracking) - Release deployment
- **Operations Effort** (Time Tracking) - Post-release monitoring, support
- **Total Effort** (Number - calculated)

#### Deployment:
- **Research Effort** (Time Tracking) - Nghiên cứu deployment strategy
- **Development Effort** (Time Tracking) - Deployment scripts, automation
- **Deployment Effort** (Time Tracking) - Actual deployment execution
- **Operations Effort** (Time Tracking) - Post-deployment verification, monitoring
- **Total Effort** (Number - calculated)

---

### 3. QUẢN TRỊ ISSUE TYPES

#### Risk:
- **Research Effort** (Time Tracking) - Nghiên cứu risk
- **Development Effort** (Time Tracking) - Risk assessment, mitigation planning
- **Deployment Effort** (Time Tracking) - Mitigation implementation
- **Operations Effort** (Time Tracking) - Risk monitoring, review
- **Total Effort** (Number - calculated)

#### Portfolio Item:
- **Research Effort** (Time Tracking) - Nghiên cứu portfolio item
- **Development Effort** (Time Tracking) - Portfolio planning, coordination
- **Deployment Effort** (Time Tracking) - Portfolio execution
- **Operations Effort** (Time Tracking) - Portfolio monitoring, optimization
- **Total Effort** (Number - calculated)

#### Budget:
- **Research Effort** (Time Tracking) - Nghiên cứu budget requirements
- **Development Effort** (Time Tracking) - Budget planning, allocation
- **Deployment Effort** (Time Tracking) - Budget approval, activation
- **Operations Effort** (Time Tracking) - Budget monitoring, tracking
- **Total Effort** (Number - calculated)

#### Customer:
- **Research Effort** (Time Tracking) - Nghiên cứu customer needs
- **Development Effort** (Time Tracking) - Customer onboarding, setup
- **Deployment Effort** (Time Tracking) - Customer activation
- **Operations Effort** (Time Tracking) - Customer relationship management
- **Total Effort** (Number - calculated)

#### Customer Feedback:
- **Research Effort** (Time Tracking) - Nghiên cứu feedback
- **Development Effort** (Time Tracking) - Feedback analysis
- **Deployment Effort** (Time Tracking) - Feedback response, actions
- **Operations Effort** (Time Tracking) - Follow-up, satisfaction tracking
- **Total Effort** (Number - calculated)

#### Demand Forecast:
- **Research Effort** (Time Tracking) - Nghiên cứu demand trends
- **Development Effort** (Time Tracking) - Forecast modeling, analysis
- **Deployment Effort** (Time Tracking) - Forecast presentation, approval
- **Operations Effort** (Time Tracking) - Forecast monitoring, updates
- **Total Effort** (Number - calculated)

---

### 4. GOVERNANCE ISSUE TYPES

#### Policy:
- **Research Effort** (Time Tracking) - Nghiên cứu policy requirements
- **Development Effort** (Time Tracking) - Policy writing, review
- **Deployment Effort** (Time Tracking) - Policy approval, publication
- **Operations Effort** (Time Tracking) - Policy maintenance, updates
- **Total Effort** (Number - calculated)

#### Compliance Audit:
- **Research Effort** (Time Tracking) - Nghiên cứu compliance requirements
- **Development Effort** (Time Tracking) - Audit planning, preparation
- **Deployment Effort** (Time Tracking) - Audit execution
- **Operations Effort** (Time Tracking) - Audit reporting, remediation
- **Total Effort** (Number - calculated)

#### Requirement:
- **Research Effort** (Time Tracking) - Nghiên cứu requirements
- **Development Effort** (Time Tracking) - Requirements analysis, documentation
- **Deployment Effort** (Time Tracking) - Requirements approval, handover
- **Operations Effort** (Time Tracking) - Requirements tracking, updates
- **Total Effort** (Number - calculated)

#### Test Case:
- **Research Effort** (Time Tracking) - Nghiên cứu test requirements
- **Development Effort** (Time Tracking) - Test case writing
- **Deployment Effort** (Time Tracking) - Test execution
- **Operations Effort** (Time Tracking) - Test maintenance, updates
- **Total Effort** (Number - calculated)

---

**Lưu ý**: Product Research, Product Development, Product Deployment, Product Operations, Project Research, Project Development, Project Deployment, Project Operations đã được quyết định LOẠI BỎ và thay thế bằng Epic/Story/Task với custom fields (Work Type, Phase, Customer). Xem PHAN_TICH_ISSUE_TYPES.md để biết chi tiết.

**Effort tracking cho các công việc này được thực hiện thông qua Epic/Story/Task**:
- Epic/Story với Work Type=Product, Phase=Research → Track Research Effort
- Story với Work Type=Product, Phase=Development → Track Research + Development + Testing Effort
- Epic/Story/Task với Work Type=Project, Phase=Deployment → Track Research + Development + Deployment Effort
- Task/Service Request với Work Type=Project, Phase=Operations → Track Operations Effort

---

## AUTOMATION RULES

### Auto-calculate Total Effort:
- **Trigger**: When any effort field is updated
- **Action**: Calculate Total Effort = Research + Development + Testing + Deployment + Operations + Review + Documentation + Coordination
- **Update**: Total Effort field

### Auto-calculate Effort Percentages:
- **Trigger**: When Total Effort is updated
- **Action**: Calculate percentages for all effort fields:
  - Research Effort % = (Research Effort / Total Effort) × 100
  - Development Effort % = (Development Effort / Total Effort) × 100
  - Testing Effort % = (Testing Effort / Total Effort) × 100
  - Deployment Effort % = (Deployment Effort / Total Effort) × 100
  - Operations Effort % = (Operations Effort / Total Effort) × 100
  - Review Effort % = (Review Effort / Total Effort) × 100
  - Documentation Effort % = (Documentation Effort / Total Effort) × 100
  - Coordination Effort % = (Coordination Effort / Total Effort) × 100
- **Update**: All Effort % fields

### Update Epic Total Effort:
- **Trigger**: When child issue effort is updated
- **Action**: Sum all child issues' effort by phase:
  - Total Research Effort = Sum of all children's Research Effort
  - Total Development Effort = Sum of all children's Development Effort
  - Total Testing Effort = Sum of all children's Testing Effort
  - Total Deployment Effort = Sum of all children's Deployment Effort
  - Total Operations Effort = Sum of all children's Operations Effort
  - Total Review Effort = Sum of all children's Review Effort
  - Total Documentation Effort = Sum of all children's Documentation Effort
  - Total Coordination Effort = Sum of all children's Coordination Effort
  - Total Effort = Sum of all children's Total Effort
- **Update**: Epic's Total Effort fields

### Effort Validation:
- **Trigger**: When issue transitions to specific status (e.g., Done, Closed)
- **Action**: Validate required effort fields are filled
- **Alert**: If required fields are empty

### Effort Variance Alert:
- **Trigger**: When Actual Effort is updated
- **Action**: Calculate variance = (Actual - Estimated) / Estimated × 100
- **Alert**: If variance > 20%

---

## JQL QUERIES CHO EFFORT TRACKING

### All Issues with Effort:
```jql
project = PROJ AND "Total Effort" > 0
```

### Issues by Effort Phase:
```jql
project = PROJ AND "Research Effort" > 0
project = PROJ AND "Development Effort" > 0
project = PROJ AND "Testing Effort" > 0
project = PROJ AND "Deployment Effort" > 0
project = PROJ AND "Operations Effort" > 0
project = PROJ AND "Review Effort" > 0
project = PROJ AND "Documentation Effort" > 0
project = PROJ AND "Coordination Effort" > 0
```

### Effort by Issue Type:
```jql
project = PROJ AND type = Story AND "Total Effort" > 0
project = PROJ AND type = Incident AND "Total Effort" > 0
```

### High Effort Issues:
```jql
project = PROJ AND "Total Effort" > 40
```

### Effort by Customer (Project issues):
```jql
project = PROJ AND "Work Type" = Project AND Customer is not EMPTY AND "Total Effort" > 0
```

---

## DASHBOARDS & REPORTS

### Effort Summary Dashboard:
- Total Effort by Phase (all issue types)
- Effort by Issue Type
- Effort Trend over time
- Effort by Customer/Product

### Issue Type Effort Reports:
- Effort breakdown for each issue type
- Average effort per issue type
- Effort distribution by phase per issue type

---

## IMPLEMENTATION CHECKLIST

- [ ] Add effort fields to all 39 issue types (Nâng cao) / 8 issue types (Cơ bản)
- [ ] Add Testing, Review, Documentation, Coordination effort fields
- [ ] Setup automation rules for Total Effort calculation
- [ ] Setup automation rules for Effort % calculation
- [ ] Setup automation rules for Epic effort aggregation
- [ ] Create JQL queries for effort tracking
- [ ] Create dashboards for effort reporting
- [ ] Test effort tracking on all issue types
- [ ] Train users on effort logging

---

**Tài liệu này đảm bảo effort tracking hoàn thiện cho TẤT CẢ issue types (39 types Nâng cao / 8 types Cơ bản) với 8 effort fields đầy đủ.**
