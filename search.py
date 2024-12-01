import re

def grep(pattern, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            if re.search(pattern, line):
                print(line.strip())
    return 

def sed(old_pattern, new_pattern, file_name):
    # ... 
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
    with open(file_name, 'w') as fp:
        for line in lines:
            updated_line = re.sub(old_pattern, new_pattern, line)#replace old pattern with new pattern
            fp.write(updated_line)#update new pattern lines in the file
    with open(file_name, 'r') as fp:
        for line in fp:
            print(line.strip())
    return

def awk(n, file_name):
    # ...
    n = int(n)
    with open(file_name, 'r') as fp:
        for line in fp:
            columns = line.split()
            if(len(columns)) >= n:
                print(columns[n-1])
            else:
                print("Column not found", n)
    return

def main():
    file_name = input("Enter the file name")
    command  = input("Enter the command: grep, sed, awk")

    if command == 'grep':
        pattern = input("Enter the pattern")
        grep(pattern, file_name);
    elif command == 'sed':
        old_pattern = input("Enter old pattern")
        new_pattern = input("Enter new pattern")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number")
        num = int(n)
        awk(n, file_name)
    else:
        print("Comamnd is invalid")

if __name__ == "__main__":
    main()
