##====== This File is to be run by a Computer, not by CircuitPython ======##

import os

# List of files that should not be compiled
blacklist = ["compile.py"]

working_dir = os.getcwd()

filenames = next(os.walk("."), (None, None, []))[2]  # [] if no file
directories = next(os.walk("."), (None, None, []))[1]  # [] if no folders

# Refine file list
python_files = [file for file in filenames if file.endswith('.py') and file not in blacklist]

# Recurse through directories to find more python files
for directory in directories:
    filenames = next(os.walk(directory), (None, None, []))[2]  # [] if no file
    new_directories = next(os.walk(directory), (None, None, []))[1]  # [] if no folders
    if len(new_directories) > 0:
        directories.extend([directory + '/' + new_directory for new_directory in new_directories])
    python_files.extend([directory + '/' + file for file in filenames if file.endswith('.py') and file not in blacklist])

print(python_files)