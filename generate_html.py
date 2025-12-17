#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo website tĩnh đơn giản - tất cả gói gọn trong 1 file HTML
"""

import json
import html

# Danh sách file markdown theo cấu trúc thư mục
files = {
    'intro': 'README.md',
    'phien-ban-co-ban': '01-Phien-Ban/PHIEN_BAN_CO_BAN.md',
    'phien-ban-nang-cao': '01-Phien-Ban/PHIEN_BAN_NANG_CAO.md',
    'phan-tich-issue-types': '01-Phien-Ban/PHAN_TICH_ISSUE_TYPES.md',
    'kich-ban-trien-khai': '02-Huong-Dan-Trien-Khai/KICH_BAN_TRIEN_KHAI.md',
    'checklist-trien-khai': '02-Huong-Dan-Trien-Khai/CHECKLIST_TRIEN_KHAI.md',
    'huong-dan-trien-khai-jira': '02-Huong-Dan-Trien-Khai/HUONG_DAN_TRIEN_KHAI_JIRA.md',
    'huong-dan-member-moi': '03-Huong-Dan-Su-Dung/HUONG_DAN_MEMBER_MOI.md',
    'tai-lieu-training': '03-Huong-Dan-Su-Dung/TAI_LIEU_TRAINING.md',
    'kich-ban-su-dung': '03-Huong-Dan-Su-Dung/KICH_BAN_SU_DUNG.md',
    'ma-tran-phan-quyen': '04-Cau-Hinh/MA_TRAN_PHAN_QUYEN.md',
    'sla-configuration': '04-Cau-Hinh/SLA_CONFIGURATION.md',
    'workflow-diagrams': '04-Cau-Hinh/WORKFLOW_DIAGRAMS.md',
    'effort-tracking': '05-Effort-Tracking/EFFORT_TRACKING_HOAN_THIEN.md',
    'danh-gia-hoan-thien': '05-Effort-Tracking/DANH_GIA_HOAN_THIEN.md',
    'story-point-performance': '05-Effort-Tracking/DANH_GIA_STORY_POINT_PERFORMANCE.md',
    'bo-sung-itil': '06-ITIL-Quan-Tri/BO_SUNG_ITIL_VA_QUAN_TRI.md',
    'jql-queries': '07-Reference/JQL_QUERIES.md',
    'troubleshooting-faq': '07-Reference/TROUBLESHOOTING_FAQ.md',
    'bao-cao-tong-hop': '07-Reference/BAO_CAO_TONG_HOP.md'
}

print("Đang đọc các file markdown...")
content_map = {}
for key, filepath in files.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            content_map[key] = content
            print(f"✓ {filepath}")
    except Exception as e:
        print(f"✗ Lỗi khi đọc {filepath}: {e}")
        content_map[key] = f"# Error\n\nKhông thể tải file: {filepath}\n\nError: {str(e)}"

# Convert to JSON and escape
json_str = json.dumps(content_map, ensure_ascii=False, indent=2)
json_str_escaped = json_str.replace('</script>', '<\\/script>').replace('</', '<\\/')

print(f"\nĐã load {len(content_map)} files")
print(f"Tổng kích thước: {len(json_str)} characters")

# Tạo HTML đơn giản
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ Thống Quản Lý Jira - VNPT AI</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }}
        
        .container {{
            display: flex;
            min-height: 100vh;
        }}
        
        /* Sidebar */
        .sidebar {{
            width: 280px;
            background: #2c3e50;
            color: white;
            padding: 20px;
            overflow-y: auto;
            position: fixed;
            height: 100vh;
        }}
        
        .sidebar h1 {{
            font-size: 1.3em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }}
        
        .nav-section {{
            margin-bottom: 25px;
        }}
        
        .nav-section h3 {{
            color: #3498db;
            font-size: 0.9em;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}
        
        .nav-item {{
            display: block;
            padding: 8px 12px;
            color: #ecf0f1;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        
        .nav-item:hover {{
            background: #34495e;
            padding-left: 16px;
        }}
        
        .nav-item.active {{
            background: #3498db;
            color: white;
        }}
        
        /* Main Content */
        .main-content {{
            margin-left: 280px;
            flex: 1;
            padding: 30px;
            max-width: 1000px;
        }}
        
        .content-section {{
            display: none;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .content-section.active {{
            display: block;
        }}
        
        .content-section h1 {{
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }}
        
        .content-section h2 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        .content-section h3 {{
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        .content-section p {{
            margin-bottom: 15px;
        }}
        
        .content-section ul, .content-section ol {{
            margin-left: 20px;
            margin-bottom: 15px;
        }}
        
        .content-section li {{
            margin-bottom: 8px;
        }}
        
        .content-section code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        
        .content-section pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin-bottom: 15px;
        }}
        
        .content-section pre code {{
            background: none;
            padding: 0;
        }}
        
        .content-section table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        
        .content-section table th,
        .content-section table td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        
        .content-section table th {{
            background: #3498db;
            color: white;
        }}
        
        .content-section table tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        
        .info-box {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        
        .info-box h3 {{
            margin-top: 0;
            color: #1976d2;
        }}
        
        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                height: auto;
                position: relative;
            }}
            
            .main-content {{
                margin-left: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Sidebar Navigation -->
        <nav class="sidebar">
            <h1>📚 Tài Liệu Jira</h1>
            
            <div class="nav-section">
                <h3>Bắt Đầu</h3>
                <a href="#" class="nav-item active" data-section="intro">Giới Thiệu</a>
            </div>
            
            <div class="nav-section">
                <h3>Cho Admin/Manager</h3>
                <a href="#" class="nav-item" data-section="phien-ban-co-ban">1. Phiên Bản Cơ Bản</a>
                <a href="#" class="nav-item" data-section="phien-ban-nang-cao">2. Phiên Bản Nâng Cao</a>
                <a href="#" class="nav-item" data-section="phan-tich-issue-types">3. Phân Tích Issue Types</a>
                <a href="#" class="nav-item" data-section="kich-ban-trien-khai">4. Kịch Bản Triển Khai</a>
                <a href="#" class="nav-item" data-section="checklist-trien-khai">5. Checklist Triển Khai</a>
                <a href="#" class="nav-item" data-section="ma-tran-phan-quyen">6. Ma Trận Phân Quyền</a>
                <a href="#" class="nav-item" data-section="sla-configuration">7. Cấu Hình SLA</a>
                <a href="#" class="nav-item" data-section="effort-tracking">8. Effort Tracking</a>
                <a href="#" class="nav-item" data-section="story-point-performance">9. Story Point & Performance</a>
            </div>
            
            <div class="nav-section">
                <h3>Cho Users</h3>
                <a href="#" class="nav-item" data-section="huong-dan-member-moi">1. Hướng Dẫn Member Mới</a>
                <a href="#" class="nav-item" data-section="tai-lieu-training">2. Tài Liệu Training</a>
                <a href="#" class="nav-item" data-section="kich-ban-su-dung">3. Kịch Bản Sử Dụng</a>
                <a href="#" class="nav-item" data-section="huong-dan-trien-khai-jira">4. Hướng Dẫn Triển Khai Jira</a>
                <a href="#" class="nav-item" data-section="bo-sung-itil">5. Bổ Sung ITIL & Quản Trị</a>
            </div>
            
            <div class="nav-section">
                <h3>Tham Khảo</h3>
                <a href="#" class="nav-item" data-section="workflow-diagrams">Workflow Diagrams</a>
                <a href="#" class="nav-item" data-section="jql-queries">JQL Queries</a>
                <a href="#" class="nav-item" data-section="danh-gia-hoan-thien">Đánh Giá Hoàn Thiện</a>
                <a href="#" class="nav-item" data-section="troubleshooting-faq">Troubleshooting & FAQ</a>
                <a href="#" class="nav-item" data-section="bao-cao-tong-hop">Báo Cáo Tổng Hợp</a>
            </div>
        </nav>
        
        <!-- Main Content -->
        <main class="main-content">
            <div id="content-container"></div>
        </main>
    </div>
    
    <script>
        // Embedded content data
        const CONTENT_DATA = {json_str_escaped};
        
        // Simple markdown to HTML converter (basic)
        function markdownToHTML(md) {{
            if (!md) return '';
            
            let html = md;
            
            // Headers
            html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
            html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
            html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
            
            // Bold
            html = html.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
            
            // Italic
            html = html.replace(/\\*(.*?)\\*/g, '<em>$1</em>');
            
            // Code blocks
            html = html.replace(/```([\\s\\S]*?)```/g, '<pre><code>$1</code></pre>');
            html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
            
            // Links
            html = html.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2">$1</a>');
            
            // Lists
            html = html.replace(/^\\* (.*$)/gim, '<li>$1</li>');
            html = html.replace(/^\\d+\\. (.*$)/gim, '<li>$1</li>');
            html = html.replace(/(<li>.*<\\/li>)/s, '<ul>$1</ul>');
            
            // Paragraphs
            html = html.replace(/\\n\\n/g, '</p><p>');
            html = '<p>' + html + '</p>';
            
            // Tables (basic)
            html = html.replace(/\\|(.+)\\|/g, function(match, content) {{
                const cells = content.split('|').map(c => c.trim());
                return '<tr>' + cells.map(c => '<td>' + c + '</td>').join('') + '</tr>';
            }});
            
            // Line breaks
            html = html.replace(/\\n/g, '<br>');
            
            return html;
        }}
        
        // Show content
        function showContent(sectionId) {{
            const container = document.getElementById('content-container');
            
            if (!CONTENT_DATA[sectionId]) {{
                container.innerHTML = '<div class="content-section active"><h1>Không tìm thấy nội dung</h1><p>Section: ' + sectionId + '</p></div>';
                return;
            }}
            
            // Use marked.js if available, otherwise use basic converter
            let html;
            if (typeof marked !== 'undefined') {{
                html = marked.parse(CONTENT_DATA[sectionId]);
            }} else {{
                html = markdownToHTML(CONTENT_DATA[sectionId]);
            }}
            
            container.innerHTML = '<div class="content-section active">' + html + '</div>';
            
            // Scroll to top
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}
        
        // Navigation
        document.addEventListener('DOMContentLoaded', function() {{
            // Show intro by default
            showContent('intro');
            
            // Setup navigation
            document.querySelectorAll('.nav-item').forEach(item => {{
                item.addEventListener('click', function(e) {{
                    e.preventDefault();
                    
                    // Update active state
                    document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
                    this.classList.add('active');
                    
                    // Show content
                    const sectionId = this.getAttribute('data-section');
                    showContent(sectionId);
                }});
            }});
        }});
    </script>
</body>
</html>"""

# Write file
output_file = 'index.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✅ Đã tạo file: {output_file}")
print(f"✅ Kích thước: {len(html_content)/1024:.1f} KB")
print(f"\n🚀 Mở file {output_file} bằng trình duyệt để xem!")
