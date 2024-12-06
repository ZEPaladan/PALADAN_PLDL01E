
class ServiceInformation():
    def __init__(self, contract_account_number, name, service_address, tin, rate_class, business_area):
        self.contract_account_number = contract_account_number
        self.account_name = name
        self.service_address = service_address
        self.tin = tin
        self.rate_class = rate_class
        self.business_area = business_area

    def DisplayServiceInformation(self, contract_account_number, name, service_address, tin, rate_class, business_area):
        print("=========================================================")
        print("                         Maynilad Water Services, Inc.")
        print("                         8390 DR A SANTOS AVENUE BF HOMES")
        print("                         PARANAQUE CITY")
        print("                         Vat Reg TIN 005-393-442-0000")
        print("                         SPM No.: ")
        print("                         Machine SN: ")
        print("")
        print("SOA # 00000000003456789012")
        print("")
        print("                 STATEMENT OF ACCOUNT                   ")
        print("             For the Month of: February 2024          ")
        print("")
        print("                 SERVICE INFORMATION                     ")
        print("")
        print(f"Contract Account No.                        {contract_account_number}")
        print(f"Account Name:                               {name}")
        print(f"Service Address:                            {service_address}")
        print(f"TIN:                                        {tin}")
        print(f"Rate Class:                                 {rate_class}")
        print(f"Business Area:                              {business_area}")


class MeteringInformation():
    def __init__(self, reading_date, present_reading, previous_reading, consumption):
        self.reading_date = reading_date
        self.present_reading = present_reading
        self.previous_reading = previous_reading
        self.consumption = consumption

    def DisplayMeteringInformation(self, reading_date, present_reading, previous_reading, consumption):
        print("=========================================================")
        print("                 METERING INFORMATION                     ")
        print("Meter No.                MRU No.                 Seq. No.")
        print("C23_UAT_ISU_B_493        17001394                9,999")
        print(f"Reading Date:                               {reading_date}")
        print(f"Present Reading:                            {present_reading}")
        print(f"Previous Reading:                           {previous_reading}")
        print(f"Consumption (cu. m):                        {consumption}")
        print("=========================================================")
        print("                 BILL & PAYMENT HISTORY                     ")
        print("Desc            Total Amount           OR#            Date")
        print("Description: WB-Water Bill, GD-Guarantee Deposit,        ")
        print("      MISC-Reopening Fee, Connection Fee, Metering Charge")


class BillingSummaryInformation():
    def __init__(self, billing_period, reading_date, payment_due_date, consumption):
        self.billing_period = billing_period
        self.reading_date = reading_date
        self.payment_due_date = payment_due_date
        self.consumption = consumption
        self.total_amount_due = 0
        self.basic_charge = 0
        self.rate_cu = 23.52
        self.environmental_charges = 0
        self.maintenance_service_charge = 1.53
        self.total_charges_before_taxes = 0
        self.government_taxes = 0

    def BillingSummaryComputation(self):
        self.basic_charge = self.rate_cu * self.consumption
        self.environmental_charges = self.basic_charge * 0.2
        self.total_charges_before_taxes = self.basic_charge + self.environmental_charges + self.maintenance_service_charge
        self.government_taxes = self.total_charges_before_taxes * 0.025
        self.total_amount_due = self.total_charges_before_taxes + self.government_taxes

    def DisplayBillingSummaryInformation(self, billing_period, reading_date, payment_due_date, consumption):
        print("=========================================================")
        print("                 BILLING SUMMARY                     ")
        print(f"Billing Period: {billing_period} TO {reading_date}")
        print(f"Current Charges:                                    {self.total_amount_due: .2f}")
        print(f"Basic Charge:                                       {self.basic_charge: .2f}")
        print(f"Environmental Charge (20% of Basic Charge):         {self.environmental_charges: .2f}")
        print(f"Maintenace Service Charge (MSC):                    {self.maintenance_service_charge: .2f}")
        print(f"Total Current Charges Before Taxes:                 {self.total_charges_before_taxes: .2f}")
        print(f"Government Taxes:                                   {self.government_taxes: .2f}")
        print("=========================================================")
        print(f"TOTAL AMOUNT DUE:                                   {self.total_amount_due: .2f}")
        print(f"PAYMENT DUE DATE:                                   {payment_due_date}")
        print("=========================================================")








