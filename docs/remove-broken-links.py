import os
import re
from pathlib import Path

def find_asset_images(assets_directory):
    """
    Find all image files in the .document360/assets directory.
    Returns a set of tuples (article_folder, filename).
    """
    assets_path = Path(assets_directory)
    
    if not assets_path.exists():
        print(f"Warning: Assets directory '{assets_directory}' does not exist.")
        return set()
    
    # Common image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'}
    
    existing_images = set()
    
    # Find all files in article_* subdirectories
    for article_folder in assets_path.glob('article_*'):
        if article_folder.is_dir():
            for file in article_folder.iterdir():
                if file.is_file() and file.suffix.lower() in image_extensions:
                    existing_images.add((article_folder.name, file.name))
    
    return existing_images

def remove_broken_image_links(content, existing_images):
    """
    Remove image markdown links where the image file doesn't exist.
    
    Handles patterns like:
    ![alt text](/docs/.document360/assets/article_XXX/image_YYY.jpg)
    
    Returns (modified_content, removed_count, list_of_removed)
    """
    removed_links = []
    
    # Pattern to match image markdown
    # Captures: ![alt](path)
    image_pattern = r'!\[[^\]]*\]\(([^\)]+)\)'
    
    def check_and_remove(match):
        full_match = match.group(0)  # The entire ![...](...)
        image_path = match.group(1)   # Just the path part
        
        # Extract article_XXX and filename from the path
        article_match = re.search(r'(article_\d+)/([^/]+)$', image_path)
        
        if article_match:
            article_folder = article_match.group(1)
            filename = article_match.group(2)
            
            # Check if this image exists
            if (article_folder, filename) not in existing_images:
                # Image doesn't exist - remove it
                removed_links.append({
                    'full_match': full_match,
                    'path': image_path,
                    'article': article_folder,
                    'file': filename
                })
                return ''  # Replace with empty string (remove the image link)
        
        # Keep the image link if it exists or couldn't be parsed
        return full_match
    
    # Process the content
    modified_content = re.sub(image_pattern, check_and_remove, content)
    
    return modified_content, len(removed_links), removed_links

def clean_file(file_path, existing_images, dry_run=False):
    """
    Remove broken image links from a single file.
    Returns (success, was_modified, count, removed_links)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove broken image links
        modified_content, count, removed_links = remove_broken_image_links(original_content, existing_images)
        
        # Only write if changes were made and not in dry-run mode
        if count > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        return True, count > 0, count, removed_links
    
    except Exception as e:
        return False, False, 0, [f"Error: {str(e)}"]

def clean_all_broken_links(markdown_directory, assets_directory, dry_run=False):
    """
    Remove broken image links from all markdown files.
    
    Args:
        markdown_directory: Directory containing markdown files
        assets_directory: Directory containing image assets (.document360/assets)
        dry_run: If True, don't actually modify files, just report what would change
    """
    print(f"{'='*80}")
    print(f"SCANNING FOR BROKEN IMAGE LINKS")
    print(f"{'='*80}\n")
    
    # Find all existing images in assets
    print(f"Scanning assets directory...")
    existing_images = find_asset_images(assets_directory)
    print(f"Found {len(existing_images)} image(s) in assets directory\n")
    
    # Find all markdown files
    markdown_path = Path(markdown_directory)
    markdown_files = list(markdown_path.rglob('*.md')) + list(markdown_path.rglob('*.markdown'))
    
    if not markdown_files:
        print(f"No markdown files found in '{markdown_directory}'")
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
    
    all_removed = []
    
    for md_file in markdown_files:
        success, was_modified, count, removed_links = clean_file(md_file, existing_images, dry_run)
        
        relative_path = md_file.relative_to(markdown_path)
        
        if success:
            if was_modified:
                print(f"✓ {relative_path}")
                print(f"  Removed {count} broken image link(s):")
                for link in removed_links[:5]:  # Show first 5
                    print(f"    • {link['article']}/{link['file']}")
                if len(removed_links) > 5:
                    print(f"    ... and {len(removed_links) - 5} more")
                print()
                
                files_modified += 1
                total_links_removed += count
                
                all_removed.append({
                    'file': str(relative_path),
                    'count': count,
                    'links': removed_links
                })
            else:
                files_unchanged += 1
        else:
            print(f"✗ {relative_path}")
            print(f"  └─ {removed_links[0]}")  # Error message
            print()
            files_with_errors += 1
    
    # Summary
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN COMPLETE - No files were actually modified")
    else:
        print(f"BROKEN LINK CLEANUP COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Files unchanged: {files_unchanged}")
    print(f"  Total broken links removed: {total_links_removed}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")
    
    # Save detailed report
    if all_removed:
        report_file = Path('broken_links_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("BROKEN IMAGE LINKS REMOVAL REPORT\n")
            f.write("="*80 + "\n\n")
            
            if dry_run:
                f.write("DRY RUN MODE - No files were actually modified\n\n")
            
            for item in all_removed:
                f.write(f"File: {item['file']}\n")
                f.write(f"Broken links removed: {item['count']}\n\n")
                for link in item['links']:
                    f.write(f"  Full match: {link['full_match']}\n")
                    f.write(f"  Path: {link['path']}\n")
                    f.write(f"  Missing: {link['article']}/{link['file']}\n")
                    f.write("-"*80 + "\n")
                f.write("\n")
            
            f.write(f"\nSUMMARY\n")
            f.write("="*80 + "\n")
            f.write(f"Files modified: {files_modified}\n")
            f.write(f"Total broken links removed: {total_links_removed}\n")
        
        print(f"\nDetailed report saved to: {report_file.absolute()}")

if __name__ == "__main__":
    # CONFIGURATION
    MARKDOWN_DIR = "."  # Directory containing your markdown files
    ASSETS_DIR = ".document360/assets"  # Path to assets directory
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually remove broken links
    
    # Run the cleanup
    print(f"{'='*80}")
    print(f"BROKEN IMAGE LINK REMOVAL SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually remove broken links\n")
    
    clean_all_broken_links(MARKDOWN_DIR, ASSETS_DIR, DRY_RUN)