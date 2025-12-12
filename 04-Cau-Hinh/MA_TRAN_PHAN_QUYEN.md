# MA TRẬN PHÂN QUYỀN - ROLE × ISSUE TYPE

## KÝ HIỆU

- ✅ **Create** - Có quyền tạo issue type này
- ✅ **Edit** - Có quyền chỉnh sửa issue type này
- ✅ **View** - Có quyền xem issue type này
- ✅ **Transition** - Có quyền chuyển trạng thái trong workflow
- ✅ **Assign** - Có quyền assign issue
- ✅ **Approve** - Có quyền approve (cho Change Request, etc.)
- ⚠️ **Limited** - Quyền hạn chế (chỉ một số trường hợp)
- ❌ **No** - Không có quyền

---

## PHIÊN BẢN CƠ BẢN - MA TRẬN PHÂN QUYỀN (7 Roles × 12 Issue Types)

| Issue Type | Product Owner | Developer | QA/Tester | Support | SRE/DevOps | CAB | Jira Admin |
|------------|---------------|-----------|-----------|---------|------------|-----|------------|
| **Epic** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All |
| **Story** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ✅ Create/Edit<br>✅ Transition (Dev flow)<br>✅ Assign (self) | ❌ | ❌ | ❌ | ❌ | ✅ All |
| **Task** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ✅ Create/Edit<br>✅ Transition (Dev flow)<br>✅ Assign (self) | ❌ | ❌ | ❌ | ❌ | ✅ All |
| **Bug** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ✅ Create/Edit<br>✅ Transition (Dev flow)<br>✅ Assign (self) | ✅ Create<br>✅ Edit (Testing results)<br>✅ Transition (Testing → Ready) | ❌ | ❌ | ❌ | ✅ All |
| **Incident** | ✅ View<br>✅ Approve (nếu liên quan) | ✅ View (read-only) | ❌ | ✅ Create (SEV2-SEV3)<br>✅ Edit<br>✅ Transition | ✅ Create (SEV1-SEV2)<br>✅ Edit<br>✅ Transition | ❌ | ✅ All |
| **Change Request** | ✅ Create/Edit<br>✅ Approve<br>✅ Transition | ✅ View (read-only) | ❌ | ❌ | ✅ Create (Ops scope)<br>✅ Approve (deployment)<br>✅ Transition | ✅ Approve/Reject<br>✅ Transition (CAB Review) | ✅ All |
| **Service Request** | ✅ View<br>✅ Approve (nếu cần) | ❌ | ❌ | ✅ Create/Edit<br>✅ Transition | ❌ | ❌ | ✅ All |
| **Service Order** | ✅ View | ❌ | ❌ | ✅ View | ❌ | ❌ | ✅ All |
| **Product Research** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ⚠️ View<br>⚠️ Edit (nếu assigned) | ❌ | ❌ | ❌ | ❌ | ✅ All |
| **Product Development** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ✅ Create/Edit<br>✅ Transition (Dev flow)<br>✅ Assign (self) | ✅ Edit (Testing results)<br>✅ Transition (Testing → Ready) | ❌ | ⚠️ View | ❌ | ✅ All |
| **Project Deployment** | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ⚠️ View<br>⚠️ Edit (nếu assigned) | ❌ | ❌ | ✅ Create/Edit<br>✅ Transition<br>✅ Assign | ❌ | ✅ All |
| **Project Operations** | ✅ View | ❌ | ❌ | ✅ Create/Edit<br>✅ Transition | ✅ Create/Edit<br>✅ Transition | ❌ | ✅ All |

---

## PHIÊN BẢN NÂNG CAO - MA TRẬN PHÂN QUYỀN (12 Roles × 47 Issue Types)

### Roles:
1. Product Owner
2. Developer
3. QA/Tester
4. Support
5. SRE/DevOps
6. CAB
7. Jira Admin
8. Problem Manager
9. Knowledge Manager
10. Change Manager
11. Service Manager
12. Security Officer

### Issue Types (47):

| Issue Type | PO | Dev | QA | Support | SRE | CAB | Admin | Problem Mgr | Knowledge Mgr | Change Mgr | Service Mgr | Security |
|------------|----|-----|----|---------|-----|-----|-------|-------------|---------------|------------|-------------|----------|
| **Epic** | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Story** | ✅ All | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Task** | ✅ All | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Bug** | ✅ All | ✅ Create/Edit/Transition | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Incident** | ✅ View | ✅ View | ❌ | ✅ Create (SEV2-3)/Edit/Transition | ✅ Create (SEV1-2)/Edit/Transition | ❌ | ✅ All | ✅ View | ❌ | ❌ | ✅ View | ✅ View |
| **Change Request** | ✅ Approve | ✅ View | ❌ | ❌ | ✅ Create/Approve (deploy) | ✅ Approve/Reject | ✅ All | ✅ View | ❌ | ✅ Create/Edit/Transition | ✅ View | ✅ View |
| **Service Request** | ✅ View/Approve | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Service Order** | ✅ View | ❌ | ❌ | ✅ View | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Problem** | ✅ View | ✅ View | ❌ | ✅ View | ✅ View | ❌ | ✅ All | ✅ Create/Edit/Transition | ❌ | ❌ | ✅ View | ✅ View |
| **Knowledge Article** | ✅ View | ✅ View | ✅ View | ✅ View | ✅ View | ❌ | ✅ All | ✅ View | ✅ Create/Edit/Transition | ❌ | ✅ View | ❌ |
| **SLA Review** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Service Catalog Item** | ✅ View | ❌ | ❌ | ✅ View | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Availability Incident** | ✅ View | ❌ | ❌ | ✅ View | ✅ Create/Edit/Transition | ❌ | ✅ All | ✅ View | ❌ | ❌ | ✅ View | ❌ |
| **Capacity Request** | ✅ Approve | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Disaster Recovery Plan** | ✅ View | ❌ | ❌ | ❌ | ✅ View | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ✅ View |
| **Disaster Recovery Test** | ✅ View | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ✅ View |
| **Security Incident** | ✅ View | ❌ | ❌ | ❌ | ✅ View | ❌ | ✅ All | ✅ View | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition |
| **Security Assessment** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition |
| **Supplier** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Supplier Performance Review** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **IT Asset** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Asset Request** | ✅ Approve | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Configuration Item (CI)** | ✅ View | ✅ View | ❌ | ❌ | ✅ View | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Release** | ✅ Create/Edit/Transition | ✅ View | ✅ View | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ✅ View | ✅ View | ❌ |
| **Deployment** | ✅ View | ✅ View | ✅ View | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Risk** | ✅ Create/Edit/Transition | ✅ View | ❌ | ❌ | ✅ View | ❌ | ✅ All | ✅ View | ❌ | ❌ | ✅ View | ✅ View |
| **Portfolio Item** | ✅ Create/Edit/Transition | ✅ View | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Budget** | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Customer** | ✅ View | ❌ | ❌ | ✅ View | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ |
| **Customer Feedback** | ✅ View | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Demand Forecast** | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Policy** | ✅ View | ✅ View | ✅ View | ✅ View | ✅ View | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition |
| **Compliance Audit** | ✅ View | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition |
| **Requirement** | ✅ Create/Edit/Transition | ✅ View | ✅ View | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Test Case** | ✅ View | ✅ View | ✅ Create/Edit/Transition | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Product Research** | ✅ Create/Edit/Transition | ✅ View | ❌ | ❌ | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Product Development** | ✅ Create/Edit/Transition | ✅ Create/Edit/Transition | ✅ Edit (Testing) | ❌ | ✅ View | ❌ | ✅ All | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Product Deployment** | ✅ Create/Edit/Transition | ✅ View | ✅ View | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Product Operations** | ✅ View | ❌ | ❌ | ❌ | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Project Research** | ✅ Create/Edit/Transition | ✅ View | ❌ | ✅ View | ❌ | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Project Development** | ✅ Create/Edit/Transition | ✅ Create/Edit/Transition | ✅ Edit (Testing) | ✅ View | ✅ View | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Project Deployment** | ✅ Create/Edit/Transition | ✅ View | ❌ | ✅ View | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |
| **Project Operations** | ✅ View | ❌ | ❌ | ✅ Create/Edit/Transition | ✅ Create/Edit/Transition | ❌ | ✅ All | ❌ | ❌ | ❌ | ✅ View | ❌ |

---

## CHI TIẾT QUYỀN HẠN

### Product Owner:
- ✅ Tạo/Edit/Transition: Epic, Story, Task, Bug, Change Request, Product Research, Product Development, Product Deployment, Project Research, Project Development, Project Deployment, Risk, Portfolio Item, Budget, Demand Forecast, Requirement
- ✅ Approve: Change Request, Capacity Request, Asset Request
- ✅ View: Tất cả issue types

### Developer:
- ✅ Tạo/Edit/Transition: Story, Task, Bug, Product Development, Project Development (trong Dev workflow)
- ✅ View: Epic, Incident, Change Request, Product Research, Product Deployment, Project Research, Project Deployment, Release, Deployment, Risk, Policy, Requirement, Test Case, Configuration Item

### QA/Tester:
- ✅ Tạo/Edit/Transition: Bug, Test Case (trong Testing workflow)
- ✅ Edit: Story, Task, Product Development, Project Development (Testing results only)
- ✅ View: Story, Task, Product Development, Project Deployment, Release, Deployment, Requirement, Knowledge Article, Policy

### Support:
- ✅ Tạo/Edit/Transition: Service Request, Incident (SEV2-SEV3), Project Operations, Customer Feedback
- ✅ View: Service Order, Product Research, Project Research, Project Development, Project Deployment, Customer, Knowledge Article, Policy

### SRE/DevOps:
- ✅ Tạo/Edit/Transition: Incident (SEV1-SEV2), Change Request (Ops scope), Product Deployment, Project Deployment, Project Operations, Availability Incident, Capacity Request, Disaster Recovery Test, Release, Deployment
- ✅ Approve: Change Request (deployment)
- ✅ View: Story, Task, Bug, Problem, Security Incident, Risk, Configuration Item, Product Development, Project Research, Project Development

### CAB:
- ✅ Approve/Reject: Change Request
- ✅ Transition: Change Request (CAB Review → Approved/Rejected)

### Problem Manager:
- ✅ Tạo/Edit/Transition: Problem
- ✅ View: Incident, Change Request, Availability Incident, Security Incident, Risk

### Knowledge Manager:
- ✅ Tạo/Edit/Transition: Knowledge Article
- ✅ View: Tất cả issue types (để tạo knowledge articles)

### Change Manager:
- ✅ Tạo/Edit/Transition: Change Request
- ✅ View: Incident, Problem, Release

### Service Manager:
- ✅ Tạo/Edit/Transition: Service Request, Service Catalog Item, SLA Review, Supplier, Supplier Performance Review, IT Asset, Configuration Item, Customer, Disaster Recovery Plan
- ✅ View: Tất cả service-related issues

### Security Officer:
- ✅ Tạo/Edit/Transition: Security Incident, Security Assessment, Policy, Compliance Audit
- ✅ View: Incident, Problem, Change Request, Risk, Disaster Recovery Plan, Disaster Recovery Test

### Jira Admin:
- ✅ All permissions trên tất cả issue types
- ❌ Không tham gia vận hành sản phẩm

---

## EFFORT TRACKING PERMISSIONS

### Quyền Log Effort:
- ✅ **Tất cả roles** có thể log effort vào các effort fields (Research, Development, Deployment, Operations) cho issues được assign cho họ
- ✅ **Product Owner** có thể log effort cho tất cả issues
- ✅ **Jira Admin** có thể log effort cho tất cả issues

### Quyền View Effort Reports:
- ✅ **Product Owner**: Xem tất cả effort reports
- ✅ **Jira Admin**: Xem tất cả effort reports
- ✅ **Service Manager**: Xem effort reports cho service-related issues
- ⚠️ **Other roles**: Chỉ xem effort reports cho issues được assign cho họ hoặc trong projects họ có quyền

---

## NOTES

1. **Limited permissions** có thể được customize dựa trên nhu cầu cụ thể
2. **View permissions** mặc định cho tất cả roles trong cùng project
3. **Effort tracking** có thể được log bởi bất kỳ role nào cho issues được assign cho họ
4. **Admin permissions** nên được giới hạn để tránh xung đột quy trình

---

**Ma trận này cung cấp framework rõ ràng để cấu hình permissions trong Jira.**
