# PHÂN TÍCH LICENSE, PLUGIN VÀ KHẢ NĂNG TRIỂN KHAI

## TỔNG QUAN

Tài liệu này phân tích chi tiết từng tính năng trong hệ thống Jira đã thiết kế, xác định:
- **Built-in**: Tính năng có sẵn trong Jira (không cần plugin)
- **Plugin**: Cần cài đặt plugin/add-on
- **License**: Cần license nâng cao (Jira Software, Service Management)
- **Custom**: Cần custom development/script

---

## PHÂN TÍCH THEO TỪNG TÍNH NĂNG

### 1. ISSUE TYPES

#### Phiên Bản Cơ Bản (8 types):
1. **Epic** - Built-in (Jira Software)
2. **Story** - Built-in (Jira Software)
3. **Task** - Built-in (Jira Core/Software)
4. **Bug** - Built-in (Jira Software)
5. **Incident** - Built-in (Jira Service Management)
6. **Change Request** - Built-in (Jira Service Management)
7. **Service Request** - Built-in (Jira Service Management)
8. **Service Order** - Built-in (Jira Service Management)

**Kết luận**: Tất cả 8 issue types đều là built-in, nhưng cần:
- **Jira Software** license cho Epic, Story, Task, Bug
- **Jira Service Management** license cho Incident, Change Request, Service Request, Service Order

#### Phiên Bản Nâng Cao (39 types):
- **Agile (4 types)**: Built-in (Jira Software)
- **ITIL Cơ Bản (4 types)**: Built-in (Jira Service Management)
- **ITIL Nâng Cao (12 types)**: 
 - Problem, Knowledge Article, SLA Review, Service Catalog Item, Availability Incident, Capacity Request, Disaster Recovery Plan, Disaster Recovery Test, Security Incident, Security Assessment, Supplier, Supplier Performance Review
 - **Một số cần plugin hoặc custom issue types**
- **Asset & Configuration (3 types)**: 
 - IT Asset, Asset Request, Configuration Item (CI)
 - **Cần plugin**: Insight (CMDB) hoặc Assets for Jira
- **Release & Deployment (2 types)**: 
 - Release, Deployment
 - Built-in (Jira Software)
- **Quản Trị (6 types)**: 
 - Risk, Portfolio Item, Budget, Customer, Customer Feedback, Demand Forecast
 - **Một số cần plugin hoặc custom issue types**
- **Governance (4 types)**: 
 - Policy, Compliance Audit, Requirement, Test Case
 - **Một số cần plugin hoặc custom issue types**

**Kết luận**: 
- 8 types đầu (Agile + ITIL Cơ Bản): Built-in
- Các types còn lại: Cần tạo custom issue types (built-in feature) hoặc dùng plugin

---

### 2. CUSTOM FIELDS

#### Effort Fields (8 fields):
1. **Research Effort** - Built-in (Time Tracking field)
2. **Development Effort** - Built-in (Time Tracking field)
3. **Testing Effort** - Built-in (Time Tracking field)
4. **Deployment Effort** - Built-in (Time Tracking field)
5. **Operations Effort** - Built-in (Time Tracking field)
6. **Review Effort** - Built-in (Time Tracking field)
7. **Documentation Effort** - Built-in (Time Tracking field)
8. **Coordination Effort** - Built-in (Time Tracking field)

**Kết luận**: Tất cả effort fields đều có thể tạo bằng built-in Time Tracking field của Jira.

#### Calculated Fields:
- **Total Effort** - **Custom**: Cần ScriptRunner hoặc Automation rule để tính tổng
- **Effort %** (8 fields) - **Custom**: Cần ScriptRunner hoặc Automation rule để tính %
- **Effort Variance** - **Custom**: Cần ScriptRunner hoặc Automation rule
- **Effort Efficiency** - **Custom**: Cần ScriptRunner hoặc Automation rule

**Kết luận**: 
- Fields cơ bản: Built-in
- Calculated fields: Cần ScriptRunner plugin hoặc Jira Automation (built-in từ Jira 8.0+)

#### Classification Fields:
- **Work Type** - Built-in (Select List)
- **Phase** - Built-in (Select List)
- **Customer** - Built-in (User Picker)
- **Product** - Built-in (Text hoặc Select List)
- **Cost Center** - Built-in (Select List)
- **Budget Code** - Built-in (Text)

**Kết luận**: Tất cả classification fields đều là built-in.

---

### 3. WORKFLOWS

#### Phiên Bản Cơ Bản (9 workflows):
- **Built-in**: Tất cả workflows có thể tạo bằng built-in Workflow Editor
- **Không cần plugin**: Jira có sẵn workflow engine
- **Giới hạn**: 
 - Workflow conditions, validators, post-functions cơ bản: Built-in
 - Workflow conditions phức tạp: Cần ScriptRunner hoặc Automation

#### Phiên Bản Nâng Cao (47 workflows):
- **Built-in**: Workflow structure có thể tạo bằng built-in
- **Advanced features**: 
 - Complex conditions: Cần ScriptRunner
 - Custom validators: Cần ScriptRunner
 - Advanced post-functions: Cần ScriptRunner hoặc Automation

**Kết luận**: 
- Workflows cơ bản: Built-in
- Workflows phức tạp: Cần ScriptRunner plugin hoặc Jira Automation

---

### 4. SLA CONFIGURATION

#### SLA Fields:
- **Severity** - Built-in (Jira Service Management)
- **First Response Time** - Built-in (Jira Service Management)
- **Resolution Time** - Built-in (Jira Service Management)
- **SLA Timer** - Built-in (Jira Service Management)

#### SLA Automation:
- **Auto-assignment** - Built-in (Jira Automation)
- **Escalation rules** - Built-in (Jira Automation)
- **Notification rules** - Built-in (Jira Automation)

**Kết luận**: 
- **Tất cả SLA features đều built-in trong Jira Service Management**
- **Cần license**: Jira Service Management (không có trong Jira Software/Core)

---

### 5. DASHBOARDS & REPORTS

#### Dashboards:
- **Built-in**: Jira có sẵn dashboard engine
- **Gadgets cơ bản**: Built-in (Issue Statistics, Created vs Resolved, etc.)
- **Advanced gadgets**: 
 - Effort tracking charts: Cần ScriptRunner hoặc custom gadgets
 - Advanced analytics: Cần plugins như eazyBI, Chart.js, hoặc custom development

#### Reports:
- **Built-in reports**: 
 - Sprint Report, Burndown Chart, Velocity Chart (Jira Software)
 - SLA Report, Service Level Report (Jira Service Management)
- **Advanced reports**: 
 - Effort Summary Report: Cần ScriptRunner hoặc custom
 - Financial Report: Cần plugin hoặc custom
 - Performance Report: Cần plugin hoặc custom

**Kết luận**: 
- Dashboards và reports cơ bản: Built-in
- Advanced dashboards/reports: Cần ScriptRunner hoặc plugins

---

### 6. AUTOMATION

#### Basic Automation:
- **Jira Automation** (built-in từ Jira 8.0+):
 - Auto-assignment
 - Auto-transition
 - Field auto-population
 - Notification rules
 - Basic calculations

#### Advanced Automation:
- **ScriptRunner** (plugin):
 - Complex calculations (Total Effort, Effort %, Variance)
 - Epic effort aggregation
 - Advanced conditions
 - Custom scripts

**Kết luận**: 
- Automation cơ bản: Built-in (Jira Automation)
- Automation phức tạp: Cần ScriptRunner plugin

---

### 7. INTEGRATIONS

#### GitLab Integration:
- **Built-in**: Jira có sẵn GitLab integration (từ Jira 8.0+)
- **Không cần plugin**: Sử dụng built-in GitLab integration

#### Confluence Integration:
- **Built-in**: Jira có sẵn Confluence integration
- **Không cần plugin**: Sử dụng built-in integration

#### Email Notifications:
- **Built-in**: Jira có sẵn email notification system
- **Không cần plugin**: Sử dụng built-in email

#### Slack Integration:
- **Plugin**: Cần cài đặt Slack integration plugin (có sẵn trên Atlassian Marketplace)

#### Monitoring Tools (Prometheus, Grafana):
- **Custom**: Cần custom development hoặc sử dụng REST API

#### BI Tools (Tableau, Power BI):
- **Custom**: Cần custom development sử dụng Jira REST API

**Kết luận**: 
- GitLab, Confluence, Email: Built-in
- Slack: Cần plugin
- Monitoring/BI Tools: Cần custom development

---

### 8. PERMISSIONS & ROLES

#### Roles:
- **Built-in**: Jira có sẵn permission system
- **Custom roles**: Có thể tạo bằng built-in Permission Schemes
- **Role-based permissions**: Built-in feature

**Kết luận**: 
- **Tất cả permission features đều built-in**

---

## TỔNG KẾT THEO PHIÊN BẢN

### PHIÊN BẢN CƠ BẢN (8 Issue Types)

#### Built-in (Không cần plugin):
- 8 Issue Types (cần Jira Software + Service Management license)
- 8 Effort Fields (Time Tracking - built-in)
- Classification Fields (Select List, User Picker - built-in)
- 9 Workflows (built-in Workflow Editor)
- SLA Configuration (Jira Service Management - built-in)
- 5 Dashboards cơ bản (built-in gadgets)
- Permissions & Roles (built-in)
- GitLab Integration (built-in)
- Email Notifications (built-in)
- Basic Automation (Jira Automation - built-in)

#### Cần Plugin/License:
- **Jira Software** license (cho Epic, Story, Task, Bug)
- **Jira Service Management** license (cho Incident, Change Request, Service Request, Service Order, SLA)
- **ScriptRunner** (optional - cho calculated fields và advanced automation)

**Tổng chi phí ước tính**:
- Jira Software: ~$7.75/user/month (Cloud) hoặc $10/user/year (Server/Data Center)
- Jira Service Management: ~$7.75/user/month (Cloud) hoặc $10/user/year (Server/Data Center)
- ScriptRunner: ~$5/user/year (optional)

---

### PHIÊN BẢN NÂNG CAO (39 Issue Types)

#### Built-in (Không cần plugin):
- 8 Issue Types đầu (Agile + ITIL Cơ Bản)
- 8 Effort Fields (Time Tracking - built-in)
- Classification Fields (built-in)
- Workflows cơ bản (built-in)
- SLA Configuration (built-in)
- Dashboards cơ bản (built-in)
- Permissions & Roles (built-in)
- GitLab, Confluence, Email (built-in)
- Basic Automation (built-in)

#### Cần Plugin/License:
- **Jira Software** license
- **Jira Service Management** license
- **ScriptRunner** (recommended - cho calculated fields, advanced automation)
- **Insight (CMDB)** hoặc **Assets for Jira** (cho Asset Management - 3 types)
- **eazyBI** hoặc **Chart.js** (optional - cho advanced dashboards)
- **Custom Issue Types** (31 types còn lại - có thể tạo bằng built-in hoặc cần plugin)

#### Custom Development:
- Advanced dashboards/reports (nếu không dùng plugin)
- Monitoring tools integration (Prometheus, Grafana)
- BI tools integration (Tableau, Power BI)
- Custom calculated fields (nếu không dùng ScriptRunner)

**Tổng chi phí ước tính**:
- Jira Software: ~$7.75/user/month
- Jira Service Management: ~$7.75/user/month
- ScriptRunner: ~$5/user/year (recommended)
- Insight (CMDB): ~$10/user/year (optional)
- eazyBI: ~$5/user/year (optional)

---

## KHUYẾN NGHỊ

### Cho Phiên Bản Cơ Bản:
1. **Jira Software** license (bắt buộc)
2. **Jira Service Management** license (bắt buộc)
3. **ScriptRunner** (khuyến nghị - cho calculated fields)

**Tổng**: 2 licenses bắt buộc + 1 plugin khuyến nghị

### Cho Phiên Bản Nâng Cao:
1. **Jira Software** license (bắt buộc)
2. **Jira Service Management** license (bắt buộc)
3. **ScriptRunner** (khuyến nghị - cho calculated fields và automation)
4. **Insight (CMDB)** (tùy chọn - cho Asset Management)
5. **eazyBI** (tùy chọn - cho advanced reports)

**Tổng**: 2 licenses bắt buộc + 1-3 plugins tùy chọn

---

## LƯU Ý QUAN TRỌNG

### 1. Custom Issue Types:
- **Có thể tạo bằng built-in**: Jira cho phép tạo custom issue types không giới hạn
- **Không cần plugin**: Tính năng built-in
- **Giới hạn**: Mỗi issue type cần có workflow riêng (built-in)

### 2. Calculated Fields:
- **Jira Automation** (built-in từ Jira 8.0+): Có thể tính toán đơn giản
- **ScriptRunner**: Cần cho calculations phức tạp (Total Effort, Effort %, Variance)

### 3. SLA:
- **Built-in trong Jira Service Management**: Không cần plugin
- **Cần license**: Jira Service Management (không có trong Jira Software)

### 4. Workflows:
- **Cơ bản**: Built-in
- **Advanced**: Cần ScriptRunner cho conditions/validators phức tạp

### 5. Dashboards:
- **Cơ bản**: Built-in gadgets
- **Advanced**: Cần plugins hoặc custom development

---

## KẾT LUẬN

### Có thể triển khai độc lập không?
 **CÓ** - Hầu hết tính năng đều có thể triển khai bằng built-in features của Jira.

### Cần mua license không?
 **CÓ** - Cần 2 licenses:
1. **Jira Software** (cho Agile features)
2. **Jira Service Management** (cho ITIL features và SLA)

### Cần plugin không?
 **TÙY CHỌN** - Khuyến nghị:
- **ScriptRunner**: Cho calculated fields và advanced automation (khuyến nghị)
- **Insight (CMDB)**: Cho Asset Management (tùy chọn)
- **eazyBI**: Cho advanced reports (tùy chọn)

### Cần code mở rộng không?
 **TÙY CHỌN** - Chỉ cần cho:
- Advanced integrations (Monitoring tools, BI tools)
- Custom dashboards/reports phức tạp (nếu không dùng plugin)

### Toàn bộ là build-in không?
 **KHÔNG HOÀN TOÀN** - Nhưng:
- **80-90% tính năng là built-in**
- **10-20% cần plugin hoặc custom development** (tùy chọn)

---

## TÀI LIỆU THAM KHẢO

- [Jira Software Documentation](https://support.atlassian.com/jira-software-cloud/)
- [Jira Service Management Documentation](https://support.atlassian.com/jira-service-management-cloud/)
- [ScriptRunner Documentation](https://scriptrunner.adaptavist.com/)
- [Jira Automation Documentation](https://support.atlassian.com/jira-service-management-cloud/docs/use-automation-rules-in-jira-service-management/)

---

**Lưu ý**: Chi phí và tính năng có thể thay đổi theo thời gian. Vui lòng kiểm tra trang web chính thức của Atlassian để có thông tin mới nhất.
