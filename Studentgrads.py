# Student Grades

student = {
    "name": input("Enter your name: "),
    "course": input("Enter your course: ")
}

grades = []

print("\nEnter your 3 grades:")

for i in range(3):
    grade = input("Enter grade: ")
    grades.append(grade)

student["grades"] = grades

print("\n--- Student Information ---")
print("Name:", student["name"])
print("Course:", student["course"])
print("Grades:")

for grade in student["grades"]:
    print("-", grade)
