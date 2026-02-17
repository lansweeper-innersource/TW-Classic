import os
import re
from pathlib import Path

def remove_heading_links(content):
    """
    Remove heading anchor links from markdown content.
    
    Converts:
        [Link Text](#heading-id)
    To:
        Link Text
    
    Returns (modified_content, was_modified, count)
    """
    # Pattern to match markdown links with # anchors
    # Matches: [text](#anchor)
    pattern = r'\[([^\]]+)\]\(#[^\)]+\)'
    
    # Count matches before removing
    matches = re.findall(pattern, content)
    count = len(matches)
    
    # Replace [text](#anchor) with just text
    # The \1 refers to the first capture group (the link text)
    modified_content = re.sub(pattern, r'\1', content)
    
    was_modified = (content != modified_content)
    
    return modified_content, was_modified, count

def clean_file(file_path, dry_run=False):
    """
    Remove heading links from a single file.
    Returns (success, was_modified, count, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove heading links
        modified_content, was_modified, count = remove_heading_links(original_content)
        
        # Only write if changes were made and not in dry-run mode
        if was_modified and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        if was_modified:
            return True, True, count, f"Removed {count} heading link(s)"
        else:
            return True, False, 0, "No heading links found"
    
    except Exception as e:
        return False, False, 0, f"Error: {str(e)}"

def clean_all_articles(directory, dry_run=False):
    """
    Remove heading links from all markdown files.
    
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
    total_links_removed = 0
    
    for md_file in markdown_files:
        success, was_modified, count, message = clean_file(md_file, dry_run)
        
        relative_path = md_file.relative_to(root_path)
        
        if success:
            if was_modified:
                print(f"✓ {relative_path}")
                print(f"  └─ {message}")
                files_modified += 1
                total_links_removed += count
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
        print(f"HEADING LINK CLEANUP COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Files unchanged: {files_unchanged}")
    print(f"  Total heading links removed: {total_links_removed}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")

if __name__ == "__main__":
    # CONFIGURATION
    ARTICLES_DIR = "."  # Directory containing your markdown files
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the cleanup
    print(f"{'='*80}")
    print(f"HEADING LINK REMOVAL SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually clean files\n")
    
    clean_all_articles(ARTICLES_DIR, DRY_RUN)