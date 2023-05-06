# CTI-110
# P4HW2 - Salary Calculator
# Young, Samuel   
# 5-5-23
#


employees = []
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    name = input("Enter employee's name or 'Done' to terminate: ")
    if name.lower() == "done":
        break
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
        total_overtime_pay += overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay

    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    print()
    print("Employee name:", name)
    print()
    print("Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f'{hours_worked:<16.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}')
    print()


    employees.append({
        "name": name,
        "hours_worked": hours_worked,
        "pay_rate": pay_rate,
        "overtime_hours": overtime_hours,
        "overtime_pay": overtime_pay,
        "regular_pay": regular_pay,
        "gross_pay": gross_pay
    })

print()
print("Total number of employees entered:", len(employees))
print("Total amount paid for overtime:", f"${total_overtime_pay:.2f}")
print("Total amount paid for regular hours:", f"${total_regular_pay:.2f}")
print("Total amount paid in gross:", f"${total_gross_pay:.2f}")

