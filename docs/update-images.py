import os
import re
from pathlib import Path

def update_image_paths(content):
    """
    Update image paths from:
        (images\article_XXX\image_YYY.jpg "title")
    to:
        (/docs/.document360/assets/article_XXX/image_YYY.jpg)
    
    Also handles:
    - Forward slashes (images/article_XXX/...)
    - Different image extensions (jpg, png, gif, etc.)
    - Image paths with or without titles
    
    Returns (modified_content, replacement_count, list_of_replacements)
    """
    replacements_made = []
    
    # Pattern to match image paths
    # Matches: (images\article_XXX\image_YYY.ext "optional title")
    # or: (images/article_XXX/image_YYY.ext "optional title")
    pattern = r'\(images[\\/](article_\d+)[\\/]([^\)\"]+?)(?:\s+"[^"]*")?\)'
    
    def replacement_function(match):
        article_folder = match.group(1)  # e.g., article_130
        image_filename = match.group(2)  # e.g., image_002.jpg
        
        # Create new path with /assets/
        new_path = f"(/docs/.document360/assets/{article_folder}/{image_filename})"
        
        # Track replacement
        old_path = match.group(0)
        if old_path not in [r['old'] for r in replacements_made]:
            replacements_made.append({
                'old': old_path,
                'new': new_path
            })
        
        return new_path
    
    # Perform replacement
    modified_content = re.sub(pattern, replacement_function, content)
    
    replacement_count = len(re.findall(pattern, content))
    
    return modified_content, replacement_count, replacements_made

def update_file_images(file_path, dry_run=False):
    """
    Update image paths in a single file.
    Returns (success, replacements_count, replacements_list)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Update image paths
        modified_content, count, replacements = update_image_paths(original_content)
        
        # Only write if changes were made and not in dry-run mode
        if count > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        return True, count, replacements
    
    except Exception as e:
        return False, 0, [{'old': 'Error', 'new': str(e)}]

def update_all_images(directory, dry_run=False):
    """
    Update image paths in all markdown files.
    
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
    total_replacements = 0
    files_with_errors = 0
    
    all_replacements = []
    
    for md_file in markdown_files:
        success, count, replacements = update_file_images(md_file, dry_run)
        
        relative_path = md_file.relative_to(root_path)
        
        if success:
            if count > 0:
                print(f"✓ {relative_path}")
                print(f"  Updated {count} image path(s):")
                for rep in replacements[:5]:  # Show first 5 to avoid clutter
                    print(f"    • {rep['old']}")
                    print(f"      → {rep['new']}")
                if len(replacements) > 5:
                    print(f"    ... and {len(replacements) - 5} more")
                print()
                
                files_modified += 1
                total_replacements += count
                
                all_replacements.append({
                    'file': str(relative_path),
                    'count': count,
                    'replacements': replacements
                })
            else:
                # Uncomment to see files with no images
                # print(f"  {relative_path} - No image paths to update")
                pass
        else:
            print(f"✗ {relative_path}")
            print(f"  {replacements[0]['new']}")  # Error message
            print()
            files_with_errors += 1
    
    # Summary
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN COMPLETE - No files were actually modified")
    else:
        print(f"IMAGE PATH UPDATE COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Total image paths updated: {total_replacements}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")
    
    # Save detailed report
    if all_replacements:
        report_file = Path('image_update_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("IMAGE PATH UPDATE REPORT\n")
            f.write("="*80 + "\n\n")
            
            if dry_run:
                f.write("DRY RUN MODE - No files were actually modified\n\n")
            
            for item in all_replacements:
                f.write(f"File: {item['file']}\n")
                f.write(f"Total updates: {item['count']}\n\n")
                for rep in item['replacements']:
                    f.write(f"  Old: {rep['old']}\n")
                    f.write(f"  New: {rep['new']}\n")
                    f.write("-"*80 + "\n")
                f.write("\n")
            
            f.write(f"\nSUMMARY\n")
            f.write("="*80 + "\n")
            f.write(f"Files modified: {files_modified}\n")
            f.write(f"Total image paths updated: {total_replacements}\n")
        
        print(f"\nDetailed report saved to: {report_file.absolute()}")

if __name__ == "__main__":
    # CONFIGURATION
    ARTICLES_DIR = "."  # Directory containing your markdown files
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the image path update
    print(f"{'='*80}")
    print(f"IMAGE PATH UPDATE SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually update files\n")
    
    update_all_images(ARTICLES_DIR, DRY_RUN)