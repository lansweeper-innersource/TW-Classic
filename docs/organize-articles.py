import os
import re
from pathlib import Path

def extract_folder_from_url(file_path):
    """
    Extract the folder name from the community URL in the markdown file.
    Returns None if no valid URL is found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the Lansweeper community URL pattern
        # Pattern: https://community.lansweeper.com/t5/{folder-name}/...
        pattern = r'https://community\.lansweeper\.com/t5/([^/]+)/'
        match = re.search(pattern, content)
        
        if match:
            folder_name = match.group(1)
            # Convert URL-style naming to folder-friendly format
            # e.g., "billing-related-questions" -> "Billing Related Questions"
            folder_name = folder_name.replace('-', ' ').title()
            return folder_name
        
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def organize_articles(source_directory, target_directory=None):
    """
    Organize markdown articles into folders based on their community URLs.
    
    Args:
        source_directory: Directory containing the markdown files
        target_directory: Directory where organized folders will be created 
                         (defaults to source_directory)
    """
    source_path = Path(source_directory)
    target_path = Path(target_directory) if target_directory else source_path
    
    if not source_path.exists():
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return
    
    # Find all markdown files
    markdown_files = list(source_path.glob('*.md')) + list(source_path.glob('*.markdown'))
    
    if not markdown_files:
        print(f"No markdown files found in '{source_directory}'")
        return
    
    print(f"Found {len(markdown_files)} markdown file(s) to process.\n")
    
    moved_count = 0
    skipped_count = 0
    
    for md_file in markdown_files:
        # Skip if file is already in a subdirectory
        if md_file.parent != source_path:
            continue
            
        folder_name = extract_folder_from_url(md_file)
        
        if folder_name:
            # Create the target folder if it doesn't exist
            target_folder = target_path / folder_name
            target_folder.mkdir(exist_ok=True)
            
            # Move the file
            target_file = target_folder / md_file.name
            
            # Handle duplicate filenames
            if target_file.exists():
                print(f"⚠️  '{md_file.name}' already exists in '{folder_name}' - skipping")
                skipped_count += 1
            else:
                md_file.rename(target_file)
                print(f"✓ Moved '{md_file.name}' -> '{folder_name}/'")
                moved_count += 1
        else:
            print(f"✗ No valid URL found in '{md_file.name}' - skipping")
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"Organization complete!")
    print(f"  Files moved: {moved_count}")
    print(f"  Files skipped: {skipped_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    # CONFIGURATION
    # Set this to the directory containing your markdown files
    SOURCE_DIR = "."  # Current directory, or specify a path like "C:/Users/YourName/Articles"
    
    # Optional: Set a different target directory for organized folders
    # Leave as None to organize in the same directory
    TARGET_DIR = None
    
    # Run the organization
    organize_articles(SOURCE_DIR, TARGET_DIR)