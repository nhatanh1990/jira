# CHECKLIST TRIỂN KHAI JIRA - CHI TIẾT TỪNG BƯỚC

## PHASE 1: CHUẨN BỊ & PLANNING

### 1.1. Phân tích yêu cầu
- [ ] Xác định các teams và roles cần thiết
- [ ] Xác định issue types cần sử dụng
- [ ] Xác định workflows cho từng issue type
- [ ] Xác định custom fields cần thiết
- [ ] Xác định dashboards cần tạo
- [ ] Xác định integration points (GitLab, etc.)

### 1.2. Tạo user accounts
- [ ] Tạo accounts cho tất cả users
- [ ] Group users theo teams
- [ ] Assign roles cho từng user
- [ ] Setup email notifications

---

## PHASE 2: PROJECT SETUP

### 2.1. Tạo Project
- [ ] Tạo project mới
- [ ] Chọn project template (Scrum + IT Service Management)
- [ ] Đặt project key (ví dụ: PROJ, AI, MFG)
- [ ] Đặt project name và description
- [ ] Assign project lead

### 2.2. Issue Types
- [ ] Kích hoạt Epic
- [ ] Kích hoạt Story
- [ ] Kích hoạt Task
- [ ] Kích hoạt Bug
- [ ] Tạo Service Request (custom issue type)
- [ ] Tạo Service Order (custom issue type)
- [ ] Tạo Incident (custom issue type)
- [ ] Tạo Change Request (custom issue type)
- [ ] Tạo Ops Task (custom issue type nếu cần)

### 2.3. Issue Type Scheme
- [ ] Tạo Issue Type Scheme
- [ ] Assign issue types vào scheme
- [ ] Link scheme với project

---

## PHASE 3: CUSTOM FIELDS

### 3.1. Agile Custom Fields
- [ ] Story Points (Select List: 1,2,3,5,8,13,21)
- [ ] Original Estimate (Time Tracking)
- [ ] Time Spent (Time Tracking)
- [ ] Remaining Estimate (Time Tracking)
- [ ] Acceptance Criteria (Text Area)
- [ ] AI Feature Type (Select List)
- [ ] Manufacturing Process (Select List)
- [ ] Bug Type (Select List)
- [ ] Environment (Select List)
- [ ] Severity (Select List - cho Bug)

### 3.2. ITIL Custom Fields
- [ ] Severity (Select List: SEV1, SEV2, SEV3, SEV4)
- [ ] Impact (Select List)
- [ ] Urgency (Select List)
- [ ] Priority (Select List: P1, P2, P3, P4)
- [ ] Incident Category (Select List)
- [ ] Root Cause (Text Area)
- [ ] Resolution Time (Number - hours)
- [ ] First Response Time (Number - minutes)
- [ ] Change Type (Select List)
- [ ] Change Category (Select List)
- [ ] Risk Level (Select List)
- [ ] CAB Approval (Select List)
- [ ] Request Type (Select List)
- [ ] Service Catalog Item (Text)
- [ ] SLA Target (Date)
- [ ] Order Number (Text)
- [ ] Total Cost (Number)
- [ ] Payment Status (Select List)

### 3.3. Performance Fields
- [ ] Team Member (User Picker)
- [ ] Velocity (Number)
- [ ] Effort Variance (Number)
- [ ] Performance Score (Number)
- [ ] Quality Metrics (Text Area)
- [ ] AI Model Performance (Text Area)
- [ ] Manufacturing Efficiency (Number)

### 3.4. Field Configuration
- [ ] Tạo Field Configuration Scheme
- [ ] Set required fields cho từng issue type
- [ ] Set hidden fields cho từng issue type
- [ ] Link Field Configuration Scheme với project

---

## PHASE 4: WORKFLOWS

### 4.1. Agile Workflow
- [ ] Tạo workflow: To Do → In Progress → Code Review → Testing → Ready for Release → Done
- [ ] Thêm transition: Any → Blocked
- [ ] Thêm transition: Testing → In Progress
- [ ] Setup conditions cho transitions
- [ ] Setup validators cho transitions
- [ ] Setup post-functions cho transitions
- [ ] Assign workflow cho Story, Task, Bug

### 4.2. Epic Workflow
- [ ] Tạo workflow: To Do → In Progress → Done
- [ ] Assign workflow cho Epic

### 4.3. Service Request Workflow
- [ ] Tạo workflow: New → In Progress → Pending Approval → Approved → Fulfilled → Closed
- [ ] Thêm transition: Pending Approval → Rejected → Closed
- [ ] Setup conditions và validators
- [ ] Assign workflow cho Service Request

### 4.4. Service Order Workflow
- [ ] Tạo workflow: Order Received → Processing → Payment Pending → In Production → Shipped → Delivered → Closed
- [ ] Thêm transition: Payment Pending → Payment Failed → Cancelled
- [ ] Assign workflow cho Service Order

### 4.5. Incident Workflow (ITIL)
- [ ] Tạo workflow: New → Acknowledged → Investigating → Mitigated → Resolved → Closed
- [ ] Thêm transition: Any → Escalated
- [ ] Thêm transition: Any → On Hold
- [ ] Setup SLA post-functions
- [ ] Assign workflow cho Incident

### 4.6. Change Request Workflow (ITIL)
- [ ] Tạo workflow: Draft → Submitted → Under Review → CAB Review → Approved → Implementation → Testing → Completed → Closed
- [ ] Thêm transition: Under Review → Rejected → Closed
- [ ] Thêm transition: CAB Review → Rejected → Closed
- [ ] Setup conditions cho Emergency Change
- [ ] Assign workflow cho Change Request

### 4.7. Workflow Scheme
- [ ] Tạo Workflow Scheme
- [ ] Map issue types với workflows
- [ ] Link Workflow Scheme với project

---

## PHASE 5: SCREENS

### 5.1. Create Screens
- [ ] Epic Create Screen
- [ ] Story Create Screen
- [ ] Task Create Screen
- [ ] Bug Create Screen
- [ ] Service Request Create Screen
- [ ] Service Order Create Screen
- [ ] Incident Create Screen
- [ ] Change Request Create Screen

### 5.2. Edit Screens
- [ ] Epic Edit Screen
- [ ] Story Edit Screen
- [ ] Task Edit Screen
- [ ] Bug Edit Screen
- [ ] Service Request Edit Screen
- [ ] Service Order Edit Screen
- [ ] Incident Edit Screen
- [ ] Change Request Edit Screen

### 5.3. View Screens
- [ ] Epic View Screen
- [ ] Story View Screen
- [ ] Task View Screen
- [ ] Bug View Screen
- [ ] Service Request View Screen
- [ ] Service Order View Screen
- [ ] Incident View Screen
- [ ] Change Request View Screen

### 5.4. Transition Screens
- [ ] Agile Transition Screen
- [ ] ITIL Transition Screen

### 5.5. Screen Schemes
- [ ] Tạo Agile Screen Scheme
- [ ] Tạo ITIL Screen Scheme
- [ ] Map issue types với screen schemes
- [ ] Link Screen Scheme với project

---

## PHASE 6: PERMISSIONS

### 6.1. Permission Scheme
- [ ] Tạo Permission Scheme mới
- [ ] Copy từ default scheme
- [ ] Customize permissions cho từng role

### 6.2. Product Owner Permissions
- [ ] Browse Projects: 
- [ ] Create/Edit Issues: 
- [ ] Transition Issues: (all)
- [ ] Delete Issues: 
- [ ] Administer Projects: 
- [ ] Approve Change Request: 

### 6.3. Developer Permissions
- [ ] Browse Projects: 
- [ ] Create Issues: (Story, Task, Bug only)
- [ ] Edit Issues: (Story, Task, Bug only)
- [ ] Transition Issues: (Dev workflow only)
- [ ] View Incident: (read-only)
- [ ] View Change Request: (read-only)

### 6.4. QA/Tester Permissions
- [ ] Browse Projects: 
- [ ] Create Issues: (Bug only)
- [ ] Edit Issues: (Testing results only)
- [ ] Transition Issues: (Testing → Ready for Release)

### 6.5. Support Permissions
- [ ] Browse Projects: 
- [ ] Create Issues: (Service Request, Incident SEV2-SEV3)
- [ ] Edit Issues: (Service Request, Incident)
- [ ] Transition Issues: (SR and Incident workflows)

### 6.6. SRE/DevOps Permissions
- [ ] Browse Projects: 
- [ ] Create Issues: (Incident SEV1-SEV2, Change Request, Ops Task)
- [ ] Edit Issues: (Incident, Change Request, Ops Task)
- [ ] Transition Issues: (Incident, Change Request workflows)
- [ ] Approve Change Request: 

### 6.7. CAB Permissions
- [ ] Browse Projects: 
- [ ] View Issues: (all)
- [ ] Edit Issues: (Change Request - approval only)
- [ ] Transition Issues: (CAB Review → Approved/Rejected)

### 6.8. Jira Admin Permissions
- [ ] All administrative permissions: 
- [ ] Không tham gia vận hành: 

### 6.9. Apply Permissions
- [ ] Link Permission Scheme với project
- [ ] Test permissions với test users

---

## PHASE 7: ITIL CONFIGURATION

### 7.1. Incident Management
- [ ] Setup Severity levels (SEV1-SEV4)
- [ ] Setup Impact levels
- [ ] Setup Urgency levels
- [ ] Setup Priority calculation (Impact × Urgency)
- [ ] Configure SLA rules (xem SLA_CONFIGURATION.md):
 - [ ] SEV1: First Response 15 min, Resolution 4 hours, Escalation 30 min
 - [ ] SEV2: First Response 1 hour, Resolution 8 hours, Escalation 2 hours
 - [ ] SEV3: First Response 4 hours, Resolution 24 hours, Escalation 8 hours
 - [ ] SEV4: First Response 1 day, Resolution 3 days, Escalation 2 days
- [ ] Setup SLA custom fields (SLA Status, First Response Time Target/Actual, Resolution Time Target/Actual, Escalation Level)
- [ ] Configure business hours (SEV1-SEV2: 24/7, SEV3-SEV4: Business Hours)
- [ ] Setup auto-assignment rules
- [ ] Setup escalation rules
- [ ] Setup SLA automation (auto-calculate SLA Status, auto-escalate)

### 7.2. Change Management
- [ ] Setup Change Types (Standard, Normal, Emergency)
- [ ] Setup Change Categories
- [ ] Setup Risk Levels
- [ ] Create CAB group
- [ ] Add CAB members
- [ ] Setup approval workflow
- [ ] Setup Emergency Change process
- [ ] Configure SLA rules (xem SLA_CONFIGURATION.md):
 - [ ] Standard Change: Implementation 2 days
 - [ ] Normal Change: Review 2 days, Approval 3 days, Implementation 5 days (Total: 10 days)
 - [ ] Emergency Change: Review 2 hours, Approval 4 hours, Implementation 1 day (Total: 1.5 days)
- [ ] Setup SLA custom fields (SLA Status, Review/Approval/Implementation Time Target/Actual)
- [ ] Configure business hours (Standard/Normal: Business Hours, Emergency: 24/7)
- [ ] Setup SLA automation
- [ ] Configure post-implementation review

### 7.3. Service Request
- [ ] Setup Request Types (Access Request, Information Request, Service Provisioning, Other)
- [ ] Setup Service Catalog items
- [ ] Configure approval workflow
- [ ] Configure SLA rules (xem SLA_CONFIGURATION.md):
 - [ ] Access Request: Response 2 hours, Fulfillment 1 day
 - [ ] Information Request: Response 1 hour, Fulfillment 4 hours
 - [ ] Service Provisioning: Response 4 hours, Fulfillment 3 days
 - [ ] Other: Response 4 hours, Fulfillment 5 days
- [ ] Setup SLA custom fields (SLA Status, Response/Fulfillment Time Target/Actual, SLA Target Date)
- [ ] Configure business hours (Business Hours: 8:00-18:00, Monday-Friday)
- [ ] Setup SLA automation

### 7.4. Service Order
- [ ] Setup Order lifecycle
- [ ] Configure payment status workflow
- [ ] Configure SLA rules (xem SLA_CONFIGURATION.md):
 - [ ] Order Received → Processing: 2 hours
 - [ ] Processing → Payment Confirmed: 1 day
 - [ ] Payment Confirmed → In Production: 1 day
 - [ ] Delivery: Theo Delivery Date trong order terms
- [ ] Setup SLA custom fields (SLA Status, Processing/Payment/Production Time Target/Actual, Delivery SLA Status)
- [ ] Configure business hours (Business Hours: 8:00-18:00, Monday-Friday)
- [ ] Setup SLA automation
- [ ] Link với Service Request (nếu cần)

---

## PHASE 8: AUTOMATION

### 8.1. Auto-assignment Rules
- [ ] Bug → Assign to QA team lead
- [ ] Incident SEV1 → Assign to SRE on-call
- [ ] Service Request → Assign to Support team
- [ ] Change Request → Assign to Change Manager

### 8.2. Auto-transition Rules
- [ ] MR Created → Transition to "Code Review"
- [ ] MR Merged → Transition to "Testing"
- [ ] Pipeline Passes → Auto-assign to QA

### 8.3. Field Auto-population
- [ ] Priority (Incident) → Auto-calculate từ Impact + Urgency
- [ ] Resolution Time → Auto-calculate từ timestamps
- [ ] First Response Time → Auto-calculate từ timestamps
- [ ] SLA Status → Auto-calculate (On Track, At Risk, Breached)
- [ ] SLA Target Date → Auto-calculate từ Created Date + SLA Target
- [ ] SLA Breach → Auto-set khi vượt SLA

### 8.4. SLA Automation Rules
- [ ] Auto-calculate SLA Status (At Risk = 80% target, Breached = >100% target)
- [ ] Auto-escalate khi SLA At Risk
- [ ] Auto-escalate khi SLA Breached
- [ ] Auto-notify khi SLA At Risk (2 giờ trước breach)
- [ ] Auto-notify khi SLA Breached
- [ ] Auto-assign dựa trên SLA status

### 8.5. Notification Rules
- [ ] SEV1 Incident → Notify SRE team + Management
- [ ] Change Request approved → Notify implementation team
- [ ] SLA breach → Escalate to manager
- [ ] SLA At Risk → Notify assignee + team lead
- [ ] Daily SLA report → Gửi báo cáo SLA compliance hàng ngày

---

## PHASE 9: INTEGRATIONS

### 9.1. GitLab Integration
- [ ] Install GitLab for Jira app
- [ ] Connect GitLab instance
- [ ] Link Jira project với GitLab project
- [ ] Configure branch naming convention
- [ ] Setup auto-transition rules
- [ ] Test integration

### 9.2. Other Integrations (nếu cần)
- [ ] Slack notifications
- [ ] Email notifications
- [ ] CI/CD pipeline integration
- [ ] Monitoring tools integration

---

## PHASE 10: DASHBOARDS

### 10.1. Executive Dashboard
- [ ] Portfolio Summary gadget
- [ ] ITIL Service Health gadget
- [ ] AI Projects Overview gadget
- [ ] Manufacturing Impact gadget
- [ ] Team Performance gadget
- [ ] Financial Overview gadget

### 10.2. Product Owner Dashboard
- [ ] Sprint Progress gadget
- [ ] Backlog Management gadget
- [ ] Release Planning gadget
- [ ] Team Velocity gadget
- [ ] Quality Metrics gadget

### 10.3. Development Team Dashboard
- [ ] My Work gadget
- [ ] Sprint Board gadget
- [ ] GitLab Integration gadget
- [ ] Time Tracking gadget

### 10.4. QA Dashboard
- [ ] Testing Queue gadget
- [ ] Quality Metrics gadget
- [ ] Test Results gadget

### 10.5. Support Dashboard
- [ ] Service Request Queue gadget
- [ ] Incident Management gadget
- [ ] Customer Satisfaction gadget

### 10.6. SRE/DevOps Dashboard
- [ ] Incident Management gadget
- [ ] Change Management gadget
- [ ] Infrastructure Health gadget
- [ ] AI Service Monitoring gadget

### 10.7. Manufacturing Dashboard
- [ ] Production Issues gadget
- [ ] Service Orders gadget
- [ ] Efficiency Metrics gadget
- [ ] AI in Manufacturing gadget

### 10.8. ITIL Service Management Dashboard
- [ ] Service Health gadget
- [ ] Change Management gadget
- [ ] Service Catalog gadget
- [ ] Problem Management gadget

---

## PHASE 11: REPORTS

### 11.1. Agile Reports
- [ ] Sprint Report
- [ ] Burndown Chart
- [ ] Velocity Chart
- [ ] Cumulative Flow Diagram
- [ ] Epic Report
- [ ] Version Report

### 11.2. ITIL Reports
- [ ] Incident Report
- [ ] Change Management Report
- [ ] SLA Report
- [ ] Service Request Report
- [ ] Problem Management Report

### 11.3. Performance Reports
- [ ] Time Tracking Report
- [ ] Effort Variance Report
- [ ] Team Performance Report
- [ ] Quality Metrics Report

---

## PHASE 12: TESTING

### 12.1. Workflow Testing
- [ ] Test Agile workflow với test user (Developer)
- [ ] Test Epic workflow với test user (PO)
- [ ] Test Service Request workflow với test user (Support)
- [ ] Test Incident workflow với test user (SRE)
- [ ] Test Change Request workflow với test user (CAB)
- [ ] Verify transitions hoạt động đúng
- [ ] Verify conditions và validators

### 12.2. Permission Testing
- [ ] Test Product Owner permissions
- [ ] Test Developer permissions
- [ ] Test QA permissions
- [ ] Test Support permissions
- [ ] Test SRE permissions
- [ ] Test CAB permissions
- [ ] Verify restrictions hoạt động đúng

### 12.3. Custom Fields Testing
- [ ] Test tạo issue với required fields
- [ ] Test validation rules
- [ ] Test field visibility
- [ ] Test field calculations

### 12.4. Automation Testing
- [ ] Test auto-assignment rules
- [ ] Test auto-transition rules
- [ ] Test notification rules
- [ ] Test field auto-population

### 12.5. Integration Testing
- [ ] Test GitLab integration
- [ ] Test branch creation từ Jira
- [ ] Test MR creation từ Jira
- [ ] Test auto-transition khi MR merged

---

## PHASE 13: TRAINING & DOCUMENTATION

### 13.1. User Training
- [ ] Training cho Product Owners
- [ ] Training cho Development Team
- [ ] Training cho QA Team
- [ ] Training cho Support Team
- [ ] Training cho SRE/DevOps Team
- [ ] Training cho CAB Members
- [ ] Training cho Jira Admins

### 13.2. Documentation
- [ ] Tạo user guide cho từng role
- [ ] Tạo workflow documentation
- [ ] Tạo process documentation
- [ ] Tạo FAQ document
- [ ] Tạo troubleshooting guide

### 13.3. Best Practices
- [ ] Document best practices cho issue creation
- [ ] Document best practices cho ITIL processes
- [ ] Document best practices cho performance tracking

---

## PHASE 14: GO-LIVE

### 14.1. Pre-Go-Live
- [ ] Final review của tất cả configurations
- [ ] Backup current configuration
- [ ] Communicate go-live date với teams
- [ ] Prepare support team

### 14.2. Go-Live
- [ ] Activate project
- [ ] Migrate existing data (nếu có)
- [ ] Monitor system performance
- [ ] Collect initial feedback

### 14.3. Post-Go-Live
- [ ] Daily check-ins với teams (tuần đầu)
- [ ] Address issues và questions
- [ ] Fine-tune configurations dựa trên feedback
- [ ] Schedule follow-up training nếu cần

---

## PHASE 15: MAINTENANCE & OPTIMIZATION

### 15.1. Regular Maintenance
- [ ] Weekly review của workflows
- [ ] Monthly review của permissions
- [ ] Quarterly review của dashboards
- [ ] Regular cleanup của old issues

### 15.2. Continuous Improvement
- [ ] Collect feedback từ users
- [ ] Analyze metrics và reports
- [ ] Identify improvement opportunities
- [ ] Implement improvements
- [ ] Document changes

---

## NOTES

- Checklist này nên được điều chỉnh dựa trên nhu cầu cụ thể
- Một số items có thể được thực hiện song song
- Ưu tiên các items critical trước
- Test thoroughly trước khi go-live
- Document mọi thay đổi

---

**Status Legend:**
- = Completed
- = Not applicable / Restricted
- [ ] = Pending
