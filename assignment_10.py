
import os


def main():
    print()

def ask_user_filename():
    file = input("What is the name of the file you are trying to get? ")
    
def ask_user_directory():
    directory = input("What is the name of the directory you are trying to get access to?")
    
def directory_exist(dir):
    tru = os.path.isdir(dir)
    
    
def filename_exist(file):
    tru = os.path.isfile(file)
      
    
def ask_personal_info():
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("what is your phone number? ")