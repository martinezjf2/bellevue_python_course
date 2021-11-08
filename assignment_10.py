
import os


def main():
    ask_user_directory()
    

def ask_user_filename():
    file_input = input("\nWhat is the name of the file you are trying to get? ")
    return file_input
    
def ask_user_directory():
    directory_input = input("\nWhat is the name of the directory you are trying to get access to? ")
    directory = directory_exist(directory_input)
    filename = ask_user_filename()
    write_in_file(directory, filename)
    read_in_file(directory, filename)
    
def write_in_file(dir, filename):
    name = input("\nWhat is your name? ")
    address = input("\nWhat is your address? ")
    phone_number = input("\nwhat is your phone number? ")
    file = open(os.path.join(dir, filename), 'w')
    file.write(f"{name}, {address}, {phone_number}")
    file.close()
    
def read_in_file(dir, filename):
    # print(dir)
    # print(filename)
    file = open(os.path.join(dir, filename), 'r')
    # print(file)
    # this will only give read access
    print("\n\nContents: \n")
    for line in file:
        print(f"{line} \n")
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