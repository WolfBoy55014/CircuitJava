##====== This File is to be run by a Computer, not by CircuitPython ======##

import os
from shutil import copytree, ignore_patterns, rmtree, copy2

# List of files that should not be compiled
python_blacklist = ["build.py", "main.py", "list_pins.py"]
# List of files that should not be copied for production
not_for_production = ['build', '.git', '__pycache__', '.Trashes', ".Trash-1000", "examples", "boot_out.txt", "README.md", ".metadata_never_index", "TODO.md", ".vscode", ".fseventsd", "*.py", ".gitattributes", ".gitignore"]

controller_dir = "D:/"
working_dir = os.getcwd().replace("\\", "/")
build_dir = working_dir + "/build"

filenames = next(os.walk("."), (None, None, []))[2]  # [] if no file
directories = next(os.walk("."), (None, None, []))[1]  # [] if no folders

# Refine file list
python_files = [file for file in filenames if file.endswith('.py') and file not in python_blacklist]

# Refine file list
filenames = [file for file in filenames if file not in not_for_production]

# Recurse through directories to find more python files
for directory in directories:
    filenames = next(os.walk(directory), (None, None, []))[2]  # [] if no file
    new_directories = next(os.walk(directory), (None, None, []))[1]  # [] if no folders
    
    if len(new_directories) > 0:
        directories.extend([directory + '/' + new_directory for new_directory in new_directories])
        
    python_files.extend([directory + '/' + file for file in filenames if file.endswith('.py') and file not in python_blacklist])


# Remove build directory if it exists
if os.path.exists(build_dir):
    rmtree(build_dir)

# Copy files to build directory
copytree(working_dir, build_dir, ignore=ignore_patterns(*not_for_production))

# Copy main.py because it was missed
copy2(working_dir + "/main.py", build_dir + "/main.py")

for file in python_files:
    os.system(f"mpy-cross.exe {working_dir}/{file} -o {build_dir}/{file.replace('.py', '.mpy')}")

    # [BETA] for RP2 Based Microcontrollers
    # if (os.system(f"mpy-cross.exe {working_dir}/{file} -o {build_dir}/{file.replace('.py', '.mpy')} -march=armv6m -X emit=native") != 0):
    #     print(f"File {file} will not be compiled to Native code. Compiling to bytecode instead")
    #     os.system(f"mpy-cross.exe {working_dir}/{file} -o {build_dir}/{file.replace('.py', '.mpy')}")