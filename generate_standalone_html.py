#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để tạo file HTML standalone với tất cả nội dung được embed trực tiếp
"""

import json
import html

# Read all markdown files
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

# Convert to JSON string and escape for JavaScript
json_str = json.dumps(content_map, ensure_ascii=False, indent=2)
# Escape for embedding in HTML/JavaScript
json_str_escaped = json_str.replace('</script>', '<\\/script>')

print(f"\nĐã load {len(content_map)} files")
print(f"Tổng kích thước: {len(json_str)} characters")

# Read the HTML template
print("\nĐang đọc template HTML...")
with open('DOCUMENTATION.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

# Replace the script tag that loads content_data.js with embedded data
embedded_script = f"""
    <script>
        // Embedded content data - Tất cả nội dung đã được embed trực tiếp
        const CONTENT_DATA = {json_str_escaped};
        console.log('✓ CONTENT_DATA loaded with', Object.keys(CONTENT_DATA).length, 'sections');
    </script>
"""

# Find and replace the content_data.js script tag
if '<script src="content_data.js"></script>' in html_template:
    html_template = html_template.replace(
        '<script src="content_data.js"></script>',
        embedded_script
    )
    print("✓ Đã thay thế script tag")
else:
    # If not found, insert before the main script
    html_template = html_template.replace(
        '    <script>\n        // Initialize Mermaid',
        embedded_script + '    <script>\n        // Initialize Mermaid'
    )
    print("✓ Đã thêm embedded script")

# Update initialization to use embedded data directly
import re

# Update contentData initialization
html_template = re.sub(
    r'let contentData = typeof CONTENT_DATA !== \'undefined\' \? CONTENT_DATA : \{\};',
    'let contentData = typeof CONTENT_DATA !== \'undefined\' ? CONTENT_DATA : {};',
    html_template
)

# Update loadContentData function to use embedded data directly
new_load_function = """        // Load content data - Use embedded CONTENT_DATA directly
        async function loadContentData() {
            // CONTENT_DATA is already loaded from embedded script above
            if (typeof CONTENT_DATA !== 'undefined' && Object.keys(CONTENT_DATA).length > 0) {
                contentData = CONTENT_DATA;
                console.log('✓ Using embedded CONTENT_DATA with', Object.keys(CONTENT_DATA).length, 'sections');
                return true;
            }
            
            // Fallback: Try to load from JSON file (should not be needed for standalone)
            try {
                const response = await fetch('content_data.json');
                if (response.ok) {
                    contentData = await response.json();
                    console.log('✓ Loaded content from content_data.json (fallback)');
                    return true;
                }
            } catch (error) {
                console.log('⚠ Could not load content_data.json (this is normal for standalone file)');
            }
            
            console.warn('⚠ No content data available');
            return false;
        }"""

# Find and replace the loadContentData function (more robust pattern)
pattern = r'async function loadContentData\(\)\s*\{[^}]*\}'
html_template = re.sub(pattern, new_load_function, html_template, flags=re.DOTALL)
print("✓ Đã cập nhật hàm loadContentData để sử dụng embedded data")

# Update initialization code - more specific replacement
init_old = """        // Initialize: Load content data and intro
        (async () => {
            // Wait a bit for content_data.js to load if it exists
            await new Promise(resolve => setTimeout(resolve, 100));
            await loadContentData();
            
            // Load intro content
            if (contentData && Object.keys(contentData).length > 0) {
                loadMarkdown('intro');
            } else {
                console.error('No content data available. Please ensure content_data.js exists.');
                document.getElementById('intro').innerHTML = `
                    <div class="loading">
                        <h2>⚠ Lỗi: Không thể tải dữ liệu</h2>
                        <p>File <code>content_data.js</code> không được tìm thấy hoặc không thể load.</p>
                        <p>Vui lòng:</p>
                        <ol>
                            <li>Đảm bảo file <code>content_data.js</code> nằm cùng thư mục với file HTML này</li>
                            <li>Hoặc sử dụng local server để chạy file HTML</li>
                            <li>Xem hướng dẫn trong file <code>HUONG_DAN_SU_DUNG_HTML.md</code></li>
                        </ol>
                    </div>
                `;
            }
        })();"""

init_new = """        // Initialize: Load content data and intro
        (async () => {
            // CONTENT_DATA should already be available from embedded script
            // But wait a tiny bit to ensure it's loaded
            await new Promise(resolve => setTimeout(resolve, 50));
            
            // Load content data (will use embedded CONTENT_DATA)
            await loadContentData();
            
            // Ensure contentData is set from embedded CONTENT_DATA
            if (typeof CONTENT_DATA !== 'undefined' && Object.keys(CONTENT_DATA).length > 0) {
                contentData = CONTENT_DATA;
                console.log('✓ CONTENT_DATA initialized with', Object.keys(CONTENT_DATA).length, 'sections');
            }
            
            // Load intro content
            if (contentData && Object.keys(contentData).length > 0) {
                console.log('✓ Loading intro content...');
                loadMarkdown('intro');
            } else {
                console.error('✗ No content data available');
                document.getElementById('intro').innerHTML = `
                    <div class="loading">
                        <h2>⚠ Lỗi: Không thể tải dữ liệu</h2>
                        <p>CONTENT_DATA không được tìm thấy trong file HTML.</p>
                        <p>Vui lòng tạo lại file bằng cách chạy:</p>
                        <pre><code>python3 generate_standalone_html.py</code></pre>
                        <p>Hoặc xem hướng dẫn trong file <code>HUONG_DAN_SU_DUNG_HTML.md</code></p>
                    </div>
                `;
            }
        })();"""

if init_old in html_template:
    html_template = html_template.replace(init_old, init_new)
    print("✓ Đã cập nhật phần khởi tạo")
else:
    # Try pattern matching as fallback
    init_pattern = r'// Initialize: Load content data and intro.*?\(\)\);'
    if re.search(init_pattern, html_template, flags=re.DOTALL):
        html_template = re.sub(init_pattern, init_new, html_template, flags=re.DOTALL)
        print("✓ Đã cập nhật phần khởi tạo (pattern match)")
    else:
        print("⚠ Không tìm thấy phần khởi tạo để cập nhật")

# Write standalone HTML file
output_file = 'DOCUMENTATION_STANDALONE.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"\n✓ Đã tạo file: {output_file}")
print(f"✓ Kích thước file: {len(html_template)} characters")
print(f"\nFile HTML standalone đã sẵn sàng! Mở file {output_file} bằng trình duyệt web.")
