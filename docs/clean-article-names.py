import os
import re
from pathlib import Path

def extract_h1_title(content):
    """
    Extract the first H1 heading from markdown content.
    Returns the title without the # symbol, or None if not found.
    """
    # Match # Title (with optional leading/trailing whitespace)
    pattern = r'^#\s+(.+?)$'
    match = re.search(pattern, content, re.MULTILINE)
    
    if match:
        return match.group(1).strip()
    return None

def create_safe_filename(title):
    """
    Convert a title string into a safe filename.
    Removes special characters and converts spaces to underscores.
    """
    # Remove or replace unsafe characters
    safe_name = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace multiple spaces with single space
    safe_name = re.sub(r'\s+', ' ', safe_name)
    # Trim and limit length
    safe_name = safe_name.strip()[:100]  # Limit to 100 chars
    
    return safe_name

def comment_out_header_and_source(content):
    """
    Comment out the first H1 heading and any source link that follows it.
    Returns the modified content.
    """
    lines = content.split('\n')
    modified_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is the first H1 heading
        if re.match(r'^#\s+.+', line):
            # Comment out the H1
            modified_lines.append(f'<!-- {line} -->')
            i += 1
            
            # Look ahead for a source link pattern
            # Check the next few lines for source information
            source_block = []
            while i < len(lines):
                next_line = lines[i]
                
                # Check if line contains "Source:" or a community URL
                if re.search(r'\*\*Source:\*\*|https://community\.lansweeper\.com', next_line):
                    source_block.append(next_line)
                    i += 1
                # If we hit an empty line after collecting source lines, include it
                elif source_block and next_line.strip() == '':
                    source_block.append(next_line)
                    i += 1
                    break
                # If we found source content and now hit non-source content, stop
                elif source_block:
                    break
                # If it's an empty line before source content, skip it
                elif next_line.strip() == '':
                    i += 1
                    continue
                else:
                    break
            
            # Comment out the source block if found
            if source_block:
                modified_lines.append('<!--')
                modified_lines.extend(source_block)
                # Remove trailing empty line from source block if exists
                if modified_lines[-1].strip() == '':
                    modified_lines.pop()
                modified_lines.append('-->')
            
            # Found and processed H1, done with this section
            break
        else:
            modified_lines.append(line)
            i += 1
    
    # Add remaining lines
    while i < len(lines):
        modified_lines.append(lines[i])
        i += 1
    
    return '\n'.join(modified_lines)

def process_markdown_file(file_path):
    """
    Process a single markdown file:
    1. Extract H1 title
    2. Comment out H1 and source
    3. Rename file based on title
    Returns (success, old_name, new_name, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title = extract_h1_title(content)
        
        if not title:
            return False, file_path.name, None, "No H1 heading found"
        
        # Comment out H1 and source
        modified_content = comment_out_header_and_source(content)
        
        # Create new filename
        safe_title = create_safe_filename(title)
        new_filename = f"{safe_title}.md"
        new_file_path = file_path.parent / new_filename
        
        # Check if new filename already exists and is different from current
        if new_file_path.exists() and new_file_path != file_path:
            return False, file_path.name, new_filename, "Target filename already exists"
        
        # Write modified content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        # Rename file if needed
        if file_path.name != new_filename:
            file_path.rename(new_file_path)
            return True, file_path.name, new_filename, "Renamed and modified"
        else:
            return True, file_path.name, new_filename, "Modified (name unchanged)"
        
    except Exception as e:
        return False, file_path.name, None, f"Error: {str(e)}"

def clean_article_names(directory, recursive=True):
    """
    Process all markdown files in the directory and subdirectories.
    
    Args:
        directory: Root directory to process
        recursive: If True, process subdirectories as well
    """
    root_path = Path(directory)
    
    if not root_path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Find all markdown files
    if recursive:
        markdown_files = list(root_path.rglob('*.md')) + list(root_path.rglob('*.markdown'))
    else:
        markdown_files = list(root_path.glob('*.md')) + list(root_path.glob('*.markdown'))
    
    if not markdown_files:
        print(f"No markdown files found in '{directory}'")
        return
    
    print(f"Found {len(markdown_files)} markdown file(s) to process.\n")
    print(f"{'='*80}")
    
    success_count = 0
    error_count = 0
    
    for md_file in markdown_files:
        success, old_name, new_name, message = process_markdown_file(md_file)
        
        relative_dir = md_file.parent.relative_to(root_path) if md_file.parent != root_path else "."
        
        if success:
            if "unchanged" in message:
                print(f"✓ [{relative_dir}] {old_name}")
                print(f"  └─ Content modified (H1 & source commented out)")
            else:
                print(f"✓ [{relative_dir}] {old_name}")
                print(f"  └─ Renamed to: {new_name}")
            success_count += 1
        else:
            print(f"✗ [{relative_dir}] {old_name}")
            print(f"  └─ {message}")
            error_count += 1
        print()
    
    print(f"{'='*80}")
    print(f"Processing complete!")
    print(f"  Successfully processed: {success_count}")
    print(f"  Errors/Skipped: {error_count}")
    print(f"{'='*80}")

if __name__ == "__main__":
    # CONFIGURATION
    # Set this to the directory containing your organized markdown files
    ARTICLES_DIR = "."  # Current directory, or specify path like "C:/Users/YourName/Articles"
    
    # Set to True to process subdirectories (your organized folders), False for current dir only
    RECURSIVE = True
    
    # Run the cleanup
    clean_article_names(ARTICLES_DIR, RECURSIVE)