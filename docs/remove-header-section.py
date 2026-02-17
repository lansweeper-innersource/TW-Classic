import os
import re
from pathlib import Path

def remove_header_section(content):
    """
    Remove the header section containing:
    - Commented source link
    - Horizontal rule (---)
    - Optional: Image/icon line with description
    - Horizontal rule (---)
    
    Handles both:
    1. With TL;DR image/description
    2. Without TL;DR (just comment and horizontal rule)
    
    Returns (modified_content, was_modified)
    """
    # Pattern 1: With TL;DR content (image and description)
    pattern_with_tldr = r'''
        ^\s*                                    # Start of content, optional whitespace
        <!--\s*                                 # Opening comment
        \*\*Source:\*\*\s*                      # Source label
        \[.*?\]\(.*?\)                          # Markdown link [text](url)
        \s*-->\s*                               # Closing comment
        \n*                                     # Optional newlines
        ---\s*                                  # First horizontal rule
        \n*                                     # Optional newlines
        !\[.*?\]\(.*?\)                         # Image: ![alt](path)
        .*?                                     # Any characters (title, etc.)
        \*\*.*?\*\*                             # Bold text description
        \s*\n*                                  # Optional whitespace/newlines
        ---\s*                                  # Second horizontal rule
        \n*                                     # Optional newlines after
    '''
    
    # Pattern 2: Without TL;DR content (just comment and horizontal rule)
    pattern_without_tldr = r'''
        ^\s*                                    # Start of content, optional whitespace
        <!--\s*                                 # Opening comment
        \*\*Source:\*\*\s*                      # Source label
        \[.*?\]\(.*?\)                          # Markdown link [text](url)
        \s*-->\s*                               # Closing comment
        \n*                                     # Optional newlines
        ---\s*                                  # Horizontal rule
        \n*                                     # Optional newlines after
    '''
    
    # Try pattern with TL;DR first
    modified_content = re.sub(pattern_with_tldr, '', content, count=1, flags=re.VERBOSE | re.MULTILINE)
    was_modified = (content != modified_content)
    
    # If that didn't work, try pattern without TL;DR
    if not was_modified:
        modified_content = re.sub(pattern_without_tldr, '', content, count=1, flags=re.VERBOSE | re.MULTILINE)
        was_modified = (content != modified_content)
    
    # If verbose patterns didn't work, try simpler approaches
    if not was_modified:
        # Alternative pattern 1 - with TL;DR
        simple_pattern_tldr = r'<!--[\s\S]*?\*\*Source:\*\*[\s\S]*?-->\s*\n---\s*\n.*?!\[.*?\].*?\*\*.*?\*\*.*?\n---\s*\n+'
        modified_content = re.sub(simple_pattern_tldr, '', content, count=1)
        was_modified = (content != modified_content)
    
    if not was_modified:
        # Alternative pattern 2 - without TL;DR
        simple_pattern_no_tldr = r'<!--[\s\S]*?\*\*Source:\*\*[\s\S]*?-->\s*\n---\s*\n+'
        modified_content = re.sub(simple_pattern_no_tldr, '', content, count=1)
        was_modified = (content != modified_content)
    
    return modified_content, was_modified

def clean_file(file_path, dry_run=False):
    """
    Remove the header section from a single file.
    Returns (success, was_modified, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove the header section
        modified_content, was_modified = remove_header_section(original_content)
        
        # Only write if changes were made and not in dry-run mode
        if was_modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        if was_modified:
            return True, True, "Header section removed"
        else:
            return True, False, "No header section found"
    
    except Exception as e:
        return False, False, f"Error: {str(e)}"

def clean_all_articles(directory, dry_run=False):
    """
    Remove header sections from all markdown files.
    
    Args:
        directory: Root directory containing markdown files
        dry_run: If True, don't actually modify files, just report what would change
    """
    root_path = Path(directory)
    
    if not root_path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Find all markdown files
    markdown_files = list(root_path.rglob('*.md')) + list(root_path.rglob('*.markdown'))
    
    if not markdown_files:
        print(f"No markdown files found in '{directory}'")
        return
    
    if dry_run:
        print(f"{'='*80}")
        print(f"DRY RUN MODE - No files will be modified")
        print(f"{'='*80}\n")
    
    print(f"Processing {len(markdown_files)} markdown file(s)...\n")
    print(f"{'='*80}\n")
    
    files_modified = 0
    files_unchanged = 0
    files_with_errors = 0
    
    for md_file in markdown_files:
        success, was_modified, message = clean_file(md_file, dry_run)
        
        relative_path = md_file.relative_to(root_path)
        
        if success:
            if was_modified:
                print(f"✓ {relative_path}")
                print(f"  └─ {message}")
                files_modified += 1
            else:
                # Uncomment to see files with no changes
                # print(f"  {relative_path} - {message}")
                files_unchanged += 1
        else:
            print(f"✗ {relative_path}")
            print(f"  └─ {message}")
            files_with_errors += 1
        
        # Add spacing after modified files for readability
        if was_modified:
            print()
    
    # Summary
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN COMPLETE - No files were actually modified")
    else:
        print(f"HEADER CLEANUP COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Files unchanged: {files_unchanged}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")

if __name__ == "__main__":
    # CONFIGURATION
    ARTICLES_DIR = "."  # Directory containing your markdown files
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the cleanup
    print(f"{'='*80}")
    print(f"HEADER SECTION REMOVAL SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually clean files\n")
    
    clean_all_articles(ARTICLES_DIR, DRY_RUN)