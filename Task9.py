
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}


name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print("Student not found in the record.")
