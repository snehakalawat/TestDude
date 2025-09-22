# Task 2: Write, append, and read from a file

# Step 1: Take user input and write to file
user_input = input("Enter something to write into the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
with open("output.txt", "a") as file:
    file.write("This is additional appended data.\n")

# Step 3: Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal content of 'output.txt':")
    print(file.read())
