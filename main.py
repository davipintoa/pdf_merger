
import os
import sys
import datetime
from typing import List, Tuple
from pypdf import PdfWriter

# Try importing natsort for natural sorting, otherwise fallback to sorted
try:
    from natsort import natsorted as sorted_func
except ImportError:
    sorted_func = sorted

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

def get_pdf_files(directory: str) -> List[str]:
    """Scans the directory for PDF files."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        return []
        
    files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    return sorted_func(files)

def display_files(files: List[str]):
    """Displays the list of files with their index."""
    if not files:
        print("No PDF files found in the 'input' directory.")
        return

    print("\nAvailable PDF files:")
    for idx, file in enumerate(files, 1):
        print(f"[{idx}] {file}")

def get_user_order(files: List[str]) -> List[str]:
    """Prompts the user for the order of files to merge."""
    if not files:
        return []

    print("\nEnter the index of the files in the order you want to merge them.")
    print("Separate numbers with commas (e.g., 3, 1, 2) or spaces.")
    print("Press ENTER to merge all files in the displayed order.")
    
    while True:
        try:
            user_input = input("Order: ").strip()
            
            if not user_input:
                return files # Return original order if input is empty

            # Replace commas with spaces and split
            parts = user_input.replace(',', ' ').split()
            indices = [int(p) for p in parts]
            
            # Validate indices
            selected_files = []
            valid = True
            for idx in indices:
                if 1 <= idx <= len(files):
                    selected_files.append(files[idx-1])
                else:
                    print(f"Invalid index: {idx}. Please try again.")
                    valid = False
                    break
            
            if valid:
                return selected_files
                
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def merge_pdfs(files: List[str], base_dir: str):
    """Merges the given list of PDF files."""
    if not files:
        print("No files selected for merging.")
        return

    merger = PdfWriter()

    print("\nMerging files...")
    for pdf in files:
        file_path = os.path.join(base_dir, pdf)
        try:
            print(f"Adding: {pdf}")
            merger.append(file_path)
        except Exception as e:
            print(f"Error adding {pdf}: {e}")
            merge = False # Flag to stop? No, maybe skip.
            # But usually if one fails, the whole merge might be bad.
            # Let's continue but warn.

    # Create output directory
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder_name = f"merged_{timestamp}"
    output_path_full = os.path.join(OUTPUT_DIR, output_folder_name)
    
    if not os.path.exists(output_path_full):
        os.makedirs(output_path_full)

    output_filename = "merged_output.pdf"
    final_output_path = os.path.join(output_path_full, output_filename)

    try:
        merger.write(final_output_path)
        merger.close()
        print(f"\nSuccessfully merged {len(files)} files!")
        print(f"Saved to: {os.path.abspath(final_output_path)}")
    except Exception as e:
        print(f"Error saving merged file: {e}")

def main():
    print("--- PDF Merger Tool ---")
    
    # Check if input directory exists
    if not os.path.exists(INPUT_DIR):
        print(f"Creating '{INPUT_DIR}' directory...")
        os.makedirs(INPUT_DIR)
        print(f"Please place your PDF files in the '{INPUT_DIR}' folder and run this script again.")
        input("Press Enter to exit...")
        return

    # Check if output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = get_pdf_files(INPUT_DIR)
    
    if not files:
        print(f"No PDF files found in '{INPUT_DIR}'.")
        print(f"Please place your PDF files in the '{INPUT_DIR}' folder and run this script again.")
        input("Press Enter to exit...")
        return

    display_files(files)
    
    selected_files = get_user_order(files)
    
    if selected_files:
        merge_pdfs(selected_files, INPUT_DIR)
    
    print("\nDone.")
    try:
        # Keep window open if double-clicked
        input("Press Enter to exit...")
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
