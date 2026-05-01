import os
import re

# Configuration
INPUT_FOLDER = '/Users/jatin.s/Downloads/dictionary'
OUTPUT_PREFIX = 'sap_export'
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB in bytes

def clean_html_tags(text):
    """Removes HTML tags and cleans up entities."""
    text = re.sub(r'<[^<]+?>', '', text)
    text = text.replace('&nbsp;', ' ').strip()
    return text

def parse_html_to_text(html_content):
    """Extracts tables and formats them into aligned text."""
    lines = []
    
    # 1. Extract Title and Description
    titles = re.findall(r'<(h[23])>(.*?)</\1>', html_content, re.DOTALL)
    for _, content in titles:
        lines.append(clean_html_tags(content))
    lines.append("=" * 100)
    
    # 2. Extract Table Sections
    table_sections = re.findall(r'<table class="innerTable">(.*?)</table>', html_content, re.DOTALL)
    
    for section in table_sections:
        # Get Headers
        headers = [clean_html_tags(h) for h in re.findall(r'<th>(.*?)</th>', section, re.DOTALL)]
        
        # Get Rows
        rows_raw = re.findall(r'<tr class="cell">(.*?)</tr>', section, re.DOTALL)
        rows = []
        for r in rows_raw:
            cells = re.findall(r'<td>(.*?)</td>', r, re.DOTALL)
            rows.append([clean_html_tags(c) for c in cells])
            
        if not headers or not rows:
            continue
            
        # Calculate column widths for alignment
        widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(widths):
                    widths[i] = max(widths[i], len(cell))
        
        # Build formatted table string
        head_str = " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
        sep_str = "-+-".join("-" * widths[i] for i in range(len(headers)))
        lines.append(head_str)
        lines.append(sep_str)
        
        for row in rows:
            row_str = " | ".join(row[i].ljust(widths[i]) if i < len(row) else "".ljust(widths[i]) for i in range(len(widths)))
            lines.append(row_str)
            
        lines.append("\n" + "=" * 100 + "\n")
        
    return "\n".join(lines)

def process_files():
    file_count = 1
    current_out_filename = f"{OUTPUT_PREFIX}_{file_count}.txt"
    current_out_file = open(current_out_filename, 'w', encoding='utf-8')
    current_size = 0

    # Get list of all HTML files
    html_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.html')]
    print(f"Starting processing of {len(html_files)} files...")

    for filename in html_files:
        file_path = os.path.join(INPUT_FOLDER, filename)
        
        try:
            with open(file_path, 'r', encoding='iso-8859-1') as f:
                html_data = f.read()
            
            # Convert HTML to formatted text
            formatted_block = parse_html_to_text(html_data) + "\n\n"
            block_bytes = formatted_block.encode('utf-8')
            
            # Check if adding this block exceeds 5MB
            if current_size + len(block_bytes) > MAX_FILE_SIZE:
                current_out_file.close()
                file_count += 1
                current_out_filename = f"{OUTPUT_PREFIX}_{file_count}.txt"
                current_out_file = open(current_out_filename, 'w', encoding='utf-8')
                current_size = 0
                print(f"Created {current_out_filename}")

            current_out_file.write(formatted_block)
            current_size += len(block_bytes)

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    current_out_file.close()
    print("Processing complete.")

if __name__ == "__main__":
    process_files()
