
import os


def main():
    print()

def ask_user_filename():
    file = input("What is the name of the file you are trying to get? ")
    
def ask_user_directory():
    directory_input = input("What is the name of the directory you are trying to get access to?")
    directory = directory_exist(directory_input)
    
    
def directory_exist(dir):
    directory = ''
    tru = os.path.isdir(dir)
    if (tru):
        directory = dir
    else:
        directory = os.mkdir(dir)
        print("Folder Created")
    return directory
    
def filename_exist(file):
    fil = ''
    tru = os.path.isfile(file)
    if (tru):
        fil = open(file, "r+")
    else:
        fil = open(file, "r+")
    return fil
      
    
def ask_personal_info():
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("what is your phone number? ")