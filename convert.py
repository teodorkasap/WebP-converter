import os
import fnmatch

def define_folder():
    current_folder = os.getcwd()
    folder_to_convert = input(
        "Enter a folder with the files you want to convert: ")

    folder = current_folder + "/" + folder_to_convert
    return folder


def define_format():
    format = input("Enter format to convert WebP files to: ")
    return format

def get_files(folder):
    for file in os.listdir(folder):
        if file.lower().endswith(".md"):
            print(os.path.join(folder, file))


path = define_folder()
get_files(path)
