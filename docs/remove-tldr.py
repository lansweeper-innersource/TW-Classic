import os
import re
from pathlib import Path

def remove_tldr_sections(content):
    """
    Remove any line or paragraph that contains the TL;DR-Sweepy-Icon image.
    
    Matches patterns like:
    ![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_XXX/image_YYY.jpg) **Description text...**
    
    Returns (modified_content, was_modified, count)
    """
    # Pattern to match lines containing TL;DR-Sweepy-Icon
    # This matches:
    # - The image: ![TL;DR-Sweepy-Icon...](...)
    # - Any text following it on the same line (including bold text)
    # - The entire line including newlines
    
    pattern = r'^.*?!\[TL;DR-Sweepy-Icon[^\]]*\].*?$\n?'
    
    # Count matches before removing
    matches = re.findall(pattern, content, re.MULTILINE)
    count = len(matches)
    
    # Remove all matches
    modified_content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    was_modified = (content != modified_content)
    
    return modified_content, was_modified, count

def clean_file(file_path, dry_run=False):
    """
    Remove TL;DR sections from a single file.
    Returns (success, was_modified, count, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove TL;DR sections
        modified_content, was_modified, count = remove_tldr_sections(original_content)
        
        # Only write if changes were made and not in dry-run mode
        if was_modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        if was_modified:
            return True, True, count, f"Removed {count} TL;DR section(s)"
        else:
            return True, False, 0, "No TL;DR sections found"
    
    except Exception as e:
        return False, False, 0, f"Error: {str(e)}"

def clean_all_articles(directory, dry_run=False):
    """
    Remove TL;DR sections from all markdown files.
    
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
    total_sections_removed = 0
    
    for md_file in markdown_files:
        success, was_modified, count, message = clean_file(md_file, dry_run)
        
        relative_path = md_file.relative_to(root_path)
        
        if success:
            if was_modified:
                print(f"✓ {relative_path}")
                print(f"  └─ {message}")
                print()
                files_modified += 1
                total_sections_removed += count
            else:
                # Uncomment to see files with no changes
                # print(f"  {relative_path} - {message}")
                files_unchanged += 1
        else:
            print(f"✗ {relative_path}")
            print(f"  └─ {message}")
            print()
            files_with_errors += 1
    
    # Summary
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN COMPLETE - No files were actually modified")
    else:
        print(f"TL;DR SECTION CLEANUP COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Files unchanged: {files_unchanged}")
    print(f"  Total TL;DR sections removed: {total_sections_removed}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")

if __name__ == "__main__":
    # CONFIGURATION
    ARTICLES_DIR = "."  # Directory containing your markdown files
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the cleanup
    print(f"{'='*80}")
    print(f"TL;DR SECTION REMOVAL SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually clean files\n")
    
    clean_all_articles(ARTICLES_DIR, DRY_RUN)