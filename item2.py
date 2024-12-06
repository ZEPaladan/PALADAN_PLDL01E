#Initialization of employee's name, department, total deduction, gross income, net income, and pag-ibig contribution
employees_name = ""
department = ""
total_deduction = 0
gross_income = 0
net_income = 0
pagibig_contri = 100.00

#input employee's name, department, rate per hour, number of working hours per day, number of days per week, and number of weeks per month
employees_name = str(input("Enter the employee's name: "))
department = str(input("Enter the department: "))
rate_per_hour = float(input("Enter rate per hour: "))
no_of_working_hours_per_day = int(input("Enter the number of working hours per day: "))
no_of_days_per_week = int(input("Enter the number of days per week: "))
no_of_weeks_per_month = int(input("Enter the number of weeks per month: "))

#Computing the gross income
gross_income = no_of_working_hours_per_day * no_of_days_per_week * no_of_weeks_per_month * rate_per_hour

#Determining PhilHealth and SSS contribution
if 0 <= gross_income <= 20000:
    philhealth_contri = 100.00
    sss_contri = 125.75
elif 20001 <= gross_income <= 50000:
    philhealth_contri = 1200.00
    sss_contri = 2200.50
elif 50001 <= gross_income <= 75000:
    philhealth_contri = 6800.00
    sss_contri = 4800.00
else:
    philhealth_contri = 8800.00
    sss_contri = 5800.00

#Computing the Total Deduction
total_deduction = sss_contri + pagibig_contri + philhealth_contri

#Computing the Net Income
net_income = gross_income - total_deduction

#Displaying employee's name, department, computed total deduction, computed gross income, and computed net income
print("----------------------------")
print("Employee's Name: ", employees_name)
print("Department: ", department)
print("Computed Total Deduction: ", total_deduction)
print("Computed Gross Income: ", gross_income)
print("Computed Net Income: ", net_income)
