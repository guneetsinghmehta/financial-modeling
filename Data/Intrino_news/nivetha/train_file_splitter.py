from __future__ import print_function
import os, subprocess

def split_files_for_train_and_test(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print("The input folder doesn't exist")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = os.listdir(input_folder)
    no_of_train_files = 200
    if len(files) < no_of_train_files:
        print("Not enough files to train!")
        return
    train_files = files[:no_of_train_files]
    test_files = files[no_of_train_files:]
    if not os.path.exists(os.path.join(output_folder, "train")):
        os.makedirs(os.path.join(output_folder, "train"))
    if not os.path.exists(os.path.join(output_folder, "test")):
        os.makedirs(os.path.join(output_folder, "test"))
    for file_name in train_files:
        subprocess.call(['cp', os.path.join(input_folder,file_name), os.path.join(os.path.join(output_folder, "train"),file_name)])
    for file_name in test_files:
        subprocess.call(['cp', os.path.join(input_folder,file_name), os.path.join(os.path.join(output_folder, "test"),file_name)])


if __name__ == "__main__":
    split_files_for_train_and_test("new_dict_files", "classifier")
