# ĐÁNH GIÁ STORY POINT & PERFORMANCE - DỰ ÁN & CON NGƯỜI

Tài liệu này hướng dẫn đánh giá Story Point và tính toán performance cho dự án và con người dựa trên Story Points và Effort tracking.

---

## 📋 MỤC LỤC

1. [Story Point - Khái niệm và Đánh giá](#1-story-point---khái-niệm-và-đánh-giá)
2. [Performance Metrics cho Dự án](#2-performance-metrics-cho-dự-án)
3. [Performance Metrics cho Con người](#3-performance-metrics-cho-con-người)
4. [Velocity Tracking](#4-velocity-tracking)
5. [Performance Indicators](#5-performance-indicators)
6. [Báo cáo Performance](#6-báo-cáo-performance)
7. [Custom Fields & Automation](#7-custom-fields--automation)
8. [JQL Queries cho Performance](#8-jql-queries-cho-performance)

---

## 1. STORY POINT - KHÁI NIỆM VÀ ĐÁNH GIÁ

### 1.1. Story Point là gì?

**Story Point** là đơn vị đo lường tương đối để ước lượng độ phức tạp và effort cần thiết để hoàn thành một Story.

**Đặc điểm**:
- Tương đối, không tuyệt đối (không phải giờ)
- Dựa trên độ phức tạp, không phải thời gian
- So sánh với Story khác (reference story)
- Team-based (mỗi team có scale riêng)

---

### 1.2. Fibonacci Scale

**Scale phổ biến**: 1, 2, 3, 5, 8, 13, 21

**Lý do sử dụng Fibonacci**:
- Phản ánh uncertainty tăng dần
- Dễ phân biệt giữa các mức độ
- Tránh over-precision

**Quy tắc**:
- **1 point**: Rất đơn giản, < 1 ngày
- **2 points**: Đơn giản, 1-2 ngày
- **3 points**: Trung bình, 2-3 ngày
- **5 points**: Phức tạp, 3-5 ngày
- **8 points**: Rất phức tạp, 5-8 ngày
- **13 points**: Cực kỳ phức tạp, > 8 ngày (nên split)
- **21 points**: Quá lớn, bắt buộc phải split

---

### 1.3. Cách Đánh giá Story Point

#### Bước 1: Chọn Reference Story
- Chọn 1 Story đơn giản làm baseline (ví dụ: 3 points)
- Tất cả Story khác so sánh với reference này

#### Bước 2: Planning Poker
1. Product Owner trình bày Story
2. Team members ước lượng độc lập (1, 2, 3, 5, 8, 13)
3. Reveal estimates cùng lúc
4. Nếu khác biệt lớn → Thảo luận
5. Repeat cho đến khi đồng thuận

#### Bước 3: Các yếu tố xem xét
- **Độ phức tạp**: Logic, algorithms, integrations
- **Rủi ro**: Unknowns, dependencies, technical debt
- **Effort**: Research, Development, Testing, Review
- **Uncertainty**: Requirements chưa rõ, technology mới

---

### 1.4. Story Point vs Effort (Hours)

**Mối quan hệ**:
- Story Point = Độ phức tạp (tương đối)
- Effort (Hours) = Thời gian thực tế (tuyệt đối)

**Ví dụ**:
- Story A: 3 points, 8 hours
- Story B: 3 points, 12 hours (có thể do developer khác, context khác)

**Velocity** = Story Points completed / Sprint
**Throughput** = Hours completed / Sprint

---

## 2. PERFORMANCE METRICS CHO DỰ ÁN

### 2.1. Velocity Metrics

#### A. Team Velocity
**Công thức**:
```
Team Velocity = Tổng Story Points completed trong Sprint
```

**Tính toán**:
- Track 5-10 sprints để có baseline
- Velocity trung bình = Average của các sprint
- Velocity trend = Xu hướng tăng/giảm

**JQL Query**:
```jql
project = PROJ AND type = Story AND status = Done AND sprint in closedSprints() AND sprint = "Sprint 1"
```

**Metrics**:
- **Average Velocity**: Velocity trung bình (5-10 sprints)
- **Velocity Trend**: Tăng/giảm/ổn định
- **Velocity Stability**: Độ ổn định (standard deviation)
- **Velocity Forecast**: Dự đoán velocity sprint tiếp theo

---

#### B. Epic Velocity
**Công thức**:
```
Epic Velocity = Tổng Story Points của Stories completed trong Epic
```

**Tính toán**:
- Track progress của Epic
- Forecast completion date dựa trên velocity

**JQL Query**:
```jql
project = PROJ AND type = Story AND "Epic Link" = PROJ-123 AND status = Done
```

**Metrics**:
- **Epic Progress %**: (Stories Done / Total Stories) × 100
- **Epic Velocity**: Story Points completed
- **Epic Forecast**: Estimated completion date

---

### 2.2. Throughput Metrics

#### A. Story Points per Hour
**Công thức**:
```
Story Points per Hour = Story Points completed / Total Effort (hours)
```

**Tính toán**:
- Đo lường hiệu quả: Story Points hoàn thành trên mỗi giờ effort
- So sánh giữa các sprint, epic, team

**Metrics**:
- **Average SP/Hour**: Trung bình Story Points per hour
- **SP/Hour Trend**: Xu hướng tăng/giảm
- **SP/Hour by Epic**: So sánh giữa các Epic

---

#### B. Throughput Rate
**Công thức**:
```
Throughput Rate = (Stories completed / Total Stories planned) × 100%
```

**Tính toán**:
- Tỷ lệ Stories hoàn thành so với kế hoạch
- Đo lường khả năng deliver theo plan

**Metrics**:
- **Throughput Rate**: % Stories completed
- **Throughput Trend**: Xu hướng qua các sprint
- **Forecast Accuracy**: So sánh planned vs actual

---

### 2.3. Quality Metrics

#### A. Bug Rate per Story Point
**Công thức**:
```
Bug Rate = Số lượng Bugs / Story Points completed
```

**Tính toán**:
- Số bugs tìm thấy trên mỗi Story Point
- Chỉ số chất lượng: Càng thấp càng tốt

**JQL Query**:
```jql
project = PROJ AND type = Bug AND "Linked Issues" = PROJ-123 AND created >= -30d
```

**Metrics**:
- **Bug Rate**: Bugs / Story Points
- **Bug Rate Trend**: Xu hướng qua các sprint
- **Bug Rate by Epic**: So sánh giữa các Epic

---

#### B. Defect Leakage Rate
**Công thức**:
```
Defect Leakage Rate = (Bugs found in Production / Total Bugs) × 100%
```

**Tính toán**:
- Tỷ lệ bugs lọt vào production
- Chỉ số chất lượng testing: Càng thấp càng tốt

**Metrics**:
- **Defect Leakage Rate**: % Bugs in production
- **Defect Leakage Trend**: Xu hướng qua các sprint

---

### 2.4. Efficiency Metrics

#### A. Story Point Accuracy
**Công thức**:
```
Story Point Accuracy = (Actual Effort / Estimated Effort) × 100%
```

**Tính toán**:
- Độ chính xác của estimation
- 100% = Perfect estimate
- < 100% = Under-estimated
- > 100% = Over-estimated

**Metrics**:
- **Estimation Accuracy**: % Accuracy
- **Estimation Trend**: Xu hướng cải thiện
- **Estimation by Story Size**: Accuracy theo Story Points

---

#### B. Cycle Time per Story Point
**Công thức**:
```
Cycle Time per SP = Cycle Time (days) / Story Points
```

**Tính toán**:
- Thời gian trung bình để hoàn thành 1 Story Point
- Cycle Time = Thời gian từ "In Progress" → "Done"

**Metrics**:
- **Average Cycle Time/SP**: Days per Story Point
- **Cycle Time/SP Trend**: Xu hướng
- **Cycle Time/SP by Epic**: So sánh giữa các Epic

---

### 2.5. Project Health Metrics

#### A. Sprint Goal Achievement
**Công thức**:
```
Sprint Goal Achievement = (Story Points completed / Story Points planned) × 100%
```

**Tính toán**:
- Tỷ lệ đạt mục tiêu sprint
- > 100% = Over-delivery
- < 100% = Under-delivery

**Metrics**:
- **Goal Achievement Rate**: % Achievement
- **Goal Achievement Trend**: Xu hướng qua các sprint

---

#### B. Epic Completion Rate
**Công thức**:
```
Epic Completion Rate = (Epics completed on time / Total Epics) × 100%
```

**Tính toán**:
- Tỷ lệ Epic hoàn thành đúng hạn
- Đo lường khả năng deliver theo timeline

**Metrics**:
- **Epic Completion Rate**: % On-time completion
- **Epic Completion Trend**: Xu hướng

---

## 3. PERFORMANCE METRICS CHO CON NGƯỜI

### 3.1. Individual Velocity

#### A. Story Points per Sprint
**Công thức**:
```
Individual Velocity = Tổng Story Points của Stories completed bởi team member trong Sprint
```

**Tính toán**:
- Track velocity của từng team member
- So sánh giữa các members
- Identify top performers và cần support

**JQL Query**:
```jql
project = PROJ AND type = Story AND assignee = "john.doe" AND status = Done AND sprint = "Sprint 1"
```

**Metrics**:
- **Individual Velocity**: Story Points per sprint
- **Average Individual Velocity**: Trung bình (5-10 sprints)
- **Velocity Trend**: Xu hướng tăng/giảm
- **Velocity Ranking**: Xếp hạng trong team

---

#### B. Story Points per Month
**Công thức**:
```
Story Points per Month = Tổng Story Points completed trong tháng
```

**Tính toán**:
- Track performance theo tháng
- So sánh giữa các tháng
- Identify patterns (seasonal, project-based)

**Metrics**:
- **Monthly Velocity**: Story Points per month
- **Monthly Velocity Trend**: Xu hướng
- **Peak Performance Month**: Tháng có velocity cao nhất

---

### 3.2. Individual Throughput

#### A. Story Points per Hour
**Công thức**:
```
Individual SP/Hour = Story Points completed / Total Effort (hours) của team member
```

**Tính toán**:
- Hiệu quả của team member: Story Points trên mỗi giờ
- So sánh giữa các members
- Identify efficiency improvements

**Metrics**:
- **Individual SP/Hour**: Story Points per hour
- **Average SP/Hour**: Trung bình
- **SP/Hour Trend**: Xu hướng
- **SP/Hour Ranking**: Xếp hạng

---

#### B. Throughput Rate
**Công thức**:
```
Individual Throughput Rate = (Stories completed / Stories assigned) × 100%
```

**Tính toán**:
- Tỷ lệ Stories hoàn thành so với được assign
- Đo lường khả năng deliver

**Metrics**:
- **Throughput Rate**: % Completion
- **Throughput Rate Trend**: Xu hướng

---

### 3.3. Quality Metrics

#### A. Bug Rate
**Công thức**:
```
Individual Bug Rate = Số lượng Bugs tạo ra / Story Points completed
```

**Tính toán**:
- Số bugs tạo ra trên mỗi Story Point
- Chỉ số chất lượng code: Càng thấp càng tốt

**JQL Query**:
```jql
project = PROJ AND type = Bug AND reporter = "john.doe" AND created >= -30d
```

**Metrics**:
- **Bug Rate**: Bugs / Story Points
- **Bug Rate Trend**: Xu hướng
- **Bug Rate Ranking**: Xếp hạng (càng thấp càng tốt)

---

#### B. Code Review Quality
**Công thức**:
```
Code Review Quality = (Issues found in review / Total reviews) × 100%
```

**Tính toán**:
- Tỷ lệ issues tìm thấy trong code review
- Đo lường chất lượng code trước khi review

**Metrics**:
- **Review Quality Score**: % Issues found
- **Review Quality Trend**: Xu hướng

---

### 3.4. Efficiency Metrics

#### A. Estimation Accuracy
**Công thức**:
```
Individual Estimation Accuracy = (Actual Effort / Estimated Effort) × 100%
```

**Tính toán**:
- Độ chính xác estimation của team member
- 100% = Perfect estimate
- < 100% = Under-estimated
- > 100% = Over-estimated

**Metrics**:
- **Estimation Accuracy**: % Accuracy
- **Estimation Accuracy Trend**: Xu hướng cải thiện
- **Estimation Accuracy Ranking**: Xếp hạng

---

#### B. Cycle Time Efficiency
**Công thức**:
```
Cycle Time Efficiency = (Average Cycle Time / Team Average Cycle Time) × 100%
```

**Tính toán**:
- So sánh cycle time của team member với team average
- < 100% = Nhanh hơn team average
- > 100% = Chậm hơn team average

**Metrics**:
- **Cycle Time Efficiency**: % vs Team Average
- **Cycle Time Efficiency Trend**: Xu hướng

---

### 3.5. Contribution Metrics

#### A. Story Points Contribution
**Công thức**:
```
Contribution % = (Individual Story Points / Team Story Points) × 100%
```

**Tính toán**:
- Tỷ lệ đóng góp của team member trong team
- Đo lường contribution level

**Metrics**:
- **Contribution %**: % Contribution
- **Contribution Trend**: Xu hướng
- **Contribution Ranking**: Xếp hạng

---

#### B. Cross-functional Contribution
**Công thức**:
```
Cross-functional Score = Số lượng issue types khác nhau đã làm
```

**Tính toán**:
- Số loại công việc khác nhau đã làm (Story, Task, Bug, etc.)
- Đo lường versatility

**Metrics**:
- **Cross-functional Score**: Số issue types
- **Cross-functional Trend**: Xu hướng

---

## 4. VELOCITY TRACKING

### 4.1. Team Velocity Tracking

#### Setup
1. **Baseline**: Track 5-10 sprints để có baseline
2. **Consistency**: Đảm bảo team size và composition ổn định
3. **Definition of Done**: Rõ ràng và consistent

#### Tracking
- **Sprint Velocity**: Story Points completed mỗi sprint
- **Average Velocity**: Trung bình (5-10 sprints)
- **Velocity Trend**: Tăng/giảm/ổn định
- **Velocity Forecast**: Dự đoán sprint tiếp theo

#### Analysis
- **Velocity Stability**: Standard deviation
- **Velocity Growth**: Tăng trưởng qua thời gian
- **Velocity Factors**: Yếu tố ảnh hưởng (team size, complexity, etc.)

---

### 4.2. Individual Velocity Tracking

#### Setup
1. **Track per Sprint**: Story Points completed mỗi sprint
2. **Track per Month**: Story Points completed mỗi tháng
3. **Track per Epic**: Story Points completed mỗi epic

#### Tracking
- **Individual Sprint Velocity**: Story Points per sprint
- **Individual Monthly Velocity**: Story Points per month
- **Individual Epic Velocity**: Story Points per epic

#### Analysis
- **Performance Trend**: Xu hướng tăng/giảm
- **Performance Ranking**: Xếp hạng trong team
- **Performance Factors**: Yếu tố ảnh hưởng

---

## 5. PERFORMANCE INDICATORS

### 5.1. Project Performance Indicators

#### Green (Good)
- ✅ Velocity ổn định hoặc tăng
- ✅ Sprint Goal Achievement > 90%
- ✅ Bug Rate < 0.5 bugs/SP
- ✅ Estimation Accuracy 80-120%
- ✅ Epic Completion Rate > 80%

#### Yellow (Warning)
- ⚠️ Velocity giảm < 10%
- ⚠️ Sprint Goal Achievement 70-90%
- ⚠️ Bug Rate 0.5-1 bugs/SP
- ⚠️ Estimation Accuracy 60-80% hoặc 120-150%
- ⚠️ Epic Completion Rate 60-80%

#### Red (Critical)
- ❌ Velocity giảm > 20%
- ❌ Sprint Goal Achievement < 70%
- ❌ Bug Rate > 1 bugs/SP
- ❌ Estimation Accuracy < 60% hoặc > 150%
- ❌ Epic Completion Rate < 60%

---

### 5.2. Individual Performance Indicators

#### Green (Good)
- ✅ Individual Velocity ổn định hoặc tăng
- ✅ SP/Hour > Team Average
- ✅ Bug Rate < Team Average
- ✅ Estimation Accuracy 80-120%
- ✅ Throughput Rate > 90%

#### Yellow (Warning)
- ⚠️ Individual Velocity giảm < 10%
- ⚠️ SP/Hour = Team Average ± 10%
- ⚠️ Bug Rate = Team Average ± 20%
- ⚠️ Estimation Accuracy 60-80% hoặc 120-150%
- ⚠️ Throughput Rate 70-90%

#### Red (Critical)
- ❌ Individual Velocity giảm > 20%
- ❌ SP/Hour < Team Average - 20%
- ❌ Bug Rate > Team Average + 50%
- ❌ Estimation Accuracy < 60% hoặc > 150%
- ❌ Throughput Rate < 70%

---

## 6. BÁO CÁO PERFORMANCE

### 6.1. Project Performance Report

#### Weekly Report
- Sprint velocity
- Sprint goal achievement
- Bug rate
- Active issues

#### Monthly Report
- Average velocity (last 3 months)
- Velocity trend
- Epic completion rate
- Quality metrics
- Efficiency metrics

#### Quarterly Report
- Comprehensive performance analysis
- Trends analysis
- Improvement recommendations
- Benchmark comparison

---

### 6.2. Individual Performance Report

#### Sprint Report
- Individual velocity
- Stories completed
- Bugs created
- Estimation accuracy

#### Monthly Report
- Average velocity (last 3 months)
- Velocity trend
- SP/Hour
- Quality metrics
- Efficiency metrics
- Contribution %

#### Quarterly Report
- Comprehensive performance analysis
- Performance ranking
- Improvement recommendations
- Career development suggestions

---

## 7. CUSTOM FIELDS & AUTOMATION

### 7.1. Custom Fields cho Performance

#### Story Fields
- **Story Points** (Number) - Required
- **Estimated Effort** (Time Tracking) - Optional
- **Actual Effort** (Time Tracking) - Auto-calculated
- **Effort Variance** (Number) - Auto-calculated
- **Cycle Time** (Number - days) - Auto-calculated
- **Bug Count** (Number) - Auto-calculated
- **Quality Score** (Number) - Auto-calculated

#### Epic Fields
- **Total Story Points** (Number) - Auto-calculated từ children
- **Completed Story Points** (Number) - Auto-calculated
- **Epic Progress %** (Number) - Auto-calculated
- **Epic Velocity** (Number) - Auto-calculated
- **Epic Forecast** (Date) - Auto-calculated

#### User Fields (Custom)
- **Individual Velocity** (Number) - Calculated
- **SP/Hour** (Number) - Calculated
- **Bug Rate** (Number) - Calculated
- **Estimation Accuracy** (Number) - Calculated

---

### 7.2. Automation Rules

#### Auto-calculate Effort Variance
- **Trigger**: When Actual Effort is updated
- **Action**: Calculate Effort Variance = (Actual - Estimated) / Estimated × 100
- **Update**: Effort Variance field

#### Auto-calculate Cycle Time
- **Trigger**: When Story transitions to "Done"
- **Action**: Calculate Cycle Time = (Done Date - In Progress Date) in days
- **Update**: Cycle Time field

#### Auto-calculate Bug Count
- **Trigger**: When Bug is created and linked to Story
- **Action**: Count Bugs linked to Story
- **Update**: Bug Count field

#### Auto-calculate Epic Progress
- **Trigger**: When Story in Epic transitions to "Done"
- **Action**: Calculate Epic Progress % = (Completed SP / Total SP) × 100
- **Update**: Epic Progress % field

#### Auto-calculate Individual Velocity
- **Trigger**: When Story assigned to user transitions to "Done"
- **Action**: Sum Story Points completed by user in sprint
- **Update**: Individual Velocity (custom field or report)

---

## 8. JQL QUERIES CHO PERFORMANCE

### 8.1. Project Performance Queries

#### Team Velocity
```jql
project = PROJ AND type = Story AND status = Done AND sprint in closedSprints() ORDER BY sprint DESC
```

#### Sprint Goal Achievement
```jql
project = PROJ AND sprint = "Sprint 1" AND type = Story AND status = Done
```

#### Bug Rate
```jql
project = PROJ AND type = Bug AND created >= -30d AND "Linked Issues" is not EMPTY
```

#### Estimation Accuracy
```jql
project = PROJ AND type = Story AND "Effort Variance" is not EMPTY AND "Effort Variance" > 20
```

#### Epic Progress
```jql
project = PROJ AND type = Epic AND status != Done AND "Epic Progress %" < 50
```

---

### 8.2. Individual Performance Queries

#### Individual Velocity
```jql
project = PROJ AND type = Story AND assignee = "john.doe" AND status = Done AND sprint = "Sprint 1"
```

#### Individual SP/Hour
```jql
project = PROJ AND type = Story AND assignee = "john.doe" AND status = Done AND "Total Effort" > 0
```

#### Individual Bug Rate
```jql
project = PROJ AND type = Bug AND reporter = "john.doe" AND created >= -30d
```

#### Individual Estimation Accuracy
```jql
project = PROJ AND type = Story AND assignee = "john.doe" AND "Effort Variance" is not EMPTY
```

#### Individual Contribution
```jql
project = PROJ AND type = Story AND assignee = "john.doe" AND status = Done AND sprint in closedSprints()
```

---

### 8.3. Performance Comparison Queries

#### Team vs Individual Velocity
```jql
project = PROJ AND type = Story AND status = Done AND sprint = "Sprint 1"
```

#### Performance Ranking
```jql
project = PROJ AND type = Story AND status = Done AND sprint in closedSprints() ORDER BY assignee
```

#### Quality Comparison
```jql
project = PROJ AND type = Bug AND created >= -30d ORDER BY reporter
```

---

## 📊 DASHBOARDS CHO PERFORMANCE

### 8.1. Project Performance Dashboard

**Gadgets**:
1. **Velocity Chart** - Story Points completed per sprint (line chart)
2. **Sprint Goal Achievement** - % Achievement (bar chart)
3. **Bug Rate Trend** - Bugs per Story Point (line chart)
4. **Estimation Accuracy** - % Accuracy (bar chart)
5. **Epic Progress** - Progress % by Epic (pie chart)

---

### 8.2. Individual Performance Dashboard

**Gadgets**:
1. **Individual Velocity** - Story Points per sprint (line chart)
2. **SP/Hour** - Story Points per hour (bar chart)
3. **Bug Rate** - Bugs per Story Point (line chart)
4. **Estimation Accuracy** - % Accuracy (bar chart)
5. **Contribution %** - % Contribution in team (pie chart)

---

## 📈 BEST PRACTICES

### 8.1. Story Point Estimation

**DO**:
- ✅ Sử dụng Planning Poker
- ✅ So sánh với reference story
- ✅ Xem xét độ phức tạp, rủi ro, effort
- ✅ Đồng thuận trong team
- ✅ Review và adjust sau mỗi sprint

**DON'T**:
- ❌ Convert Story Points sang hours
- ❌ So sánh Story Points giữa các team
- ❌ Sử dụng Story Points để đánh giá individual performance (trực tiếp)
- ❌ Thay đổi scale thường xuyên

---

### 8.2. Performance Evaluation

**DO**:
- ✅ Track multiple metrics (velocity, quality, efficiency)
- ✅ So sánh với baseline và trend
- ✅ Xem xét context (project, team, complexity)
- ✅ Provide feedback và support
- ✅ Celebrate improvements

**DON'T**:
- ❌ Chỉ dựa vào Story Points
- ❌ So sánh trực tiếp giữa team members
- ❌ Ignore context và factors
- ❌ Punish low performance
- ❌ Ignore quality metrics

---

## ✅ CHECKLIST

### Setup
- [ ] Define Story Point scale (Fibonacci)
- [ ] Choose reference story
- [ ] Setup custom fields
- [ ] Setup automation rules
- [ ] Create dashboards

### Tracking
- [ ] Track team velocity (5-10 sprints)
- [ ] Track individual velocity
- [ ] Track quality metrics
- [ ] Track efficiency metrics

### Reporting
- [ ] Weekly project report
- [ ] Monthly individual report
- [ ] Quarterly comprehensive report
- [ ] Performance review meetings

---

**Tài liệu này giúp đánh giá performance dựa trên Story Points và Effort tracking một cách toàn diện và công bằng.**
