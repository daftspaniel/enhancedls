#!/usr/bin/python3
import os.path

def printGreen(text, postfix=''): print("\033[92m {}\033[00m".format(text) + postfix)

path = os.getcwd()

files = [d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d))]
files.sort()
folders = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
folders.sort()

readme_filename = 'README.md'

if os.path.isfile(readme_filename):
    lines = open(readme_filename, "r").readlines()[:5]
    print("")
    printGreen(readme_filename)
    for line in lines:
        if len(line.strip()) > 0: print(" " + line.rstrip())

# Output to the console.
print("")
printGreen("Path: ", path)
print("")

max_folder_name_length = 0
for f in folders:
    if len(f) > max_folder_name_length:
        max_folder_name_length = len(f) + 3
max_file_name_length = 0
for f in files:
    if len(f) > max_file_name_length:
        max_file_name_length = len(f) + 3

if len(folders) > 0:
    printGreen("Folders:")
    out = " "
    for f in folders:
        out += f.ljust(max_folder_name_length)
    print(out)
else:
    print("No folders.")

if len(files) > 0:
    print("")
    printGreen("Files:")
    out = " "
    for f in files:
        out += f.ljust(max_file_name_length)
    print(out)
else:
    print("No files.")
print("")
