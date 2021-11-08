
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
    read_in_file(directory, filename)
    
def write_in_file(dir, filename):
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("what is your phone number? ")
    file = open(os.path.join(dir, filename), 'w')
    file.write(f"{name}, {address}, {phone_number}")
    file.close()
    
def read_in_file(dir, filename):
    file = open(os.path.join(dir, filename), 'r')
    # this will only give read access
    for line in file:
        print(line)
    file.close()
    
def directory_exist(dir):
    tru = os.path.isdir(dir)
    if (tru):
        return dir
    else:
        directory = os.mkdir(dir)
        print("Folder Created")
        return directory
        
    

    
    
    
main()