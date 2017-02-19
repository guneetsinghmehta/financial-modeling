import os, sys, subprocess

def get_done_files_from_text_file(file_name):
    done_files = None
    with open(file_name, "r") as f:
        done_files = [x.strip() for x in f.readlines()]
    return done_files

def is_file_marked(file_name):
    if not os.path.exists(file_name):
        return False
    with open(file_name, "r") as f:
        line = f.readlines()[0]
        if line.startswith("<p>"):
            return True
    return False
def move_files_to_done_folder(folder_name, done_files):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for file_name in done_files:
        if is_file_marked(file_name):
            subprocess.call(['mv', file_name, folder_name + "/"])

if __name__ == "__main__":
    done_files = get_done_files_from_text_file("done_files.txt")
    if done_files == None:
        print("Could not get proper done files")
        sys.exit()
    move_files_to_done_folder("done_files", done_files)
