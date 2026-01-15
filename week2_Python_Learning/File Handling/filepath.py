"""
File path operations module.
Demonstrates working with file paths using the os module including:
- Getting current working directory
- Creating directories
- Listing files and directories
- Joining paths
- Checking if paths exist
- Distinguishing between files and directories
- Converting relative to absolute paths
"""

import os

# Get current working directory
cwd = os.getcwd()
print(cwd)

# Create new directory
new_directory = "package"
os.mkdir(new_directory)

# Listing files and directories
files = os.listdir('.')
print(files)

# Joining paths
dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(cwd, dir_name, file_name)
print(full_path)

# To check if path exists
path = "example1.txt"
if os.path.exists(path):
    print(f"The path {path} exists")
else:
    print(f"The path {path} does not exist")

# To check if path is file or directory
path = "package"
if os.path.isfile(path):
    print(f"The path {path} is file")
elif os.path.isdir(path):
    print(f"The path {path} is directory")
else:
    print(f"The path {path} is neither file or directory")

# Absolute path - Complete path
# Relative path
relative_path = "StoryFile.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
