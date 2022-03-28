import os
import shutil
import random

# Put the directory addresses here from to where you want random names to:
src_path = r".\docs"
dst_path = r".\new_docs"

# sets all the vars for the methods
src_files = os.listdir(src_path)
dst_files = os.listdir(dst_path)
reset_files = ["cow", "cat", "dog", "donkey", "beer", "rat"]
src_path_files = []
files_ext = []
ran_numb = []


# saves the extentions of the file source that you put in and then saves the extentions in files_ext array
def get_extentions(files):
    c = 0
    while c < len(files):
        Split_ext = os.path.splitext(str(files[c]))
        files_ext.append(Split_ext[1])
        c += 1


# saves the paths from the source files in the scr_path_files array
def get_scr_paths():
    y = 0
    while y < len(src_files):
        src_path_files.append(src_path + "\\" + src_files[y])
        y += 1


# it generates from the any number input and then recalls the shuffle
def set_random(length):
    g = 0
    while g < length:
        ran_numb.append(g+1)
        g += 1
    shuffle(ran_numb)
    shuffle(ran_numb)


# * * * * * * *
# * Why: shuffling any array into random order 2 times
# * Input: any array[] whit any data
# * Return: shuffled array[]
# * Exception: TypeError returned if input in not an array[]
# * * * * * * *
def shuffle(ar):
    if isinstance(ar, list):
        random.shuffle(ar)
        random.shuffle(ar)
        return ar
    else:
        raise TypeError("Input needs to be an array[]")


# sets the files from the source path to the destination path whit the right extentions but random numbers
def replace():
    set_random(len(src_files))
    get_scr_paths()
    get_extentions(src_files)

    i = 0
    while i < len(src_path_files):
        shutil.move(src_path_files[i], dst_path + "\\" + str(ran_numb[i]) + files_ext[i])
        i += 1


# replaces all destinations files to the source path whit the right extention and the preset names in reset_files
def reset():
    get_scr_paths()
    get_extentions(dst_files)
    i = 0
    while i < len(dst_files):
        shutil.move(dst_path + "\\" + dst_files[i], src_path + "\\" + reset_files[i] + files_ext[i])
        i += 1


testing = [1, 2, 3]
testing = shuffle(testing)
print(testing)
# replace()
# reset()
