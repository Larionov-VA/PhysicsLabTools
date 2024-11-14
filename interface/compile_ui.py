# compiles all .ui files in directory into .py files
import subprocess
import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()
files = os.listdir(path)
for file in files:
    if ".ui" in file:
        compiled_file = file.replace(".ui", "Window.py")
        subprocess.Popen(f"pyside6-uic {str(path)+ str("\\") + file} -o {str(path) + str("\\") + compiled_file}", shell=True)
        print(f"{file} -> {compiled_file}")
