# WORKFLOW DIAGRAMS - SƠ ĐỒ QUY TRÌNH

## 1. AGILE WORKFLOW (Story/Task/Bug)

```
┌─────────┐
│  To Do  │
└────┬────┘
     │
     │ Developer starts work
     ▼
┌──────────────┐
│ In Progress  │
└────┬─────────┘
     │
     │ Developer creates MR
     ▼
┌──────────────┐
│ Code Review  │
└────┬─────────┘
     │
     │ Code approved
     ▼
┌──────────┐
│ Testing  │◄────┐
└────┬─────┘     │
     │           │ Bug found
     │ QA passes │
     ▼           │
┌──────────────────┐
│ Ready for Release│
└────┬─────────────┘
     │
     │ PO/Release Manager
     ▼
┌────────┐
│  Done  │
└────────┘

     │
     │ Any status (if blocked)
     ▼
┌──────────┐
│ Blocked  │
└──────────┘
```

**Transitions:**
- To Do → In Progress: Developer
- In Progress → Code Review: Developer (after MR created)
- Code Review → Testing: Code Reviewer/Dev Lead
- Testing → Ready for Release: QA/Tester
- Testing → In Progress: If bug found
- Ready for Release → Done: PO/Release Manager
- Any → Blocked: Anyone (requires reason)

---

## 2. EPIC WORKFLOW

```
┌─────────┐
│  To Do  │
└────┬────┘
     │
     │ PO starts Epic
     ▼
┌──────────────┐
│ In Progress  │
└────┬─────────┘
     │
     │ All Stories done
     ▼
┌────────┐
│  Done  │
└────────┘
```

**Transitions:**
- To Do → In Progress: Product Owner
- In Progress → Done: Product Owner (when all stories completed)

---

## 3. SERVICE REQUEST WORKFLOW

```
┌─────────┐
│   New   │
└────┬────┘
     │
     │ Support picks up
     ▼
┌──────────────┐
│ In Progress  │
└────┬─────────┘
     │
     │ Needs approval?
     ▼
┌──────────────────┐
│ Pending Approval │
└────┬─────────────┘
     │
     ├──────────────┐
     │              │
     │ Approved     │ Rejected
     ▼              ▼
┌──────────┐   ┌──────────┐
│ Approved │   │ Rejected │
└────┬─────┘   └────┬─────┘
     │              │
     │              │
     │ Fulfilled    │
     ▼              │
┌──────────┐        │
│Fulfilled │        │
└────┬─────┘        │
     │              │
     └──────┬───────┘
            │
            ▼
        ┌────────┐
        │ Closed │
        └────────┘
```

**Transitions:**
- New → In Progress: Support/Customer Service
- In Progress → Pending Approval: Support (if approval needed)
- Pending Approval → Approved: PO/Manager
- Pending Approval → Rejected: PO/Manager
- Approved → Fulfilled: Support/DevOps
- Fulfilled → Closed: Support/Customer Service
- Rejected → Closed: Support/Customer Service

---

## 4. SERVICE ORDER WORKFLOW

```
┌─────────────────┐
│  Order Received │
└────────┬────────┘
         │
         │ Validation
         ▼
┌──────────────┐
│  Processing  │
└────┬─────────┘
     │
     │ Validated
     ▼
┌──────────────────┐
│ Payment Pending  │
└────┬─────────────┘
     │
     ├──────────────┐
     │              │
     │ Paid         │ Payment Failed
     ▼              ▼
┌──────────────┐   ┌──────────┐
│In Production │   │Cancelled │
└────┬─────────┘   └──────────┘
     │
     │ Production complete
     ▼
┌──────────┐
│ Shipped  │
└────┬─────┘
     │
     │ Delivered
     ▼
┌──────────┐
│Delivered │
└────┬─────┘
     │
     │ Confirmed
     ▼
┌────────┐
│ Closed │
└────────┘
```

**Transitions:**
- Order Received → Processing: Order Manager
- Processing → Payment Pending: Order Manager
- Payment Pending → In Production: Payment confirmed
- Payment Pending → Cancelled: Payment failed
- In Production → Shipped: Manufacturing complete
- Shipped → Delivered: Delivery confirmed
- Delivered → Closed: Customer confirmed

---

## 5. INCIDENT WORKFLOW (ITIL)

```
┌─────────┐
│   New   │
└────┬────┘
     │
     │ First response (within SLA)
     ▼
┌──────────────┐
│ Acknowledged │
└────┬─────────┘
     │
     │ SRE/DevOps starts investigation
     ▼
┌──────────────────┐
│  Investigating   │
└────┬─────────────┘
     │
     ├──────────────┐
     │              │
     │ Workaround   │ Escalated
     ▼              ▼
┌──────────┐   ┌──────────┐
│Mitigated │   │Escalated │
└────┬─────┘   └──────────┘
     │
     │ Permanent fix
     ▼
┌──────────┐
│ Resolved │
└────┬─────┘
     │
     │ Support confirms
     ▼
┌────────┐
│ Closed │
└────────┘

     │
     │ Any status (if waiting)
     ▼
┌──────────┐
│  On Hold │
└──────────┘
```

**Transitions:**
- New → Acknowledged: Support/SRE (within SLA)
- Acknowledged → Investigating: SRE/DevOps
- Investigating → Mitigated: SRE/DevOps (workaround applied)
- Mitigated → Resolved: SRE/DevOps (permanent fix)
- Resolved → Closed: Support (after confirmation)
- Any → Escalated: If SLA breached or SEV1
- Any → On Hold: Waiting for external information

**SLA Rules:**
- SEV1: First Response 15 min, Resolution 4 hours
- SEV2: First Response 1 hour, Resolution 8 hours
- SEV3: First Response 4 hours, Resolution 24 hours
- SEV4: First Response 1 day, Resolution 3 days

---

## 6. CHANGE REQUEST WORKFLOW (ITIL)

```
┌─────────┐
│  Draft  │
└────┬────┘
     │
     │ Developer/SRE submits
     ▼
┌──────────────┐
│  Submitted   │
└────┬─────────┘
     │
     │ Change Manager reviews
     ▼
┌──────────────┐
│ Under Review │
└────┬─────────┘
     │
     ├──────────────┐
     │              │
     │ Normal/Emerg │ Standard
     │              │
     ▼              ▼
┌──────────────┐   ┌──────────┐
│  CAB Review  │   │Approved  │
└────┬─────────┘   └────┬─────┘
     │                  │
     ├──────────────┐   │
     │              │   │
     │ Approved     │   │
     │              │   │
     ▼              │   │
┌──────────────┐   │   │
│   Approved   │   │   │
└────┬─────────┘   │   │
     │              │   │
     │              │   │
     └──────┬───────┘   │
            │           │
            │ Rejected  │
            ▼           │
     ┌──────────┐       │
     │ Rejected │       │
     └────┬─────┘       │
          │             │
          │             │
          └──────┬──────┘
                 │
                 │ Implementation
                 ▼
          ┌──────────────┐
          │Implementation│
          └────┬─────────┘
               │
               │ Deployed
               ▼
          ┌──────────┐
          │ Testing  │
          └────┬─────┘
               │
               │ Tests pass
               ▼
          ┌──────────┐
          │Completed │
          └────┬─────┘
               │
               │ Change Manager closes
               ▼
          ┌────────┐
          │ Closed │
          └────────┘
```

**Transitions:**
- Draft → Submitted: Developer/SRE
- Submitted → Under Review: Change Manager
- Under Review → CAB Review: Change Manager (if Normal/Emergency)
- Under Review → Approved: Change Manager (if Standard)
- CAB Review → Approved: CAB Members (majority vote)
- CAB Review → Rejected: CAB Members
- Approved → Implementation: SRE/DevOps
- Implementation → Testing: SRE/DevOps
- Testing → Completed: QA/SRE
- Completed → Closed: Change Manager
- Rejected → Closed: Change Manager

**Emergency Change:**
- Bỏ qua CAB Review
- Cần approval từ 2 CAB members
- Fast-track to Implementation

---

## 7. WORKFLOW RELATIONSHIPS

### 7.1. Incident → Change Request

```
Incident (Resolved)
     │
     │ Root cause identified
     │ Needs permanent fix
     ▼
Change Request (Draft)
     │
     │ ... workflow ...
     │
     ▼
Change Request (Completed)
     │
     │ Link back to Incident
     ▼
Incident (Closed)
```

### 7.2. Service Request → Service Order

```
Service Request (Fulfilled)
     │
     │ Requires paid service
     ▼
Service Order (Order Received)
     │
     │ ... workflow ...
     │
     ▼
Service Order (Delivered)
     │
     │ Link back to SR
     ▼
Service Request (Closed)
```

### 7.3. Story → Bug

```
Story (Ready for Release)
     │
     │ Deployed to Production
     │ Bug found
     ▼
Bug (New)
     │
     │ ... workflow ...
     │
     ▼
Bug (Done)
     │
     │ Link back to Story
     ▼
Story (Done - verified)
```

---

## 8. STATUS MAPPING

### 8.1. Agile Statuses
- **To Do**: Chưa bắt đầu
- **In Progress**: Đang làm
- **Code Review**: Đang review code
- **Testing**: Đang test
- **Ready for Release**: Sẵn sàng release
- **Done**: Hoàn thành
- **Blocked**: Bị chặn

### 8.2. ITIL Statuses

**Incident:**
- **New**: Mới tạo
- **Acknowledged**: Đã xác nhận
- **Investigating**: Đang điều tra
- **Mitigated**: Đã giảm thiểu (workaround)
- **Resolved**: Đã giải quyết
- **Closed**: Đã đóng
- **Escalated**: Đã leo thang
- **On Hold**: Tạm dừng

**Change Request:**
- **Draft**: Nháp
- **Submitted**: Đã gửi
- **Under Review**: Đang xem xét
- **CAB Review**: Đang review bởi CAB
- **Approved**: Đã phê duyệt
- **Rejected**: Đã từ chối
- **Implementation**: Đang triển khai
- **Testing**: Đang test
- **Completed**: Hoàn thành
- **Closed**: Đã đóng

**Service Request:**
- **New**: Mới
- **In Progress**: Đang xử lý
- **Pending Approval**: Chờ phê duyệt
- **Approved**: Đã phê duyệt
- **Rejected**: Đã từ chối
- **Fulfilled**: Đã thực hiện
- **Closed**: Đã đóng

**Service Order:**
- **Order Received**: Đã nhận đơn
- **Processing**: Đang xử lý
- **Payment Pending**: Chờ thanh toán
- **Payment Failed**: Thanh toán thất bại
- **In Production**: Đang sản xuất
- **Shipped**: Đã giao hàng
- **Delivered**: Đã giao
- **Cancelled**: Đã hủy
- **Closed**: Đã đóng

---

## 9. TRANSITION CONDITIONS

### 9.1. Common Conditions

**Assignee Check:**
- Only assignee can transition
- Only specific roles can transition

**Field Requirements:**
- Required fields must be filled
- Certain fields must have specific values

**SLA Checks:**
- Check if SLA is met
- Check if escalation needed

**Approval Checks:**
- Check if approval is required
- Check if approval is granted

### 9.2. Post-Functions

**Common Post-Functions:**
- Update field values
- Assign to specific user/group
- Add comment
- Trigger webhook
- Send notification
- Create subtask
- Link issues
- Calculate SLA

---

## 10. WORKFLOW VALIDATION

### 10.1. Validation Rules

**Before Transition:**
- Required fields must be filled
- User must have permission
- Conditions must be met

**After Transition:**
- Update timestamps
- Calculate metrics
- Trigger notifications
- Update related issues

### 10.2. Error Handling

**Common Errors:**
- Missing required fields
- Permission denied
- Invalid transition
- Workflow violation

**Resolution:**
- Show error message
- Prevent transition
- Log error
- Notify admin

---

## NOTES

- Workflows có thể được customize dựa trên nhu cầu cụ thể
- Thêm/bớt status và transitions khi cần
- Test thoroughly trước khi deploy
- Document mọi thay đổi
- Train users về workflows

---

**Legend:**
- ┌─┐ = Status box
- ─→ = Transition arrow
- │ = Flow direction
- ▼ = Down flow
- ◄─ = Back flow
