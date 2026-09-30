#Weekly Payroll System


print("====================================")
print("             JOB POSITION           ")
print("====================================")
print(" |A| JANITOR              P18,000  ")
print(" |B| CLERK                P22,000  ")
print(" |C| CASHIER              P24,000  ")
print(" |D| MANAGER              P40,000  ")
print("====================================")

name = str(input("Enter your name: "))
job_position = str(input("Enter Your Job Postion: ")).upper()
valid_input = True


match job_position:
    case "A":
        monthly_salary = 20000
        actual_hours = 48

    case "B":
        monthly_salary = 25000
        actual_hours = 48

    case "C":
        monthly_salary = 28000
        actual_hours = 48

    case "D":
        monthly_salary = 45000
        actual_hours = 48

    case _:
        print("Invalid Job Position")


weekly_salary = monthly_salary / 4
allowance = weekly_salary * 0.05
gross_basic_salary = weekly_salary + allowance
hourly_rate = gross_basic_salary / 48
actual_hours_worked = 0
absence_deduction = 0
if actual_hours_worked < 48:
    absent_hours = 48 - actual_hours_worked
    absence_deduction = absent_hours * hourly_rate * 1.10
elif actual_hours_worked > 48:
    overtime_hours = 48 - actual_hours_worked
    overtime_rate = hourly_rate * 1.50
    overtime_pay = overtime_hours * overtime_rate
    net_salary = gross_basic_salary - absence_deduction + overtime_pay
else:
    print("N/A")


print(f'Name: {name}')
print(f'Job Position: {job_position}')
pprint(f' weekly_salary: {weekly_salary}')
print(f'Monthly Salary: {monthly_salary}')
print(f'Overtime Hours: {actual_hours}')
print(f'Overtime Rate: {hourly_rate}')
print(f'Overtime Pay: {overtime_pay}')
print(f'Net Salary: {net_salary}')
print(f'Overtime Hourly Rate: {overtime_rate}')
print(f'Overtime Hourly Pay: {hourly_rate}')

