import os
import sys

def create_directory(dir_name):
    # ...
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.")
    else:
        print(f"Directory '{dir_name}' already exists.")

    return

def change_directory(dir_name):
    # ...
    if os.path.exists(dir_name):
        os.chdir(dir_name)
        print(f"Changed to directory '{dir_name}'.")
    else:
        print(f"Directory '{dir_name}' does not exist.")

    return

def delete_directory(dir_name):
    # ...
    if os.path.exists(dir_name) and not os.listdir(dir_name):
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' deleted successfully.")
    else:
        print(f"Cannot delete directory '{dir_name}'. Either it does not exist or it is not empty.")

    return

def list_dir():
    # ...
    print("Contents of the current directory:")
    print("\n".join(os.listdir()))

    return

def display_pwd():
    # ...
    print(f"Current working directory: {os.getcwd()}")

    return

def create_file(file_name):

    with open(file_name, 'w') as f:
        pass
    print(f"File '{file_name}' is created")

    return

def write_file(file_name):

    contents = input("Enter the contents into the file");
    with open(file_name, 'a') as f:
        f.write(contents + '\n');
    print(f"Contents written to file successfully")

    return

def read_file(file_name):

    with open(file_name, 'r') as f:
        print(f.read());

    return

def delete_file(file_name):
    os.remove(file_name)
    
    return

def main():
    while True:
        print("1. Create a Directory")
        print("2. Change directory")
        print("3. Delete a directory")
        print("4. List directories")
        print("5. Display current working path")
        print("6. Create a file")
        print("7. Write to a file")
        print("8. Read a file")
        print("9. Delete a file")
        print("0. Exit")
        choice = input("Enter your choice here: ")

        if choice == '1':
            create_directory(input("Enter directory name: "))
        elif choice == '2':
            change_directory(input("Enter directory name: "))
        elif choice == '3':
            delete_directory(input("Enter directory name: "))
        elif choice == '4':
            list_dir()
        elif choice == '5':
            display_pwd()
        elif choice == '6':
            create_file(input("Enter file name: "))
        elif choice == '7':
            write_file(input("Enter file name: "))
        elif choice == '8':
            read_file(input("Enter file name: "))
        elif choice == '9':
            delete_file(input("Enter file name: "))
        elif choice == '0':
            break
        else:
            print("Invalid choice");


if __name__ == "__main__":
    main()
