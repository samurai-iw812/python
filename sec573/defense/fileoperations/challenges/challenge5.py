#ask the user to write file path and check if exists and what is the extension and size
import os
import pathlib
from datetime import datetime

user_input = input("Enter file or directory path: ").strip()
# Expand ~ and environment variables, then build a Path
expanded = os.path.expandvars(os.path.expanduser(user_input))
path = pathlib.Path(expanded)

print("Exists:", path.exists())
if not path.exists():
    exit("Path does not exist")

if path.is_file():
    stat = path.stat()
    print("Type: File")
    print("Absolute:", str(path.resolve()))
    print("Size:", stat.st_size)
    print("Extension:", path.suffix or "(none)")
    print("Last modified:", datetime.fromtimestamp(stat.st_mtime))

elif path.is_dir():
    print("Type: Directory")
    print("Absolute:", str(path.resolve()))
    try:
        children_count = sum(1 for _ in path.iterdir())
        print("Children:", children_count)
    except PermissionError:
        print("Children: Permission denied")

else:
    # Could be a symlink, socket, device, etc.
    print("Type: Other")
    