#Practuce2

students = { "Ana": 85,
             "Ben": 90,
             "Carlo": 78,
             "Diana": 95,
}

print("STUDENT GRADES")
print("------------------")
print("Ana:", students["Ana"])
print("Ben:", students["Ben"])


#Add new Student
students["Ella"] = 88
print("Ella", students["Ella"])

#Update a student grade
students["Carlo"] = 100
students["Diana"] = 75
print("Carlo:", students["Carlo"])
print("Diana", students["Diana"])

name1 = input("Enter student name: ")
grade1 = int(input("Enter Grade: " ))

students[name1] = grade1

print(students)

print("\nUpdated Student Grades")
print("------------------------")


for name, grade in students.items():
    print(name, ":", grade)
# search for a student
search = input(("\n Enter student name to search: "))
if search in students:
    print(search, "has a grade of", students[search])
else:
    print("Student not found")

    highest = max(students)
    print("Highest blood sugar count:", highest)


    lowest = min(students)
    print("Lowest blood sugar count:", lowest)


    diff = highest - lowest
    print("Difference:", diff)

    average = sum(students) / len(students)
    print("Average:", round(average, 2))

    sorted_value = sorted(students)
    print("Sorted:", sorted_value)






