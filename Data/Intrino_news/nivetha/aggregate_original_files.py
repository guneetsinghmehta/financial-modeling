import os, subprocess

def check_path_exists(path, create_path = False):
    if not create_path and not os.path.exists(path):
        print(path + " doesn't exist!")
        return False
    if not os.path.exists(path):
        os.makedirs(path)
    return True

def move_files(input_folder, output_folder):
    if not check_path_exists(input_folder):
        return
    check_path_exists(output_folder, True)
    input_files = os.listdir(input_folder)
    for file_name in input_files:
        subprocess.call(['cp', os.path.join(input_folder, file_name), os.path.join(output_folder, file_name)])

def move_all_files():
    move_files("../Marked_files", "output_files")
    move_files("../neha/done_files1", "output_files")
    move_files("../GuneetNew/cleanedup_files", "output_files")

def split_files_into_train_and_test():
    train_files = os.listdir("classifier/train")
    test_files = os.listdir("classifier/test")
    check_path_exists("output_files/train", True)
    check_path_exists("output_files/test", True)
    for file_name in train_files:
        subprocess.call(['mv', os.path.join('output_files', file_name), os.path.join('output_files/train', file_name)])
    for file_name in test_files:
        subprocess.call(['mv', os.path.join('output_files', file_name), os.path.join('output_files/test', file_name)])

if __name__ == "__main__":
    move_all_files()
    split_files_into_train_and_test()
