"""
Tests for the File Organizer
Run with: python test_organizer.py
"""

import os
import shutil
import tempfile
import unittest
from organizer import get_folder_for_file, organize_folder


class TestGetFolderForFile(unittest.TestCase):

    def test_image_extensions(self):
        self.assertEqual(get_folder_for_file("photo.jpg"), "Images")
        self.assertEqual(get_folder_for_file("icon.PNG"), "Images")  # case-insensitive
        self.assertEqual(get_folder_for_file("banner.svg"), "Images")

    def test_document_extensions(self):
        self.assertEqual(get_folder_for_file("notes.txt"), "Documents")
        self.assertEqual(get_folder_for_file("report.pdf"), "Documents")
        self.assertEqual(get_folder_for_file("essay.docx"), "Documents")

    def test_video_extensions(self):
        self.assertEqual(get_folder_for_file("clip.mp4"), "Videos")
        self.assertEqual(get_folder_for_file("movie.mkv"), "Videos")

    def test_unknown_extension(self):
        self.assertEqual(get_folder_for_file("weird.xyz123"), "Others")
        self.assertEqual(get_folder_for_file("noextension"), "Others")

    def test_code_files(self):
        self.assertEqual(get_folder_for_file("script.py"), "Code")
        self.assertEqual(get_folder_for_file("index.html"), "Code")

    def test_archive_files(self):
        self.assertEqual(get_folder_for_file("backup.zip"), "Archives")
        self.assertEqual(get_folder_for_file("data.tar"), "Archives")


class TestOrganizeFolder(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory with sample files."""
        self.test_dir = tempfile.mkdtemp()
        self.sample_files = [
            "photo.jpg", "video.mp4", "notes.txt",
            "script.py", "archive.zip", "song.mp3",
            "spreadsheet.xlsx", "unknown.xyz"
        ]
        for f in self.sample_files:
            open(os.path.join(self.test_dir, f), "w").close()

    def tearDown(self):
        """Remove the temporary directory after each test."""
        shutil.rmtree(self.test_dir)

    def test_dry_run_does_not_move_files(self):
        organize_folder(self.test_dir, dry_run=True)
        # All original files should still be in root
        remaining = os.listdir(self.test_dir)
        for f in self.sample_files:
            self.assertIn(f, remaining)

    def test_files_are_moved_to_correct_folders(self):
        organize_folder(self.test_dir, dry_run=False)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "photo.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Videos", "video.mp4")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "notes.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Code", "script.py")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Archives", "archive.zip")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Audio", "song.mp3")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Spreadsheets", "spreadsheet.xlsx")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Others", "unknown.xyz")))

    def test_invalid_path_returns_empty(self):
        result = organize_folder("/nonexistent/path/12345")
        self.assertEqual(result, {})

    def test_empty_folder_returns_empty(self):
        empty_dir = tempfile.mkdtemp()
        result = organize_folder(empty_dir, dry_run=False)
        self.assertEqual(result, {})
        shutil.rmtree(empty_dir)


if __name__ == "__main__":
    unittest.main(verbosity=2)
