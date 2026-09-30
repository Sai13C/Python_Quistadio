# Student Information Dictionary

student = {}

student["name"] = input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["course"] = input("Enter your course: ")
student["section"] = input("Enter your section: ")

print("\n--- Student Information ---")

for key, value in student.items():
    print(key.capitalize(), ":", value)
