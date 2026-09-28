patients = {
    "Rhea": (105, 130, 200),
    "Alex": (100, 140, 150)
}

normal = 120

for key, value in patients.items():
    print("\nPatient:", key)

    for v in value:
        if v > normal:
            print(v, "diabetic")
        else:
            print(v, "Normal")


    highest = max(value)
    print("Highest blood sugar count:", highest)


    lowest = min(value)
    print("Lowest blood sugar count:", lowest)


    diff = highest - lowest
    print("Difference:", diff)

    average = sum(value) / len(value)
    print("Average:", round(average, 2))

    sorted_value = sorted(value)
    print("Sorted:", sorted_value)
