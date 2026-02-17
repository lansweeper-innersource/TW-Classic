import os
import re
import csv
from pathlib import Path

def load_url_mappings_by_id(csv_file):
    """
    Load the URL mappings from the CSV file.
    Returns a dictionary of {article_id: new_url}
    where article_id is extracted from the old URL (e.g., 64446)
    """
    mappings = {}
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                old_url = row['old_url']
                new_url = row['new_url']
                
                # Extract the article ID from the old URL (the number after /ta-p/)
                match = re.search(r'/ta-p/(\d+)', old_url)
                if match:
                    article_id = match.group(1)
                    
                    # Ensure new URL has leading slash
                    if not new_url.startswith('/'):
                        new_url = '/' + new_url
                    
                    mappings[article_id] = new_url
        
        print(f"Loaded {len(mappings)} URL mappings from {csv_file}\n")
        return mappings
    
    except FileNotFoundError:
        print(f"Error: Mapping file '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading mappings: {str(e)}")
        return None

def replace_urls_by_id(content, url_mappings):
    """
    Replace community URLs with new URLs based on article ID matching.
    Matches URLs like: https://community.lansweeper.com/t5/.../ta-p/64446
    Replaces entire URL with the new mapped URL.
    
    Returns (modified_content, replacement_count, list_of_replacements)
    """
    replacements_made = []
    
    # Pattern to match Lansweeper community URLs
    # Captures the full URL and the article ID
    pattern = r'https://community\.lansweeper\.com/t5/[^\s\|\)]+/ta-p/(\d+)'
    
    def replacement_function(match):
        full_url = match.group(0)  # The entire URL
        article_id = match.group(1)  # The ID number (e.g., 64446)
        
        # Look up the new URL by article ID
        if article_id in url_mappings:
            new_url = url_mappings[article_id]
            
            # Track replacement
            replacements_made.append({
                'old': full_url,
                'new': new_url,
                'id': article_id
            })
            
            return new_url
        else:
            # If no mapping found, return original URL unchanged
            return full_url
    
    # Perform replacement
    modified_content = re.sub(pattern, replacement_function, content)
    
    replacement_count = len(replacements_made)
    
    return modified_content, replacement_count, replacements_made

def update_urls_in_file(file_path, url_mappings, dry_run=False):
    """
    Update URLs in a single file based on article ID matching.
    Returns (success, replacements_count, replacements_list)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Replace URLs
        modified_content, count, replacements = replace_urls_by_id(original_content, url_mappings)
        
        # Only write if changes were made and not in dry-run mode
        if count > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        return True, count, replacements
    
    except Exception as e:
        return False, 0, [f"Error: {str(e)}"]

def update_all_urls(directory, mapping_file, dry_run=False):
    """
    Update URLs in all markdown files based on article ID matching.
    
    Args:
        directory: Root directory containing markdown files
        mapping_file: Path to the CSV mapping file
        dry_run: If True, don't actually modify files, just report what would change
    """
    # Load mappings
    url_mappings = load_url_mappings_by_id(mapping_file)
    
    if not url_mappings:
        return
    
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
        success, count, replacements = update_urls_in_file(md_file, url_mappings, dry_run)
        
        relative_path = md_file.relative_to(root_path)
        
        if success:
            if count > 0:
                print(f"✓ {relative_path}")
                print(f"  Replaced {count} URL(s):")
                for rep in replacements[:5]:  # Show first 5 to avoid clutter
                    print(f"    • ID {rep['id']}: {rep['old'][:60]}...")
                    print(f"      → {rep['new']}")
                if len(replacements) > 5:
                    print(f"    ... and {len(replacements) - 5} more")
                print()
                
                files_modified += 1
                total_replacements += count
                
                all_replacements.append({
                    'file': str(relative_path),
                    'replacements': replacements
                })
            else:
                # Uncomment to see files with no changes
                # print(f"  {relative_path} - No URLs to replace")
                pass
        else:
            print(f"✗ {relative_path}")
            print(f"  {replacements[0]}")  # Error message
            print()
            files_with_errors += 1
    
    # Summary
    print(f"{'='*80}")
    if dry_run:
        print(f"DRY RUN COMPLETE - No files were actually modified")
    else:
        print(f"URL UPDATE COMPLETE")
    print(f"{'='*80}")
    print(f"  Files processed: {len(markdown_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Total URL replacements: {total_replacements}")
    print(f"  Errors: {files_with_errors}")
    print(f"{'='*80}")
    
    # Save detailed report
    if all_replacements:
        report_file = Path('url_id_replacement_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("URL REPLACEMENT BY ID REPORT\n")
            f.write("="*80 + "\n\n")
            
            if dry_run:
                f.write("DRY RUN MODE - No files were actually modified\n\n")
            
            for item in all_replacements:
                f.write(f"File: {item['file']}\n")
                for rep in item['replacements']:
                    f.write(f"  ID: {rep['id']}\n")
                    f.write(f"  Old: {rep['old']}\n")
                    f.write(f"  New: {rep['new']}\n")
                    f.write("-"*80 + "\n")
                f.write("\n")
            
            f.write(f"\nSUMMARY\n")
            f.write("="*80 + "\n")
            f.write(f"Files modified: {files_modified}\n")
            f.write(f"Total replacements: {total_replacements}\n")
        
        print(f"\nDetailed report saved to: {report_file.absolute()}")

if __name__ == "__main__":
    # CONFIGURATION
    ARTICLES_DIR = "."  # Directory containing your markdown files
    MAPPING_FILE = "url_mapping.csv"  # The CSV file with old/new URL mappings
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the URL replacement
    print(f"{'='*80}")
    print(f"URL REPLACEMENT BY ID SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually update files\n")
    
    update_all_urls(ARTICLES_DIR, MAPPING_FILE, DRY_RUN)