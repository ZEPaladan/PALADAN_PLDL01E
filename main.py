from employee import PersonInformation, SalaryInformation

name = input("Input your name: ")
age = input("Input your age: ")
address = input("Input you address: ")

rate_per_hour = float(input("Input your rate per hour: "))
working_hours = float(input("Input your working hours: "))

person_information = PersonInformation(name, age, address)
salary_information = SalaryInformation(rate_per_hour, working_hours)

salary_information.ComputeSalary()

person_information.DisplayPersonInformation(name, age, address)
salary_information.DisplaySalary()
