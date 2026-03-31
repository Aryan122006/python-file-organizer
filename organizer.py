"""
File Organizer - Automatically sort files into folders by type
Author: Aryana Chaturvedi
Course: Python Essentials
"""

import os
import shutil
from datetime import datetime

# --- Configuration: Map file extensions to folder names ---
FILE_TYPES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Archives":   [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ts", ".json", ".xml"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
}


def get_folder_for_file(filename):
    """Return the destination folder name for a given filename."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Others"  # Default folder for unrecognized types


def organize_folder(target_path, dry_run=False):
    """
    Organize all files in target_path into subfolders by type.

    Args:
        target_path (str): Path to the folder to organize.
        dry_run (bool): If True, only show what would happen without moving files.

    Returns:
        dict: Summary of moved files {folder: [filenames]}
    """
    if not os.path.isdir(target_path):
        print(f"Error: '{target_path}' is not a valid directory.")
        return {}

    summary = {}
    skipped = []
    files = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]

    if not files:
        print("No files found to organize.")
        return {}

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Organizing: {target_path}")
    print(f"Found {len(files)} file(s).\n")

    for filename in files:
        # Skip hidden files (e.g., .DS_Store on Mac)
        if filename.startswith("."):
            skipped.append(filename)
            continue

        destination_folder = get_folder_for_file(filename)
        dest_dir = os.path.join(target_path, destination_folder)
        src_path = os.path.join(target_path, filename)
        dest_path = os.path.join(dest_dir, filename)

        # Handle duplicate filenames by appending a timestamp
        if os.path.exists(dest_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}{ext}"
            dest_path = os.path.join(dest_dir, filename)

        if dry_run:
            print(f"  [WOULD MOVE] {filename}  →  {destination_folder}/")
        else:
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(src_path, dest_path)
            print(f"  Moved: {filename}  →  {destination_folder}/")

        # Track summary
        if destination_folder not in summary:
            summary[destination_folder] = []
        summary[destination_folder].append(filename)

    # Print summary
    print("\n--- Summary ---")
    for folder, file_list in sorted(summary.items()):
        print(f"  {folder}: {len(file_list)} file(s)")
    if skipped:
        print(f"  Skipped (hidden): {len(skipped)} file(s)")

    action = "Would move" if dry_run else "Moved"
    total = sum(len(v) for v in summary.values())
    print(f"\n{action} {total} file(s) total.")
    return summary


def main():
    print("============================")
    print("   Python File Organizer    ")
    print("============================")

    # Ask user for folder path
    target = input("\nEnter the folder path to organize (or press Enter for current directory): ").strip()
    if not target:
        target = os.getcwd()

    # Ask for dry run
    dry_input = input("Run in preview mode first? (yes/no) [yes]: ").strip().lower()
    dry_run = dry_input not in ("no", "n")

    organize_folder(target, dry_run=dry_run)

    # If dry run, offer to actually run
    if dry_run:
        confirm = input("\nProceed with actual organization? (yes/no) [no]: ").strip().lower()
        if confirm in ("yes", "y"):
            organize_folder(target, dry_run=False)
        else:
            print("No files were moved. Exiting.")


if __name__ == "__main__":
    main()
