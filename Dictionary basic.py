  print("\n--- 3. Dictionary Basics ---")
  student = {"name": "Juan", "age": 18, "course": "IT"}
  student["age"] = 19                
  student["city"] = "Davao"         
  del student["course"]               
  print(student)
  print("Name:", student["name"])
  print("Grade (default):", student.get("grade", "N/A"))
