#write code counts the nuber of folders and the number of files
import os

x=os.walk("/var/log")
folders=0
files=0
for root, dirs, filenames in x:
    folders+=len(dirs)
    files+=len(filenames)
print(f"Number of folders: {folders}")
print(f"Number of files: {files}")