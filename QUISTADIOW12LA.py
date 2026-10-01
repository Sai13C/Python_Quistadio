quistadio_salary = {
    "A0001": {
        "EmpName": "Siah Falcon",
        "DailyHrs": [8, 9, 8.5, 10, 8],
        "WeeklyBasic": 9000

    },
    "A0002": {
        "EmpName": "Tana Sarabina",
        "DailyHrs": [9, 10, 8, 8, 9],
        "WeeklyBasic": 9000

    },
    "A0003": {
        "EmpName": "Tony Ras Stark",
        "DailyHrs": [7, 8, 9, 9, 10],
        "WeeklyBasic": 9000

    },
    "A0004": {
        "EmpName": "Jana Banono",
        "DailyHrs": [9, 10, 8, 8, 9],
        "WeeklyBasic": 9000

    }
}

quistadio_emp_id = input("Enter Employee ID: ").upper()

if quistadio_emp_id in quistadio_salary:

    quistadio_employee_hours = quistadio_salary[quistadio_emp_id]

    print("Employee ID:", quistadio_emp_id)
    print("Employee Name: ", quistadio_salary[quistadio_emp_id]["EmpName"])
    print("Daily Hours:", end=" ")

    for hours in quistadio_employee_hours["DailyHrs"]:
        print(hours, end=" ")

    # calculation of daily hours
    quistadio_total_hours = sum(quistadio_employee_hours["DailyHrs"])

    quistadio_rate_per_hour = quistadio_employee_hours["WeeklyBasic"] / 40


    #calculate for the overtime
    quistadio_overtime_hours = 0

    for quistadio_hours in quistadio_employee_hours["DailyHrs"]:
        if hours > 8:
            quistadio_overtime_hours += quistadio_hours - 8

    quistadio_overtime_pay = quistadio_overtime_hours * (quistadio_rate_per_hour * 1.5)

    #Calculation for the grosspay

    quistadio_gross_pay = quistadio_employee_hours["WeeklyBasic"] + quistadio_overtime_pay

    print("\nTotal Hours:", quistadio_total_hours)
    print("Overtime Hours:", quistadio_overtime_hours)
    print("Rate Per Hour: ₱", round(quistadio_rate_per_hour, 2))
    print("Overtime Pay: ₱", round(quistadio_overtime_pay, 2))
    print("Gross Pay: ₱", round(quistadio_gross_pay, 2))


else:
    print("EMPLOYEE ID NOT FOUND")

