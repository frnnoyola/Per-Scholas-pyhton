# 1. Create a tuple containing the names of the twelve months
months = (
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
)

# 2. Print the first and last month from the tuple
print(f"First month: {months[0]}")
print(f"Last month: {months[-1]}")
print("-" * 40)

# 3. Attempt to modify the tuple to demonstrate immutability
try:
    months[0] = "NewMonth"
except TypeError as e:
    print(f"Tuples are immutable, error: {e}")
print("-" * 40)

# 4. Create a dictionary of students and their grades
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95
}

# 5. Add a new student and grade, then print the dictionary
students["Ethan"] = 88
print("All students after adding Ethan:")
print(students)
print("-" * 40)

# 6. Update an existing student's grade, then print the entry
students["Bob"] = 90
print(f"Updated Bob's record: Bob: {students['Bob']}")
print("-" * 40)

# 7. Use a loop to print out each student's name and grade formatted
print("Final Grade Roster:")
for name, grade in students.items():
    print(f"{name}: {grade}")
