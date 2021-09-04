#!/usr/bin/python3
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--allfiles", action="store_true", help="Show hidden files and folders.")
args = parser.parse_args()

def printGreen(text, postfix=''): print("\033[92m{}\033[00m".format(text) + postfix)
def printGrey(text, postfix=''): print("\033[95m{}\033[00m".format(text) + postfix)

def listItems(items, label, zero_state):
    max_name_length = 0
    for f in items:
        if len(f) > max_name_length:
            max_name_length = len(f) + 4
    if len(items) > 0:
        printGreen(label)
        out = " "
        current_line_length = 0
        for f in items:
            entry = f.ljust(max_name_length)
            if current_line_length + len(entry) > 80:
                out += '\n '
                current_line_length = 0
            out += entry
            current_line_length += len(entry)
        print(out)
    else:
        printGrey(zero_state)
        print("")

path = os.getcwd()

# Make a list of the files and folders.
files = [d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d))]
files.sort()
folders = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
folders.sort()

# Remove hidden files and folders from the lists.
if not args.allfiles:
    files = [ f for f in files if "." != f[0]]
    folders = [ f for f in folders if "." != f[0]]

readme_filename = 'README.md'

# If there is a README.md file, display a short preview of it.
if os.path.isfile(readme_filename):
    lines = open(readme_filename, "r").readlines()[:5]
    print("")
    printGreen(readme_filename)
    for line in lines:
        if len(line.strip()) > 0: 
            print(" " + line.rstrip())

# Output to the console.
print("")
printGreen("Path: ", path)
print("")

# List folders.
listItems(folders, "Folders:", "No folders.")
print("")

# List Files
listItems(files, "Files:", "No files.")
print("")
