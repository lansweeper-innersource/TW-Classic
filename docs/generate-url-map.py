import os
import re
import csv
from pathlib import Path

def extract_source_url(content):
    """
    Extract the source URL from the markdown content.
    Looks for patterns like:
    **Source:** https://community.lansweeper.com/...
    or inside HTML comments
    """
    # Try to find URL in commented source first
    comment_pattern = r'<!--[\s\S]*?\*\*Source:\*\*\s*(?:\[)?(https://community\.lansweeper\.com/[^\s\]]+)'
    match = re.search(comment_pattern, content)
    
    if match:
        return match.group(1)
    
    # Try to find URL in non-commented source
    source_pattern = r'\*\*Source:\*\*\s*(?:\[)?(https://community\.lansweeper\.com/[^\s\]]+)'
    match = re.search(source_pattern, content)
    
    if match:
        return match.group(1)
    
    # Try to find any community URL in the first 500 characters
    url_pattern = r'(https://community\.lansweeper\.com/[^\s\)]+)'
    match = re.search(url_pattern, content[:500])
    
    if match:
        return match.group(1)
    
    return None

def create_new_url_path(file_path, root_path):
    """
    Create the new URL path based on filename only (no category folder).
    Format: /docs/{filename-slug}
    
    Args:
        file_path: Path object of the markdown file
        root_path: Root directory path
    
    Returns:
        New URL path string with leading slash
    """
    # Get filename without extension
    filename = file_path.stem
    
    # Convert filename to URL slug
    # Remove spaces, special chars, convert to lowercase
    slug = filename.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special characters
    slug = re.sub(r'[\s_]+', '-', slug)    # Replace spaces/underscores with hyphens
    slug = re.sub(r'-+', '-', slug)        # Replace multiple hyphens with single
    slug = slug.strip('-')                  # Remove leading/trailing hyphens
    
    # Build the new URL path with leading slash
    new_url = f"/docs/{slug}"
    
    return new_url

def generate_url_mapping(directory, output_file='url_mapping.csv'):
    """
    Generate a mapping of old URLs to new URLs for all markdown files.
    
    Args:
        directory: Root directory containing markdown files
        output_file: Output CSV filename
    """
    root_path = Path(directory)
    
    if not root_path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Find all markdown files recursively
    markdown_files = list(root_path.rglob('*.md')) + list(root_path.rglob('*.markdown'))
    
    if not markdown_files:
        print(f"No markdown files found in '{directory}'")
        return
    
    print(f"Found {len(markdown_files)} markdown file(s) to process.\n")
    print(f"{'='*80}")
    
    mappings = []
    success_count = 0
    no_url_count = 0
    duplicate_slugs = {}
    
    for md_file in markdown_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            old_url = extract_source_url(content)
            
            if old_url:
                new_url = create_new_url_path(md_file, root_path)
                
                # Get relative location for display
                relative_path = md_file.relative_to(root_path)
                
                # Track duplicate slugs
                if new_url in duplicate_slugs:
                    duplicate_slugs[new_url].append(str(relative_path))
                else:
                    duplicate_slugs[new_url] = [str(relative_path)]
                
                mappings.append({
                    'old_url': old_url,
                    'new_url': new_url,
                    'file_path': str(relative_path),
                    'filename': md_file.name
                })
                
                print(f"✓ {md_file.name}")
                print(f"  Old: {old_url}")
                print(f"  New: {new_url}")
                print()
                
                success_count += 1
            else:
                print(f"✗ {md_file.name}")
                print(f"  No source URL found")
                print()
                no_url_count += 1
                
        except Exception as e:
            print(f"✗ {md_file.name}")
            print(f"  Error: {str(e)}")
            print()
            no_url_count += 1
    
    # Check for duplicate slugs
    duplicates_found = {k: v for k, v in duplicate_slugs.items() if len(v) > 1}
    
    if duplicates_found:
        print(f"\n{'⚠'*40}")
        print(f"WARNING: Duplicate URL slugs detected!")
        print(f"{'⚠'*40}\n")
        for slug, files in duplicates_found.items():
            print(f"URL: {slug}")
            for file in files:
                print(f"  - {file}")
            print()
    
    # Write to CSV file
    if mappings:
        output_path = Path(output_file)
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['old_url', 'new_url', 'file_path', 'filename']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for mapping in mappings:
                writer.writerow(mapping)
        
        print(f"{'='*80}")
        print(f"URL mapping complete!")
        print(f"  Successfully mapped: {success_count}")
        print(f"  No URL found: {no_url_count}")
        if duplicates_found:
            print(f"  ⚠ Duplicate slugs: {len(duplicates_found)}")
        print(f"\nMapping saved to: {output_path.absolute()}")
        print(f"{'='*80}")
        
        # Also create a simple text version for easy viewing
        txt_output = output_path.with_suffix('.txt')
        with open(txt_output, 'w', encoding='utf-8') as txtfile:
            txtfile.write("URL MAPPING - OLD TO NEW\n")
            txtfile.write("="*80 + "\n\n")
            for mapping in mappings:
                txtfile.write(f"Old: {mapping['old_url']}\n")
                txtfile.write(f"New: {mapping['new_url']}\n")
                txtfile.write(f"File: {mapping['file_path']}\n")
                txtfile.write("-"*80 + "\n\n")
            
            if duplicates_found:
                txtfile.write("\n\nDUPLICATE URL SLUGS WARNING\n")
                txtfile.write("="*80 + "\n\n")
                for slug, files in duplicates_found.items():
                    txtfile.write(f"URL: {slug}\n")
                    for file in files:
                        txtfile.write(f"  - {file}\n")
                    txtfile.write("\n")
        
        print(f"Human-readable version saved to: {txt_output.absolute()}")
        
    else:
        print(f"{'='*80}")
        print(f"No URLs found to map!")
        print(f"{'='*80}")

if __name__ == "__main__":
    # CONFIGURATION
    # Set this to the directory containing your organized markdown files
    ARTICLES_DIR = "."  # Current directory, or specify path
    
    # Output CSV file name
    OUTPUT_FILE = "url_mapping.csv"
    
    # Run the mapping generator
    generate_url_mapping(ARTICLES_DIR, OUTPUT_FILE)