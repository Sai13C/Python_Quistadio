# Student Information

subjects = ("Python", "Java", "Database")

student = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "course": input("Enter your course: ")
}

print("\n--- Student Information ---")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

print("\n--- Subjects ---")

for subject in subjects:
    print("-", subject)
