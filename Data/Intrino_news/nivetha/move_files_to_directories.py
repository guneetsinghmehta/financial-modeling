# This file was used to split the news document amoung
# the team members

# This file currently just moves the essential file for the author

# author: Nivetha

import os
import subprocess

def move_files_to_folder(input_directory, output_directory):
    files = [ x for x in os.listdir(input_directory) if os.path.isfile(input_directory + "/" + x) ]
    files.sort()
    for file_name in files:
        if file_name.split('_')[0] == "C":
            return
        subprocess.call(["mv", input_directory + "/" + file_name, output_directory + "/"])


if __name__ == "__main__":
    move_files_to_folder(".", "nivetha")
