import os
import re
import csv
from pathlib import Path

def load_url_mappings(csv_file):
    """
    Load the URL mappings from the CSV file.
    Returns a dictionary of {old_url: new_url}
    """
    mappings = {}
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure new URL has leading slash
                new_url = row['new_url']
                if not new_url.startswith('/'):
                    new_url = '/' + new_url
                mappings[row['old_url']] = new_url
        
        print(f"Loaded {len(mappings)} URL mappings from {csv_file}\n")
        return mappings
    
    except FileNotFoundError:
        print(f"Error: Mapping file '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading mappings: {str(e)}")
        return None

def find_source_section_end(content):
    """
    Find where the source section ends in the document.
    Returns the character position after which URLs should be replaced.
    """
    # Look for the commented source block
    comment_pattern = r'<!--[\s\S]*?-->'
    match = re.search(comment_pattern, content)
    
    if match:
        return match.end()
    
    # If no comment block, look for Source: pattern and skip a few lines
    source_pattern = r'\*\*Source:\*\*.*?(?:\n|$)'
    match = re.search(source_pattern, content)
    
    if match:
        # Return position after the source line plus some buffer
        return match.end() + 100  # Add buffer to skip any related formatting
    
    # If nothing found, start replacing from character 0 (shouldn't happen with your files)
    return 0

def replace_urls_in_content(content, url_mappings):
    """
    Replace old URLs with new URLs in the content, but skip the source section.
    Returns (modified_content, replacement_count, list_of_replacements)
    """
    # Find where we should start replacing URLs
    source_end = find_source_section_end(content)
    
    # Split content into protected (source) and replaceable sections
    protected_section = content[:source_end]
    replaceable_section = content[source_end:]
    
    replacements_made = []
    total_replacements = 0
    
    # Replace each old URL with new URL in the replaceable section only
    for old_url, new_url in url_mappings.items():
        # Escape special regex characters in the URL
        escaped_old_url = re.escape(old_url)
        
        # Find all occurrences in the replaceable section
        matches = list(re.finditer(escaped_old_url, replaceable_section))
        
        if matches:
            # Replace all occurrences
            replaceable_section = re.sub(escaped_old_url, new_url, replaceable_section)
            
            replacements_made.append({
                'old_url': old_url,
                'new_url': new_url,
                'count': len(matches)
            })
            total_replacements += len(matches)
    
    # Reconstruct the content
    modified_content = protected_section + replaceable_section
    
    return modified_content, total_replacements, replacements_made

def update_urls_in_file(file_path, url_mappings, dry_run=False):
    """
    Update URLs in a single file.
    Returns (success, replacements_count, replacements_list)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Replace URLs
        modified_content, count, replacements = replace_urls_in_content(original_content, url_mappings)
        
        # Only write if changes were made and not in dry-run mode
        if count > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        return True, count, replacements
    
    except Exception as e:
        return False, 0, [f"Error: {str(e)}"]

def update_all_articles(directory, mapping_file, dry_run=False):
    """
    Update URLs in all markdown files based on the mapping file.
    
    Args:
        directory: Root directory containing markdown files
        mapping_file: Path to the CSV mapping file
        dry_run: If True, don't actually modify files, just report what would change
    """
    # Load mappings
    url_mappings = load_url_mappings(mapping_file)
    
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
                for rep in replacements:
                    print(f"    • {rep['old_url']} → {rep['new_url']} ({rep['count']}x)")
                print()
                
                files_modified += 1
                total_replacements += count
                
                all_replacements.append({
                    'file': str(relative_path),
                    'replacements': replacements
                })
            else:
                # Uncomment the line below if you want to see files with no changes
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
        report_file = Path('url_replacement_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("URL REPLACEMENT REPORT\n")
            f.write("="*80 + "\n\n")
            
            if dry_run:
                f.write("DRY RUN MODE - No files were actually modified\n\n")
            
            for item in all_replacements:
                f.write(f"File: {item['file']}\n")
                for rep in item['replacements']:
                    f.write(f"  Old: {rep['old_url']}\n")
                    f.write(f"  New: {rep['new_url']}\n")
                    f.write(f"  Count: {rep['count']}\n")
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
    MAPPING_FILE = "url_mapping.csv"  # The CSV file generated by the previous script
    
    # Set to True to preview changes without modifying files
    DRY_RUN = False  # Change to False to actually update the files
    
    # Run the URL replacement
    print(f"{'='*80}")
    print(f"URL REPLACEMENT SCRIPT")
    print(f"{'='*80}\n")
    
    if DRY_RUN:
        print("⚠️  Running in DRY RUN mode - files will NOT be modified")
        print("Set DRY_RUN = False to actually update files\n")
    
    update_all_articles(ARTICLES_DIR, MAPPING_FILE, DRY_RUN)