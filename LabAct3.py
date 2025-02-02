#Initialization
company_name = ""
employee_code = 0
employee_name = ""
department = ""
cut_off = 0
basic_pay = 0
overtime = 0
absences = 0
honorarium = 0
tardy = 0
withholding_tax = 0
sss_contribution = 0
hdmf_contribution = 100
philhealth_contribution = 0
deduction = 0
gross_earning = 0
net_pay = 0

#Input
company_name = str(input("Company name: "))
employee_name = str(input("Employee name: "))
employee_code = int(input("Employee code: "))
department = str(input("Department: "))
cut_off = str(input("Salary Date Cut-off: "))
rate_per_hour = float(input("Rate per hour: "))
no_of_hours_per_day = float(input("Number of hours per payday: "))
hours_overtime = float(input("Number of hours overtime per payday: "))
hours_absent = float(input("Number of hours absent per payday: "))
hours_tardy = float(input("NUmber of hours tardy: "))
hours_honorarium = float(input("Number of hours for honorarium: "))

#Calculate
basic_pay = rate_per_hour * no_of_hours_per_day
overtime = hours_overtime * rate_per_hour
absences = hours_absent * rate_per_hour
honorarium = hours_honorarium * rate_per_hour
tardy = hours_tardy * rate_per_hour
gross_earning = basic_pay + overtime + honorarium

#Determining SSS Contribution
if gross_earning > 4250:
    sss_contribution = 180
elif 4250 <= gross_earning <= 4749.99:
    sss_contribution = 202.50
elif 4750 <= gross_earning <= 5249.99:
    sss_contribution = 225.00
elif 5250 <= gross_earning <= 5749.99:
    sss_contribution = 247.50
elif 5750 <= gross_earning <= 6249.99:
    sss_contribution = 270.00
elif 6250 <= gross_earning <= 6749.99:
    sss_contribution = 292.50
elif 6750 <= gross_earning <= 7249.99:
    sss_contribution = 315.00
elif 7250 <= gross_earning <= 7749.99:
    sss_contribution = 337.50
elif 7750 <= gross_earning <= 8249.99:
    sss_contribution = 360.00
elif 8250 <= gross_earning <= 8749.99:
    sss_contribution = 383.50
elif 8750 <= gross_earning <= 9249.99:
    sss_contribution = 405.00
elif 9250 <= gross_earning <= 9749.99:
    sss_contribution = 427.50
elif 9750 <= gross_earning <= 10249.99:
    sss_contribution = 450.00
elif 10250 <= gross_earning <= 10749.99:
    sss_contribution = 472.50
elif 10750 <= gross_earning <= 11249.99:
    sss_contribution = 495.00
elif 11250 <= gross_earning <= 11749.99:
    sss_contribution = 517.50
elif 11750 <= gross_earning <= 12249.99:
    sss_contribution = 540.00
elif 12250 <= gross_earning <= 12749.99:
    sss_contribution = 562.50
elif 12750 <= gross_earning <= 13249.99:
    sss_contribution = 585.00
elif 13250 <= gross_earning <= 13749.99:
    sss_contribution = 607.50
elif 13750 <= gross_earning <= 14249.99:
    sss_contribution = 630.00
elif 14250 <= gross_earning <= 14749.99:
    sss_contribution = 652.50
elif 14750 <= gross_earning <= 15249.99:
    sss_contribution = 675.00
elif 15250 <= gross_earning <= 15749.99:
    sss_contribution = 697.50
elif 15750 <= gross_earning <= 16249.99:
    sss_contribution = 720.00
elif 16250 <= gross_earning <= 16749.99:
    sss_contribution = 742.50
elif 16750 <= gross_earning <= 17249.99:
    sss_contribution = 765.00
elif 17250 <= gross_earning <= 17749.99:
    sss_contribution = 787.50
elif 17750 <= gross_earning <= 18249.99:
    sss_contribution = 810.00
elif 18250 <= gross_earning <= 18749.99:
    sss_contribution = 832.50
elif 18750 <= gross_earning <= 19249.99:
    sss_contribution = 855.00
elif 19250 <= gross_earning <= 19749.99:
    sss_contribution = 877.50
elif 19750 <= gross_earning:
    sss_contribution = 900.00
else:
    sss_contribution = 0

#Determining PhilHealth Contribution
if gross_earning == 10000.00:
    philhealth_contribution = gross_earning * 0.05
elif 10000.01 <= gross_earning <= 99999.99:
    philhealth_contribution = gross_earning * 0.05
elif gross_earning == 100000:
    philhealth_contribution = gross_earning * 0.05
else:
    philhealth_contribution = 0

#Determining Withholding Tax
if gross_earning < 10417:
    withholding_tax = 0.00
elif 10417 <= gross_earning <= 16666:
    withholding_tax = (0.00 + 0.05) / 10417
elif 16667 <= gross_earning <= 33332:
    withholding_tax = (937.50 + 0.2) / 16667
elif 33333 <= gross_earning <= 83332:
    withholding_tax = (4270.20 + 0.25) / 33333
elif 83333 <= gross_earning <= 333332:
    withholding_tax = (16770.70 + 0.3) / 83333
else:
    withholding_tax = (91770.70 + 0.35) / 333333

#Calculate Deductions
deduction = absences + tardy + withholding_tax + sss_contribution + philhealth_contribution + hdmf_contribution

#Calculate Net Pay
net_pay = gross_earning - deduction

#Display
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Company Name: ", company_name)
print("Employee Name: ", employee_name)
print("Employee Code: ", employee_code)
print("Cut-off: ", cut_off)
print("Pay period: ", cut_off)
print("Basic Pay: ", basic_pay)
print("Overtime Pay: ", overtime)
print("Absences: ", absences)
print("Honorarium: ", honorarium)
print("Tardy: ", tardy)
print("Withholding Tax: ", withholding_tax)
print("SSS Contribution: ", sss_contribution)
print("PhilHealth Contribution: ", philhealth_contribution)
print("HDMF Contribution: ", hdmf_contribution)
print("Deductions: ", deduction)
print("Gross Earnings: ", gross_earning)
print("Net Pay: ", net_pay)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")