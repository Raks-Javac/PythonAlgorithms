from pathlib import Path

path = Path()
file_path = path.glob("pythonBasics/*.*")

for files in file_path:
    print(files)
