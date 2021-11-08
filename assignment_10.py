
import os


def main():
    ask_user_directory()
    

def ask_user_filename():
    file_input = input("What is the name of the file you are trying to get? ")
    return file_input
    
def ask_user_directory():
    directory_input = input("What is the name of the directory you are trying to get access to?")
    directory = directory_exist(directory_input)
    filename = ask_user_filename()
    write_in_file(directory, filename)
    
def write_in_file(dir, filename):
    file = open(os.path.join(dir, filename), 'w')
    
    
    
def directory_exist(dir):
    tru = os.path.isdir(dir)
    if (tru):
        return dir
    else:
        directory = os.mkdir(dir)
        print("Folder Created")
        return directory
        
    
def ask_personal_info():
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("what is your phone number? ")
    
    
main()