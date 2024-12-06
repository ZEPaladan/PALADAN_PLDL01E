class PersonInformation():
    def __init__ (self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def DisplayPersonInformation(self, name, age, address):
        print("==========================================")
        print(f"Hi {name}")
        print(f"You are {age} years old")
        print(f"From {address}")
        print("==========================================")

class SalaryInformation():
    def __init__(self, rate_per_hour, working_hours):
        self.rate_per_hour = rate_per_hour
        self.working_hours = working_hours
        self.salary = 0

    def ComputeSalary(self):
        self.salary = self.rate_per_hour * self.working_hours

    def DisplaySalary(self):
        print("==========================================")
        print(f"Salary: {self.salary: .2f}")
        print("==========================================")