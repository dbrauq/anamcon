from uuid import uuid4

from os.path import dirname, abspath, isfile, isdir, join
from os import listdir, remove, rmdir
from shutil import copytree

def create_uuidv4(): 
    return str(uuid4())

def delete_folder_content(folder):
    for path in listdir(folder):
        abs_path = join(folder, path)
        if isfile(abs_path): remove(abs_path)
        elif isdir(abs_path):
            delete_folder_content(abs_path)
            rmdir(abs_path)

def copy_folder_content(source, destination):
    copytree(source,destination)
