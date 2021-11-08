
import os


def main():
    print()

def ask_user_filename():
    file_input = input("What is the name of the file you are trying to get? ")
    filename = filename_exist(file_input)
    return filename
    
def ask_user_directory():
    directory_input = input("What is the name of the directory you are trying to get access to?")
    directory = directory_exist(directory_input)
    filename = ask_user_filename()
    
    
def directory_exist(dir):
    tru = os.path.isdir(dir)
    if (tru):
        return dir
    else:
        directory = os.mkdir(dir)
        print("Folder Created")
        return directory
    
def filename_exist(file):
    tru = os.path.isfile(file)
    if (tru):
        fil = open(file, "r+")
        return fil
    else:
        fil = open(file, "r+")
        return fil
      
    
def ask_personal_info():
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("what is your phone number? ")