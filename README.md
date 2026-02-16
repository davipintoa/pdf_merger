# PDF Merger Tool

A simple Python script to merge multiple PDF files into one.

## Features
- Scans the `input` folder for PDF files.
- Allows you to choose the order of merging.
- Supports natural sorting (e.g., 1.pdf, 2.pdf, 10.pdf correctly ordered).
- Saves the merged file in a timestamped folder inside `output/`.

## Quick Start

1.  **Setup:**
    Double-click `setup.bat`. This will verify Python is installed, create a virtual environment, and install all necessary dependencies.

2.  **Run:**
    Double-click `run.bat` to launch the tool.

## Manual Setup

If you prefer to set up manually:

1.  **Install Requirements:**
    Make sure you have Python installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Add PDFs:**
    Place the PDF files you want to merge into the `input` folder.

## Usage

1.  Run the script (or use `run.bat`):
    ```bash
    python main.py
    ```

2.  Follow the on-screen prompts:
    - The script will list the available PDFs.
    - Enter the numbers of the files in the order you want them merged (e.g., `3, 1, 2`).
    - Press **Enter** without typing anything to merge all files in the displayed order.

3.  **Find Output:**
    The merged PDF will be saved in a new folder inside `output/` (e.g., `output/merged_20231027_1530/merged_output.pdf`).

## Troubleshooting
- If no files are found, make sure they are `.pdf` files inside the `input` directory.
- If you see an error about `pypdf` or `natsort` missing, run the pip install command again.
