# Task 1: Read from a file
try:
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

