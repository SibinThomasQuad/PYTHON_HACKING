import shutil
import sys
import os

def create_copy():
    current_file = sys.argv[0]
    new_file = current_file.split(".")[0] + "_copy.py"
    shutil.copyfile(current_file, new_file)

if __name__ == "__main__":
    create_copy()
    print("Program copied itself successfully!")
