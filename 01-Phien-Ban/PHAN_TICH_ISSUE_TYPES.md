# PHÂN TÍCH 4 ISSUE TYPES - CÓ CẦN THIẾT KHÔNG?

## TỔNG QUAN

Phân tích 4 issue types:
1. Product Research
2. Product Development
3. Project Deployment
4. Project Operations

**Câu hỏi**: Có thể gom vào Epic/Story không? Có thực sự cần thiết không?

---

## PHÂN TÍCH CHI TIẾT

### 1. PRODUCT RESEARCH

#### Mục đích hiện tại:
- Quản lý nghiên cứu sản phẩm
- Track research effort

#### So sánh với Epic/Story:

**Epic có thể thay thế?**
- Epic có thể chứa nhiều Stories về research
- Epic có thể track Total Research Effort từ children
- Epic có thể có custom fields: Research Phase, Research Status

**Story có thể thay thế?**
- Story có thể là "Research user needs for feature X"
- Story có thể track Research Effort
- Story có thể có acceptance criteria về research deliverables

**Kết luận**: 
- **KHÔNG CẦN THIẾT** - Có thể dùng Epic/Story với custom fields
- Epic cho research projects lớn
- Story cho research tasks cụ thể

---

### 2. PRODUCT DEVELOPMENT

#### Mục đích hiện tại:
- Quản lý phát triển sản phẩm
- Track development effort

#### So sánh với Epic/Story:

**Epic có thể thay thế?**
- Epic có thể là "Develop Feature X"
- Epic có thể track Total Development Effort từ children
- Epic có thể có custom fields: Development Phase, Development Status

**Story có thể thay thế?**
- Story là cách chuẩn để quản lý development
- Story có thể track Development Effort
- Story có thể có acceptance criteria, story points

**Kết luận**:
- **KHÔNG CẦN THIẾT** - Story đã là cách chuẩn để quản lý development
- Story là issue type chính cho development
- Epic để quản lý nhóm Stories

---

### 3. PROJECT DEPLOYMENT

#### Mục đích hiện tại:
- Triển khai project cho khách hàng
- Track deployment effort

#### So sánh với Epic/Story:

**Epic có thể thay thế?**
- Epic có thể là "Deploy Project X for Customer Y"
- Epic có thể track Total Deployment Effort từ children
- Epic có thể có custom fields: Deployment Phase, Customer, Deployment Date

**Story có thể thay thế?**
- Story có thể là "Setup environment for Customer X"
- Story có thể track Deployment Effort
- Story có thể có acceptance criteria về deployment

**Task có thể thay thế?**
- Task có thể là "Deploy to production", "Migrate data", "Training"
- Task có thể track Deployment Effort
- Task phù hợp cho deployment tasks cụ thể

**Kết luận**:
- **CÓ THỂ KHÔNG CẦN THIẾT** - Có thể dùng Epic/Story/Task với custom fields
- Epic cho deployment project lớn
- Story/Task cho deployment tasks cụ thể
- **NHƯNG**: Nếu deployment là process phức tạp, có thể cần issue type riêng

---

### 4. PROJECT OPERATIONS

#### Mục đích hiện tại:
- Vận hành và support project
- Track operations effort

#### So sánh với Epic/Story/Task:

**Epic có thể thay thế?**
- Epic có thể là "Operations for Customer X"
- Epic có thể track Total Operations Effort từ children
- Epic có thể có custom fields: Operations Type, SLA Compliance

**Story/Task có thể thay thế?**
- Task có thể là "Support ticket", "Maintenance task", "Optimization task"
- Task có thể track Operations Effort
- Task phù hợp cho operations tasks cụ thể

**Service Request có thể thay thế?**
- Service Request đã có sẵn trong ITIL
- Service Request có thể track Operations Effort
- Service Request phù hợp cho customer requests

**Kết luận**:
- **KHÔNG CẦN THIẾT** - Có thể dùng Task hoặc Service Request
- Task cho operations tasks
- Service Request cho customer service requests
- Epic để quản lý nhóm operations tasks

---

## KẾT LUẬN VÀ KHUYẾN NGHỊ

### Đánh giá:

| Issue Type | Cần thiết? | Có thể thay thế bằng | Khuyến nghị |
|------------|------------|---------------------|-------------|
| **Product Research** | Không | Epic/Story | **LOẠI BỎ** - Dùng Epic/Story |
| **Product Development** | Không | Story | **LOẠI BỎ** - Story đã đủ |
| **Project Deployment** | Tùy chọn | Epic/Story/Task | **CÓ THỂ LOẠI BỎ** - Dùng Epic/Story/Task |
| **Project Operations** | Không | Task/Service Request | **LOẠI BỎ** - Dùng Task/Service Request |

---

## ĐỀ XUẤT: LOẠI BỎ 4 ISSUE TYPES

### Lý do:

1. **Trùng lặp chức năng**:
 - Product Research/Development có thể dùng Epic/Story
 - Project Deployment có thể dùng Epic/Story/Task
 - Project Operations có thể dùng Task/Service Request

2. **Epic/Story đã đủ mạnh**:
 - Epic có thể track effort từ children
 - Story có thể track effort trực tiếp
 - Custom fields có thể phân biệt loại công việc

3. **Đơn giản hóa hệ thống**:
 - Giảm số lượng issue types
 - Dễ sử dụng hơn
 - Dễ training hơn

4. **Best practices**:
 - Epic/Story là cách chuẩn trong Agile
 - Không cần tạo issue types riêng cho mỗi phase

---

## CÁCH THAY THẾ

### 1. Product Research → Epic/Story

**Sử dụng Epic khi**:
- Research project lớn, nhiều research tasks
- Cần track tổng research effort từ nhiều stories

**Sử dụng Story khi**:
- Research task cụ thể
- Có acceptance criteria rõ ràng

**Custom Fields cần thêm**:
- **Work Type**: Product, Project (để phân biệt)
- **Phase**: Research, Development, Deployment, Operations
- **Research Phase**: Market Research, User Research, Requirements Analysis, Architecture Design
- **Research Status**: In Progress, Completed, On Hold

**Ví dụ**:
- Epic: "Research AI Features for Manufacturing"
 - Story: "Research user needs for AI quality control"
 - Story: "Research competitor AI solutions"
 - Story: "Research technical feasibility"

---

### 2. Product Development → Story

**Sử dụng Story**:
- Story là cách chuẩn cho development
- Track Development Effort trực tiếp
- Có Story Points, Acceptance Criteria

**Custom Fields cần thêm**:
- **Work Type**: Product, Project
- **Phase**: Research, Development, Deployment, Operations
- **Development Phase**: Design, Development, Testing, Integration
- **Development Status**: In Progress, Code Review, Testing, Completed

**Ví dụ**:
- Epic: "Develop AI Quality Control Feature"
 - Story: "Implement ML model for defect detection"
 - Story: "Create API for quality control"
 - Story: "Build UI for quality dashboard"

---

### 3. Project Deployment → Epic/Story/Task

**Sử dụng Epic khi**:
- Deployment project lớn, nhiều deployment tasks
- Cần track tổng deployment effort

**Sử dụng Story/Task khi**:
- Deployment task cụ thể
- Setup, migration, training tasks

**Custom Fields cần thêm**:
- **Work Type**: Product, Project
- **Phase**: Research, Development, Deployment, Operations
- **Customer**: User Picker (cho Project issues)
- **Deployment Phase**: Planning, Setup, Data Migration, Training, Go-live
- **Deployment Status**: Planned, In Progress, Completed, Rolled Back
- **Deployment Environment**: Production, Staging, Development

**Ví dụ**:
- Epic: "Deploy AI System for Customer ABC"
 - Story: "Setup production environment"
 - Task: "Migrate customer data"
 - Task: "Train customer users"
 - Task: "Go-live support"

---

### 4. Project Operations → Task/Service Request

**Sử dụng Task khi**:
- Operations task cụ thể
- Maintenance, optimization tasks

**Sử dụng Service Request khi**:
- Customer service request
- Standard service request

**Custom Fields cần thêm**:
- **Work Type**: Product, Project
- **Phase**: Research, Development, Deployment, Operations
- **Customer**: User Picker (cho Project issues)
- **Operations Type**: Maintenance, Support, Optimization, Monitoring
- **SLA Compliance**: Number (0-100%)

**Ví dụ**:
- Task: "Optimize AI model performance for Customer ABC"
- Task: "Monthly maintenance for Customer ABC"
- Service Request: "Customer ABC requests new feature"

---

## CẤU TRÚC MỚI (SAU KHI LOẠI BỎ)

### Phiên Bản Cơ Bản: 8 Issue Types (từ 12)

1. Epic
2. Story
3. Task
4. Bug
5. Incident
6. Change Request
7. Service Request
8. Service Order

**Loại bỏ**:
- Product Research
- Product Development
- Project Deployment
- Project Operations

### Phiên Bản Nâng Cao: 39 Issue Types (từ 47, loại bỏ 8 types)

**Loại bỏ**:
- Product Research
- Product Development
- Product Deployment
- Product Operations
- Project Research
- Project Development
- Project Deployment
- Project Operations

**Thay thế bằng**: Epic/Story/Task với custom fields (Work Type, Phase, Customer)

---

## CUSTOM FIELDS ĐỂ PHÂN BIỆT

### Work Type Field:
- **Values**: Product, Project, Support, ITIL
- **Mục đích**: Phân biệt loại công việc

### Phase Field:
- **Values**: Research, Development, Testing, Deployment, Operations
- **Mục đích**: Phân biệt phase của công việc

### Customer Field (cho Project):
- **Type**: User Picker
- **Mục đích**: Link với khách hàng

### Ví dụ sử dụng:

**Epic với Work Type = Product, Phase = Research**:
- Tương đương Product Research

**Story với Work Type = Product, Phase = Development**:
- Tương đương Product Development

**Epic với Work Type = Project, Phase = Deployment, Customer = ABC**:
- Tương đương Project Deployment

**Task với Work Type = Project, Phase = Operations, Customer = ABC**:
- Tương đương Project Operations

---

## KHUYẾN NGHỊ CUỐI CÙNG

### LOẠI BỎ 4 ISSUE TYPES

**Lý do**:
1. Epic/Story/Task đã đủ mạnh để thay thế
2. Custom fields (Work Type, Phase, Customer) có thể phân biệt
3. Đơn giản hóa hệ thống
4. Tuân thủ Agile best practices
5. Dễ sử dụng và training hơn

**Cách thay thế**:
- Sử dụng Epic/Story/Task với custom fields
- Sử dụng Work Type và Phase để phân loại
- Sử dụng Customer field cho Project issues

**Kết quả**:
- Giảm từ 12 → 8 issue types (Cơ bản)
- Giảm từ 47 → 39 issue types (Nâng cao)
- Vẫn track effort đầy đủ (8 effort fields)
- Hệ thống đơn giản hơn, dễ sử dụng hơn

---

## IMPLEMENTATION PLAN

### Bước 1: Loại bỏ Issue Types
- [ ] Remove Product Research issue type
- [ ] Remove Product Development issue type
- [ ] Remove Project Deployment issue type
- [ ] Remove Project Operations issue type

### Bước 2: Thêm Custom Fields
- [ ] Add Work Type field (Product, Project, Support, ITIL)
- [ ] Add Phase field (Research, Development, Testing, Deployment, Operations)
- [ ] Ensure Customer field exists (cho Project issues)

### Bước 3: Migrate Existing Issues
- [ ] Migrate Product Research → Epic/Story với Work Type=Product, Phase=Research
- [ ] Migrate Product Development → Story với Work Type=Product, Phase=Development
- [ ] Migrate Project Deployment → Epic/Story/Task với Work Type=Project, Phase=Deployment
- [ ] Migrate Project Operations → Task/Service Request với Work Type=Project, Phase=Operations

### Bước 4: Update Documentation
- [ ] Update workflows
- [ ] Update dashboards
- [ ] Update JQL queries
- [ ] Update training materials

---

**Kết luận: 4 issue types này KHÔNG CẦN THIẾT và có thể LOẠI BỎ, thay thế bằng Epic/Story/Task với custom fields phù hợp.**
