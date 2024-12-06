class PersonInformation:
    def __init__(self):
        # Input for Person Information
        self.person_name = input("Full Name: ")
        self.street_address = input("Street Address: ")
        self.barangay = input("Barangay: ")
        self.city_address = input("City Address: ")
        self.province = input("Province: ")
        self.balance_previous = float(input("Balance from the previous billing: "))
        self.rate_per_kwh = float(input("Rate per KWH: "))

        # Input for Service info
        self.service_id_number = int(input("Service ID Number: "))
        self.rate = input("Rate: ")

        # Input for the billing info
        self.bill_date = input("Bill Date: ")
        self.meter_reading_date = input("Meter Reading Date: ")
        self.bill_period = input("Bill Period: ")
        self.due_date = input("Due Date: ")
        self.total_kwh = float(input("Total KWH: "))
        self.next_meter_reading = input("Next Meter Reading: ")

        # Bill Computation Summary
        self.generation = float(input("Generation: "))
        self.transmission = float(input("Transmission: "))
        self.system_loss = float(input("System Loss: "))
        self.distribution = float(input("Distribution (Meralco): "))
        self.subsidies = float(input("Subsidies: "))
        self.government_taxes = float(input("Government Taxes: "))
        self.universal_charges = float(input("Universal Charges: "))
        self.fit_an = float(input("FiT-AN (Renewable): "))
        self.applied_credits = float(input("Applied Credits: "))
        self.other_charges = float(input("Other Charges: "))
        self.installment_due = float(input("Installment Due: "))

        # Initialize the remarks attribute
        self.remarks = ""
        self.compute_balance_and_remarks()

    def compute_balance_and_remarks(self):
        # Set remarks based on previous balance
        if self.balance_previous == 0:
            self.remarks = "Thank You"
        else:
            self.remarks = "Please pay the previous balance"

    def computation(self):
        # Formulas
        self.amount_due = self.rate_per_kwh * self.total_kwh
        self.billing_period = (self.generation + self.transmission + self.system_loss + self.distribution +
                               self.subsidies + self.government_taxes + self.universal_charges + self.fit_an +
                               self.applied_credits + self.other_charges + self.installment_due)
        self.total_current_amount = self.balance_previous + self.amount_due
        self.total_amount_due = self.balance_previous + self.billing_period