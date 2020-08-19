#!/home/erolerten/anaconda3/bin/python

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
    files = []
    for file in os.listdir(folder):
        if file.lower().endswith(".webp"):
            print(os.path.join(folder, file))
            files.append(file)
    return files

def strip_file_ext(filename):
    stripped_filename = filename.split(".")[0]
    return stripped_filename

def make_folder(path):
    if os.path.exists(path) and os.path.isdir(path):
        return path
    elif os.path.exists(path):
        new_path_name = path + "_folder"
        return new_path_name
    else:
        os.mkdir(path)
        return path

def convert_webp():
    path = define_folder()
    file_extension = define_format()
    file_list = get_files(path)
    print(file_list)
    command_template = "dwebp example.webp -o example.png"
    for file in file_list:
        full_path = path + file
        filename_no_ext = strip_file_ext(file)
        folder_for_converted = make_folder(file_extension)
        command = 'dwebp "{}" -o {}/{}.{}'.format(full_path,folder_for_converted,filename_no_ext,file_extension)
        print("command to be excecuted:\n",command)
        os.system(command)

if __name__ == '__main__':
    convert_webp()