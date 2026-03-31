# 🗂️ Python File Organizer

A beginner-friendly Python script that automatically sorts files in any folder into subfolders based on their file type — no more messy Downloads folders!

---

## 📌 What It Does

Running this script on a cluttered folder like your Downloads will automatically sort files like this:

```
Downloads/
├── Images/        → .jpg, .png, .gif, .svg ...
├── Videos/        → .mp4, .mkv, .avi ...
├── Audio/         → .mp3, .wav, .flac ...
├── Documents/     → .pdf, .docx, .txt ...
├── Spreadsheets/  → .xlsx, .csv ...
├── Presentations/ → .pptx, .odp ...
├── Archives/      → .zip, .rar, .tar ...
├── Code/          → .py, .js, .html ...
├── Executables/   → .exe, .dmg ...
└── Others/        → anything unrecognized
```

---

## 🛠️ Requirements

- Python 3.6 or higher
- No external libraries needed — uses only Python's built-in `os`, `shutil`, and `datetime` modules

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **Verify Python is installed**
   ```bash
   python --version
   ```
   If you see `Python 3.x.x`, you're good to go!

---

## ▶️ How to Use

Run the script from your terminal:

```bash
python organizer.py
```

You will be prompted:

1. **Enter the folder path** you want to organize (press Enter to use the current directory)
2. **Choose preview mode** — it shows what *would* happen without moving anything
3. **Confirm** to proceed with the actual move

### Example Session

```
============================
   Python File Organizer
============================

Enter the folder path to organize: C:\Users\John\Downloads
Run in preview mode first? (yes/no) [yes]: yes

[DRY RUN] Organizing: C:\Users\John\Downloads
Found 12 file(s).

  [WOULD MOVE] photo_2024.jpg  →  Images/
  [WOULD MOVE] lecture.mp4     →  Videos/
  [WOULD MOVE] notes.pdf       →  Documents/
  [WOULD MOVE] setup.exe       →  Executables/
  ...

--- Summary ---
  Documents:   3 file(s)
  Images:      4 file(s)
  Videos:      2 file(s)
  Executables: 1 file(s)
  Others:      2 file(s)

Would move 12 file(s) total.

Proceed with actual organization? (yes/no) [no]: yes
```

---

## 🧪 Running Tests

The project includes a test suite to verify all functionality:

```bash
python test_organizer.py
```

Expected output:
```
Ran 10 tests in 0.05s
OK
```

---

## 📁 Project Structure

```
file-organizer/
├── organizer.py        # Main script
├── test_organizer.py   # Unit tests
└── README.md           # This file
```

---

## 🔒 Safety Features

- **Preview (dry run) mode** — see changes before they happen
- **Duplicate file protection** — files with the same name get a timestamp appended instead of being overwritten
- **Hidden files skipped** — files starting with `.` (like `.DS_Store`) are left untouched
- **Invalid path detection** — graceful error message if path doesn't exist

---

## 💡 Concepts Used

| Concept | Where Used |
|---|---|
| Functions | `get_folder_for_file()`, `organize_folder()`, `main()` |
| Dictionaries | `FILE_TYPES` mapping extensions to folders |
| Loops | Iterating over files in directory |
| Conditionals | Routing files, handling duplicates |
| `os` module | Directory listing, path joining, folder creation |
| `shutil` module | Moving files |
| `datetime` module | Timestamping duplicate files |
| Unit Testing | `test_organizer.py` with `unittest` |

---

## 📜 License

This project was created as part of a Python Essentials course capstone project.

