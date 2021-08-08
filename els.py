import os.path

def printGreen(text, postfix=''): print("\033[92m {}\033[00m".format(text) + postfix)

path = os.getcwd()

files = [d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d))]
files.sort()
folders = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
folders.sort()

# Output to the console.
print()
printGreen("Path: ", path)
print()

if len(folders) > 0:
    printGreen("Folders:")
    for f in folders:
        print(f)
    else:
        print("No folders.")
if len(files) > 0:
    print("")
    printGreen("Files:")
    for f in files:
        print(f)
else:
    print("No files.")
print("")