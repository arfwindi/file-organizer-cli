import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".md"],
    "archives": [".zip", ".rar", ".tar", ".gz"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".flac"],
}

def organize_files(folder: str):
    path = Path(folder)
    if not path.exists():
        print(f"❌ Folder not found: {path}")
        return

    for file in path.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in EXTENSION_MAP.items():
                if file.suffix.lower() in extensions:
                    dest = path / category
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(file), dest / file.name)
                    print(f"📦 Moved {file.name} → {category}/")
                    moved = True
                    break
            if not moved:
                other = path / "others"
                other.mkdir(exist_ok=True)
                shutil.move(str(file), other / file.name)
                print(f"📁 Moved {file.name} → others/")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ").strip() or "."
    organize_files(folder)
