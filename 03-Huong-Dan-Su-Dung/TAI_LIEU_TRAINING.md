# TÀI LIỆU TRAINING - JIRA SYSTEM

Tài liệu training chi tiết cho tất cả roles trong hệ thống Jira.

---

## MỤC LỤC

1. [Training Overview](#1-training-overview)
2. [Training cho Developer](#2-training-cho-developer)
3. [Training cho QA/Tester](#3-training-cho-qatester)
4. [Training cho Product Owner](#4-training-cho-product-owner)
5. [Training cho Support](#5-training-cho-support)
6. [Training cho SRE/DevOps](#6-training-cho-sredevops)
7. [Training cho CAB](#7-training-cho-cab)
8. [Training cho Jira Admin](#8-training-cho-jira-admin)
9. [Training nâng cao](#9-training-nâng-cao)
10. [Assessment & Certification](#10-assessment--certification)

---

## 1. TRAINING OVERVIEW

### 1.1. Mục tiêu training

- Hiểu cách sử dụng Jira hiệu quả
- Nắm vững workflows và processes
- Biết cách track effort đúng cách
- Sử dụng dashboards và reports
- Follow best practices

### 1.2. Cấu trúc training

**Level 1: Basic (2-3 giờ)**
- Giới thiệu Jira
- Các thao tác cơ bản
- Workflows cơ bản

**Level 2: Intermediate (4-6 giờ)**
- Advanced features
- Effort tracking
- Dashboards và reports
- Best practices

**Level 3: Advanced (8-10 giờ)**
- JQL queries
- Automation
- Advanced workflows
- Integration

### 1.3. Training methods

- **Self-paced**: Đọc tài liệu, xem video
- **Instructor-led**: Training với trainer
- **Hands-on**: Thực hành trên Jira
- **Workshop**: Thảo luận và Q&A

---

## 2. TRAINING CHO DEVELOPER

### 2.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira là gì?
- Tại sao sử dụng Jira?
- Các khái niệm cơ bản (Project, Issue, Workflow, Status)
- Giao diện Jira

**Thực hành**:
- Đăng nhập và làm quen với giao diện
- Xem dashboard
- Tìm issue

**Assessment**:
- Quiz: 10 câu hỏi về khái niệm cơ bản

---

### 2.2. Module 2: Issue Types cho Developer (45 phút)

**Nội dung**:
- Story: Mục đích, cách sử dụng
- Task: Mục đích, cách sử dụng
- Bug: Mục đích, cách sử dụng
- Epic: Mục đích, cách sử dụng

**Thực hành**:
- Tạo Story mới
- Tạo Task mới
- Tạo Bug mới
- Link Story với Epic

**Assessment**:
- Tạo 1 Story với đầy đủ thông tin
- Tạo 1 Bug với steps to reproduce

---

### 2.3. Module 3: Workflow cho Developer (60 phút)

**Nội dung**:
- Agile workflow: To Do → In Progress → Code Review → Testing → Ready for Release → Done
- Khi nào chuyển status?
- Các transition rules
- Blocked status

**Thực hành**:
- Chuyển Story từ To Do → In Progress
- Chuyển Story từ In Progress → Code Review
- Chuyển Story từ Code Review → Testing
- Xử lý Blocked status

**Assessment**:
- Thực hành workflow với 1 Story từ đầu đến cuối

---

### 2.4. Module 4: Effort Tracking (45 phút)

**Nội dung**:
- Tại sao cần log effort?
- Các effort fields:
 - Research Effort
 - Development Effort
 - Testing Effort
 - Review Effort
 - Documentation Effort
 - Coordination Effort
- Cách log effort
- Best practices

**Thực hành**:
- Log effort cho Story
- Log effort cho nhiều ngày
- Xem Total Effort

**Assessment**:
- Log effort cho 1 Story với đầy đủ các phase

---

### 2.5. Module 5: GitLab Integration (30 phút)

**Nội dung**:
- Tạo branch từ Jira
- Link MR với Jira issue
- Auto-transition khi MR merged
- View GitLab info trong Jira

**Thực hành**:
- Tạo branch từ Story
- Tạo MR và link với Story
- Merge MR và xem auto-transition

**Assessment**:
- Tạo branch và MR từ 1 Story

---

### 2.6. Module 6: Best Practices (30 phút)

**Nội dung**:
- Viết Summary và Description rõ ràng
- Update status thường xuyên
- Comment khi cần
- Log effort đúng cách
- Follow workflow

**Thực hành**:
- Review và cải thiện issues cũ
- Practice best practices

**Assessment**:
- Review checklist và tự đánh giá

---

### 2.7. Developer Training Summary

**Thời gian**: 4-5 giờ
**Deliverables**:
- Hiểu cách sử dụng Jira cho development
- Biết cách track effort
- Follow workflows đúng cách
- Sử dụng GitLab integration

---

## 3. TRAINING CHO QA/TESTER

### 3.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira cho QA/Tester
- Issue types liên quan: Story, Bug, Test Case
- Workflow cho testing

**Thực hành**:
- Xem issues cần test
- Filter issues by status = "Testing"

---

### 3.2. Module 2: Testing Workflow (60 phút)

**Nội dung**:
- Workflow: Code Review → Testing → Ready for Release
- Khi nào nhận Story để test?
- Cách test Story
- Cách ghi lại kết quả test

**Thực hành**:
- Nhận Story ở status "Code Review"
- Test Story
- Ghi lại kết quả test
- Chuyển status

---

### 3.3. Module 3: Tạo và quản lý Bug (60 phút)

**Nội dung**:
- Khi nào tạo Bug?
- Cách tạo Bug:
 - Summary rõ ràng
 - Description chi tiết
 - Steps to Reproduce
 - Expected vs Actual
 - Priority
- Link Bug với Story
- Track Bug lifecycle

**Thực hành**:
- Tạo Bug từ Story
- Link Bug với Story
- Update Bug status
- Verify Bug fix

---

### 3.4. Module 4: Testing Effort Tracking (30 phút)

**Nội dung**:
- Log Testing Effort
- Log Review Effort (test case review)
- Log Documentation Effort (test documentation)

**Thực hành**:
- Log testing effort cho Story
- Log effort cho Bug verification

---

### 3.5. Module 5: Test Case Management (45 phút) - Nâng cao

**Nội dung**:
- Tạo Test Case issue
- Link Test Case với Story
- Track test execution
- Test coverage

**Thực hành**:
- Tạo Test Cases cho Story
- Link Test Cases với Story
- Track test execution

---

### 3.6. QA/Tester Training Summary

**Thời gian**: 4-5 giờ
**Deliverables**:
- Hiểu testing workflow
- Biết cách tạo và quản lý Bug
- Track testing effort
- Sử dụng Test Case management

---

## 4. TRAINING CHO PRODUCT OWNER

### 4.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira cho Product Owner
- Quản lý backlog
- Prioritization
- Story Points

---

### 4.2. Module 2: Tạo Epic và Story (60 phút)

**Nội dung**:
- Tạo Epic:
 - Summary, Description
 - Work Type, Phase
 - Business Value
 - Target Release
- Tạo Story:
 - Summary (User Story format)
 - Description
 - Acceptance Criteria
 - Story Points
 - Work Type, Phase
- Link Story với Epic

**Thực hành**:
- Tạo Epic mới
- Tạo 3 Stories từ Epic
- Link Stories với Epic

---

### 4.3. Module 3: Backlog Management (45 phút)

**Nội dung**:
- Xem Backlog
- Sắp xếp priority
- Gán Story cho Developer
- Estimate Story Points

**Thực hành**:
- Sắp xếp Backlog
- Gán Stories cho Developers
- Estimate Story Points

---

### 4.4. Module 4: Review và Approve (30 phút)

**Nội dung**:
- Review Story ở status "Ready for Release"
- Approve hoặc request changes
- Transition: Ready for Release → Done

**Thực hành**:
- Review Stories
- Approve Stories
- Request changes nếu cần

---

### 4.5. Module 5: Dashboards và Reports (45 phút)

**Nội dung**:
- Product Owner Dashboard
- Velocity tracking
- Effort tracking
- Progress reports

**Thực hành**:
- Xem Product Owner Dashboard
- Xem velocity chart
- Xem effort reports

---

### 4.6. Module 6: Change Request Approval (30 phút)

**Nội dung**:
- Review Change Request
- Approve/Reject Change Request
- CAB approval process

**Thực hành**:
- Review Change Request
- Approve Change Request

---

### 4.7. Product Owner Training Summary

**Thời gian**: 4-5 giờ
**Deliverables**:
- Biết cách tạo Epic và Story
- Quản lý Backlog hiệu quả
- Review và approve Stories
- Sử dụng dashboards và reports

---

## 5. TRAINING CHO SUPPORT

### 5.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira cho Support
- Service Request vs Incident
- SLA và Priority

---

### 5.2. Module 2: Service Request Management (60 phút)

**Nội dung**:
- Tạo Service Request
- Workflow: New → In Progress → Fulfilled → Closed
- Xử lý Service Request
- Log Operations Effort

**Thực hành**:
- Tạo Service Request
- Xử lý Service Request
- Log effort
- Close Service Request

---

### 5.3. Module 3: Incident Management (90 phút)

**Nội dung**:
- Tạo Incident
- Severity levels: SEV1, SEV2, SEV3, SEV4
- Workflow: New → Acknowledged → Investigating → Resolved → Closed
- Escalation process
- SLA tracking

**Thực hành**:
- Tạo Incident SEV2
- Xử lý Incident
- Escalate Incident (nếu cần)
- Resolve và Close Incident

---

### 5.4. Module 4: Communication (30 phút)

**Nội dung**:
- Comment trên issue
- Update status thường xuyên
- Notify stakeholders
- Customer communication

**Thực hành**:
- Comment trên Service Request
- Comment trên Incident
- Update status

---

### 5.5. Support Training Summary

**Thời gian**: 4-5 giờ
**Deliverables**:
- Biết cách xử lý Service Request
- Biết cách xử lý Incident
- Follow SLA
- Communication tốt

---

## 6. TRAINING CHO SRE/DEVOPS

### 6.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira cho SRE/DevOps
- Incident Management
- Change Management
- Deployment

---

### 6.2. Module 2: Incident Management SEV1/SEV2 (90 phút)

**Nội dung**:
- Xử lý Incident SEV1 (Critical)
- Xử lý Incident SEV2 (High)
- Workflow: New → Investigating → Mitigated → Resolved → Closed
- Root cause analysis
- Post-incident review

**Thực hành**:
- Xử lý Incident SEV1
- Mitigate và Resolve
- Document root cause

---

### 6.3. Module 3: Change Management (60 phút)

**Nội dung**:
- Review Change Request
- Approve Change Request (deployment)
- Implement Change
- Workflow: Approved → Implementation → Completed → Closed
- Rollback plan

**Thực hành**:
- Review Change Request
- Approve Change Request
- Implement Change
- Complete Change

---

### 6.4. Module 4: Deployment (45 phút)

**Nội dung**:
- Tạo Deployment issue
- Link với Change Request
- Track deployment effort
- Post-deployment verification

**Thực hành**:
- Tạo Deployment issue
- Link với Change Request
- Log deployment effort

---

### 6.5. Module 5: Monitoring và Alerts (30 phút)

**Nội dung**:
- Link monitoring tools với Jira
- Auto-create Incident từ alerts
- Track incident trends

---

### 6.6. SRE/DevOps Training Summary

**Thời gian**: 5-6 giờ
**Deliverables**:
- Biết cách xử lý Incident SEV1/SEV2
- Biết cách quản lý Change
- Track deployment
- Integrate với monitoring tools

---

## 7. TRAINING CHO CAB

### 7.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- CAB là gì?
- Vai trò của CAB
- Change Advisory Board process

---

### 7.2. Module 2: Review Change Request (60 phút)

**Nội dung**:
- Review Change Request:
 - Change Type (Standard, Normal, Emergency)
 - Risk Level
 - Implementation Plan
 - Rollback Plan
- Approve/Reject Change Request
- Comment required fields

**Thực hành**:
- Review Change Request
- Approve/Reject
- Comment

---

### 7.3. Module 3: Emergency Change (30 phút)

**Nội dung**:
- Emergency Change process
- Fast-track approval
- Post-implementation review

**Thực hành**:
- Review Emergency Change
- Fast-track approval

---

### 7.4. CAB Training Summary

**Thời gian**: 2-3 giờ
**Deliverables**:
- Biết cách review Change Request
- Approve/Reject đúng cách
- Handle Emergency Change

---

## 8. TRAINING CHO JIRA ADMIN

### 8.1. Module 1: Giới thiệu (30 phút)

**Nội dung**:
- Jira Admin responsibilities
- System administration
- User management

---

### 8.2. Module 2: Project Setup (90 phút)

**Nội dung**:
- Tạo project
- Cấu hình issue types
- Setup workflows
- Cấu hình permissions

**Thực hành**:
- Tạo project mới
- Setup issue types
- Setup workflows
- Cấu hình permissions

---

### 8.3. Module 3: Custom Fields (60 phút)

**Nội dung**:
- Tạo custom fields
 - Text, Number, Date, User Picker, etc.
 - Time Tracking fields
 - Calculated fields
- Field configuration
- Screen configuration

**Thực hành**:
- Tạo custom fields
- Cấu hình fields
- Setup screens

---

### 8.4. Module 4: Workflows (90 phút)

**Nội dung**:
- Tạo workflow
- Status và transitions
- Transition conditions
- Validators
- Post-functions

**Thực hành**:
- Tạo workflow mới
- Setup transitions
- Test workflow

---

### 8.5. Module 5: Automation (60 phút)

**Nội dung**:
- Automation rules
- Triggers
- Conditions
- Actions

**Thực hành**:
- Tạo automation rules
- Test automation

---

### 8.6. Module 6: Permissions (60 phút)

**Nội dung**:
- Permission schemes
- Project roles
- User management
- Group management

**Thực hành**:
- Tạo permission scheme
- Assign permissions
- Test permissions

---

### 8.7. Module 7: Integrations (45 phút)

**Nội dung**:
- GitLab integration
- Confluence integration
- Email configuration
- Other integrations

**Thực hành**:
- Setup GitLab integration
- Test integration

---

### 8.8. Jira Admin Training Summary

**Thời gian**: 8-10 giờ
**Deliverables**:
- Biết cách setup project
- Cấu hình workflows
- Setup automation
- Manage permissions
- Setup integrations

---

## 9. TRAINING NÂNG CAO

### 9.1. JQL Queries (2 giờ)

**Nội dung**:
- JQL syntax
- Basic queries
- Advanced queries
- Functions
- Operators

**Thực hành**:
- Tạo JQL queries
- Save as filters
- Use in dashboards

---

### 9.2. Dashboards (2 giờ)

**Nội dung**:
- Tạo dashboard
- Add gadgets
- Configure gadgets
- Share dashboard

**Thực hành**:
- Tạo dashboard mới
- Add gadgets
- Configure và share

---

### 9.3. Reports (2 giờ)

**Nội dung**:
- Built-in reports
- Custom reports
- Export reports
- Schedule reports

**Thực hành**:
- Tạo reports
- Export reports
- Schedule reports

---

## 10. ASSESSMENT & CERTIFICATION

### 10.1. Assessment Methods

**Quiz**:
- Multiple choice questions
- True/False questions
- Scenario-based questions

**Practical Assessment**:
- Create issues
- Follow workflows
- Log effort
- Use features

**Project**:
- Complete a project using Jira
- Demonstrate understanding

### 10.2. Certification Levels

**Level 1: Basic User**
- Pass quiz (80%+)
- Complete practical assessment
- Certificate: "Jira Basic User"

**Level 2: Intermediate User**
- Pass advanced quiz (80%+)
- Complete advanced practical assessment
- Certificate: "Jira Intermediate User"

**Level 3: Advanced User**
- Pass expert quiz (85%+)
- Complete expert project
- Certificate: "Jira Advanced User"

**Level 4: Administrator**
- Complete Admin training
- Pass Admin assessment
- Certificate: "Jira Administrator"

---

## TRAINING SCHEDULE

### Recommended Training Schedule

**Week 1**:
- Day 1: Developer training (4-5 hours)
- Day 2: QA/Tester training (4-5 hours)
- Day 3: Product Owner training (4-5 hours)

**Week 2**:
- Day 1: Support training (4-5 hours)
- Day 2: SRE/DevOps training (5-6 hours)
- Day 3: CAB training (2-3 hours)

**Week 3**:
- Day 1-2: Jira Admin training (8-10 hours)
- Day 3: Advanced training (JQL, Dashboards, Reports)

---

## TRAINING CHECKLIST

### For All Users:
- [ ] Completed basic training
- [ ] Passed assessment
- [ ] Can create issues
- [ ] Can follow workflows
- [ ] Can log effort
- [ ] Can use dashboards

### For Role-Specific:
- [ ] Completed role-specific training
- [ ] Passed role-specific assessment
- [ ] Can perform role-specific tasks

### For Admins:
- [ ] Completed Admin training
- [ ] Passed Admin assessment
- [ ] Can setup projects
- [ ] Can configure workflows
- [ ] Can manage permissions

---

**Chúc bạn training thành công! **
