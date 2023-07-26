# creating of packages
# renaming of packages
# creation of a set with start files and web-sites
import os
import time


def folder_make(number, folder_name, parent_dir):
    i=1
    while i<number:
        folder_names = f"{folder_name}_{i}"
        path = os.path.join(parent_dir, folder_names)
        os.mkdir(path)
        print(f"{folder_names} is made")
        i+=1


def folder_rename(number, old_name, new_name):
    i=1
    while i<number:
        old_names = f"{old_name} ({i})"
        new_names = f"{new_name}_{i}"
        os.rename(old_names, new_names)
        print(f"{old_names} is renamed into {new_names} successfully")
        i+=1


def start_web_site(name):
    os.system("start {name}")
    time.sleep(1)


def start_file(path):
    os.startfile({path})
    time.sleep(1)
