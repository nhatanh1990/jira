# KỊCH BẢN TRIỂN KHAI - JIRA SYSTEM

Tài liệu này mô tả các kịch bản triển khai hệ thống Jira cho các tình huống khác nhau.

---

## MỤC LỤC

1. [Kịch bản 1: Startup/SMB - Triển khai Cơ Bản](#1-kịch-bản-1-startupsmb---triển-khai-cơ-bản)
2. [Kịch bản 2: Enterprise - Triển khai Nâng Cao](#2-kịch-bản-2-enterprise---triển-khai-nâng-cao)
3. [Kịch bản 3: Migration từ hệ thống cũ](#3-kịch-bản-3-migration-từ-hệ-thống-cũ)
4. [Kịch bản 4: Multi-team/Multi-project](#4-kịch-bản-4-multi-teammulti-project)
5. [Kịch bản 5: Phased Rollout](#5-kịch-bản-5-phased-rollout)

---

## 1. KỊCH BẢN 1: STARTUP/SMB - TRIỂN KHAI CƠ BẢN

### 1.1. Thông tin tổng quan

**Đối tượng**:
- Team size: 10-50 users
- Số project: 1-3 projects
- Yêu cầu: Agile + ITIL cơ bản
- Timeline: 3 tuần

**Mục tiêu**:
- Triển khai nhanh
- Dễ sử dụng
- Track effort cơ bản
- Tích hợp GitLab

---

### 1.2. Phase 1: Setup cơ bản (Tuần 1)

#### Day 1-2: Project Setup
- [ ] Tạo Jira project (Software Development template)
- [ ] Cấu hình 8 issue types:
 - Epic, Story, Task, Bug
 - Incident, Change Request, Service Request, Service Order
- [ ] Setup 7 roles:
 - Product Owner, Developer, QA/Tester, Support, SRE/DevOps, CAB, Jira Admin
- [ ] Tạo permission schemes

#### Day 3-4: Custom Fields
- [ ] Tạo effort tracking fields:
 - Research Effort, Development Effort, Testing Effort, Deployment Effort, Operations Effort
 - Review Effort, Documentation Effort, Coordination Effort
 - Total Effort (calculated)
- [ ] Tạo classification fields:
 - Work Type (Product, Project, Support, ITIL)
 - Phase (Research, Development, Testing, Deployment, Operations)
 - Customer (User Picker)
- [ ] Cấu hình field configuration

#### Day 5: Workflows
- [ ] Setup Agile workflow (Story/Task/Bug)
- [ ] Setup Epic workflow
- [ ] Setup ITIL workflows:
 - Incident workflow
 - Change Request workflow
 - Service Request workflow
 - Service Order workflow

**Deliverable**: Project đã được setup cơ bản, có thể tạo issues.

---

### 1.3. Phase 2: Automation & Integration (Tuần 2)

#### Day 6-7: Automation Rules
- [ ] Auto-calculate Total Effort
- [ ] Auto-calculate Effort %
- [ ] Auto-update Epic effort from children
- [ ] Auto-assign based on issue type
- [ ] Email notifications

#### Day 8-9: GitLab Integration
- [ ] Cấu hình GitLab integration
- [ ] Setup branch creation từ Jira
- [ ] Link MRs với Jira issues
- [ ] Auto-transition khi MR merged

#### Day 10: Testing
- [ ] Test tất cả workflows
- [ ] Test effort tracking
- [ ] Test automation rules
- [ ] Test GitLab integration

**Deliverable**: Automation và integration đã hoạt động.

---

### 1.4. Phase 3: Dashboards & Training (Tuần 3)

#### Day 11-12: Dashboards
- [ ] Executive Dashboard
- [ ] Product Owner Dashboard
- [ ] Development Dashboard
- [ ] Support Dashboard
- [ ] Effort Summary Dashboard

#### Day 13-14: Training
- [ ] Training cho Product Owner
- [ ] Training cho Developer team
- [ ] Training cho QA/Tester
- [ ] Training cho Support
- [ ] Training cho SRE/DevOps

#### Day 15: Go-live
- [ ] Final testing
- [ ] Migration dữ liệu (nếu có)
- [ ] Go-live
- [ ] Support trong tuần đầu

**Deliverable**: Hệ thống đã sẵn sàng sử dụng.

---

## 2. KỊCH BẢN 2: ENTERPRISE - TRIỂN KHAI NÂNG CAO

### 2.1. Thông tin tổng quan

**Đối tượng**:
- Team size: 100+ users
- Số project: 10+ projects
- Yêu cầu: ITIL đầy đủ + Quản trị + Governance
- Timeline: 12-13 tuần

**Mục tiêu**:
- Triển khai đầy đủ tính năng
- ITIL compliance
- Governance & Compliance
- Advanced reporting

---

### 2.2. Phase 1: Foundation (Tuần 1-2)

#### Week 1: Project Setup
- [ ] Tạo multiple projects
- [ ] Cấu hình 39 issue types
- [ ] Setup 12+ roles
- [ ] Tạo permission schemes cho từng project
- [ ] Setup project hierarchy

#### Week 2: Custom Fields & Workflows
- [ ] Tạo tất cả custom fields (effort + ITIL + management)
- [ ] Setup 47 workflows
- [ ] Cấu hình field configuration
- [ ] Setup screen schemes

**Deliverable**: Foundation đã được setup.

---

### 2.3. Phase 2: ITIL Processes (Tuần 3-6)

#### Week 3: Core ITIL
- [ ] Incident Management (đầy đủ)
- [ ] Change Management (với CAB)
- [ ] Service Request Management
- [ ] Service Order Management

#### Week 4: Problem & Knowledge
- [ ] Problem Management
- [ ] Knowledge Management
- [ ] SLA Management

#### Week 5: Service Operations
- [ ] Availability Management
- [ ] Capacity Management
- [ ] Security Management

#### Week 6: Service Transition
- [ ] Release Management
- [ ] Asset Management
- [ ] CMDB

**Deliverable**: ITIL processes đã được cấu hình.

---

### 2.4. Phase 3: Management & Governance (Tuần 7-9)

#### Week 7: Management Methodologies
- [ ] Risk Management
- [ ] Portfolio Management
- [ ] Kanban boards
- [ ] DevOps workflows

#### Week 8: Business Management
- [ ] Financial Management
- [ ] Business Relationship Management
- [ ] Demand Management
- [ ] BI/Analytics integration

#### Week 9: Governance & Compliance
- [ ] Policy Management
- [ ] Compliance Audit
- [ ] Requirement Management
- [ ] Test Case Management

**Deliverable**: Management & Governance đã được setup.

---

### 2.5. Phase 4: Automation & Integration (Tuần 10-11)

#### Week 10: Advanced Automation
- [ ] Complex automation rules
- [ ] SLA automation
- [ ] Escalation rules
- [ ] Notification rules

#### Week 11: Integrations
- [ ] GitLab (full integration)
- [ ] Confluence
- [ ] Slack
- [ ] Monitoring tools (Prometheus, Grafana)
- [ ] BI tools (Tableau, Power BI)

**Deliverable**: Automation và integrations đã hoạt động.

---

### 2.6. Phase 5: Dashboards & Reporting (Tuần 12)

#### Week 12: Dashboards
- [ ] 15+ dashboards
- [ ] Advanced reports
- [ ] Custom JQL queries
- [ ] Analytics

**Deliverable**: Dashboards và reporting đã sẵn sàng.

---

### 2.7. Phase 6: Training & Go-live (Tuần 13)

#### Week 13: Training & Go-live
- [ ] Training cho tất cả roles
- [ ] Training cho admins
- [ ] Documentation
- [ ] Final testing
- [ ] Phased go-live
- [ ] Support

**Deliverable**: Hệ thống đã sẵn sàng production.

---

## 3. KỊCH BẢN 3: MIGRATION TỪ HỆ THỐNG CŨ

### 3.1. Thông tin tổng quan

**Tình huống**:
- Đang sử dụng hệ thống khác (Jira cũ, Trello, Asana, etc.)
- Cần migrate dữ liệu
- Không muốn gián đoạn công việc

**Timeline**: 4-6 tuần (tùy vào lượng dữ liệu)

---

### 3.2. Phase 1: Assessment (Tuần 1)

#### Tasks:
- [ ] Đánh giá hệ thống hiện tại
- [ ] Liệt kê dữ liệu cần migrate:
 - Issues
 - Users
 - Projects
 - Attachments
 - Comments
 - History
- [ ] Xác định mapping:
 - Issue types mapping
 - Status mapping
 - Custom fields mapping
- [ ] Tạo migration plan

**Deliverable**: Migration plan đã được approve.

---

### 3.3. Phase 2: Setup Jira mới (Tuần 2)

#### Tasks:
- [ ] Setup Jira project mới (theo kịch bản 1 hoặc 2)
- [ ] Cấu hình issue types, workflows, fields
- [ ] Setup users và permissions
- [ ] Test với sample data

**Deliverable**: Jira mới đã được setup.

---

### 3.4. Phase 3: Data Migration (Tuần 3-4)

#### Week 3: Preparation
- [ ] Export dữ liệu từ hệ thống cũ
- [ ] Transform data theo format Jira
- [ ] Validate data
- [ ] Backup dữ liệu

#### Week 4: Migration
- [ ] Import users
- [ ] Import projects
- [ ] Import issues (phased):
 - Phase 1: Active issues
 - Phase 2: Recent closed issues
 - Phase 3: Historical issues
- [ ] Import attachments
- [ ] Import comments
- [ ] Validate migration

**Deliverable**: Dữ liệu đã được migrate.

---

### 3.5. Phase 4: Parallel Run (Tuần 5)

#### Tasks:
- [ ] Chạy song song 2 hệ thống
- [ ] Users sử dụng cả 2 hệ thống
- [ ] So sánh kết quả
- [ ] Fix issues
- [ ] Training users

**Deliverable**: Users đã quen với Jira mới.

---

### 3.6. Phase 5: Cutover (Tuần 6)

#### Tasks:
- [ ] Final data sync
- [ ] Cutover to Jira mới
- [ ] Archive hệ thống cũ
- [ ] Support users
- [ ] Monitor issues

**Deliverable**: Migration hoàn tất.

---

## 4. KỊCH BẢN 4: MULTI-TEAM/MULTI-PROJECT

### 4.1. Thông tin tổng quan

**Tình huống**:
- Nhiều teams (Product, Engineering, Support, Operations)
- Nhiều projects (Product A, Product B, Internal Tools, etc.)
- Cần quản lý cross-project

**Timeline**: 6-8 tuần

---

### 4.2. Phase 1: Project Structure (Tuần 1-2)

#### Week 1: Planning
- [ ] Xác định project structure:
 - Product projects
 - Internal projects
 - Support projects
- [ ] Xác định project hierarchy
- [ ] Xác định shared components

#### Week 2: Setup Projects
- [ ] Tạo projects
- [ ] Cấu hình project-specific settings
- [ ] Setup shared components
- [ ] Setup cross-project links

**Deliverable**: Project structure đã được setup.

---

### 4.3. Phase 2: Team Setup (Tuần 3-4)

#### Week 3: Roles & Permissions
- [ ] Setup roles cho từng team
- [ ] Cấu hình permissions:
 - Team-specific permissions
 - Cross-team permissions
- [ ] Setup project roles

#### Week 4: Workflows
- [ ] Setup workflows cho từng project type
- [ ] Cấu hình cross-project workflows
- [ ] Setup automation rules

**Deliverable**: Teams đã được setup.

---

### 4.4. Phase 3: Integration & Automation (Tuần 5-6)

#### Week 5: Integrations
- [ ] GitLab integration (multiple projects)
- [ ] Confluence (shared documentation)
- [ ] Slack (team notifications)

#### Week 6: Automation
- [ ] Cross-project automation
- [ ] Team-specific automation
- [ ] Reporting automation

**Deliverable**: Integrations và automation đã hoạt động.

---

### 4.5. Phase 4: Dashboards & Training (Tuần 7-8)

#### Week 7: Dashboards
- [ ] Team-specific dashboards
- [ ] Cross-project dashboards
- [ ] Executive dashboards

#### Week 8: Training & Go-live
- [ ] Training cho từng team
- [ ] Cross-team training
- [ ] Go-live
- [ ] Support

**Deliverable**: Multi-team system đã sẵn sàng.

---

## 5. KỊCH BẢN 5: PHASED ROLLOUT

### 5.1. Thông tin tổng quan

**Tình huống**:
- Large organization
- Nhiều departments
- Cần rollout từng bước để giảm risk

**Timeline**: 16-20 tuần

---

### 5.2. Phase 1: Pilot (Tuần 1-4)

#### Week 1-2: Setup Pilot
- [ ] Chọn pilot team (1-2 teams)
- [ ] Setup Jira cho pilot
- [ ] Cấu hình cơ bản

#### Week 3-4: Pilot Run
- [ ] Pilot team sử dụng Jira
- [ ] Collect feedback
- [ ] Fix issues
- [ ] Refine configuration

**Deliverable**: Pilot thành công.

---

### 5.3. Phase 2: Department 1 (Tuần 5-8)

#### Week 5-6: Setup
- [ ] Setup cho Department 1 (Engineering)
- [ ] Training
- [ ] Configuration

#### Week 7-8: Rollout
- [ ] Go-live Department 1
- [ ] Support
- [ ] Monitor

**Deliverable**: Department 1 đã sử dụng Jira.

---

### 5.4. Phase 3: Department 2 (Tuần 9-12)

#### Week 9-10: Setup
- [ ] Setup cho Department 2 (Support)
- [ ] Training
- [ ] Configuration

#### Week 11-12: Rollout
- [ ] Go-live Department 2
- [ ] Support
- [ ] Monitor

**Deliverable**: Department 2 đã sử dụng Jira.

---

### 5.5. Phase 4: Department 3 (Tuần 13-16)

#### Week 13-14: Setup
- [ ] Setup cho Department 3 (Operations)
- [ ] Training
- [ ] Configuration

#### Week 15-16: Rollout
- [ ] Go-live Department 3
- [ ] Support
- [ ] Monitor

**Deliverable**: Department 3 đã sử dụng Jira.

---

### 5.6. Phase 5: Remaining Departments (Tuần 17-20)

#### Week 17-18: Setup
- [ ] Setup cho các departments còn lại
- [ ] Training
- [ ] Configuration

#### Week 19-20: Final Rollout
- [ ] Go-live tất cả departments
- [ ] Support
- [ ] Monitor
- [ ] Documentation

**Deliverable**: Toàn bộ organization đã sử dụng Jira.

---

## TỔNG KẾT

### Kịch bản phù hợp:

| Kịch bản | Team Size | Timeline | Phù hợp cho |
|----------|-----------|----------|-------------|
| **1. Cơ Bản** | 10-50 | 3 tuần | Startup, SMB |
| **2. Nâng Cao** | 100+ | 12-13 tuần | Enterprise |
| **3. Migration** | Any | 4-6 tuần | Có hệ thống cũ |
| **4. Multi-team** | 50-200 | 6-8 tuần | Nhiều teams |
| **5. Phased** | 200+ | 16-20 tuần | Large org |

### Checklist chung:

- [ ] Đánh giá requirements
- [ ] Chọn kịch bản phù hợp
- [ ] Tạo project plan
- [ ] Setup infrastructure
- [ ] Cấu hình Jira
- [ ] Training users
- [ ] Go-live
- [ ] Support & monitor

---

**Lưu ý**: Tất cả kịch bản đều cần effort tracking để đảm bảo thống kê đầy đủ.
