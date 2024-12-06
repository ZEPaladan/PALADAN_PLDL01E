
from MIdtermExam import ServiceInformation, MeteringInformation, BillingSummaryInformation

contract_account_number = int(input("Input your Contract Account Number (CAN): "))
name = input("Input your name: ")
service_address = input("Input Service Address: ")
tin = input("Input TIN: ")
rate_class = input("Input Rate Class: ")
business_area = input("Input Business Area: ")

reading_date = input("Input Reading Date (MM/DD/YYYY): ")
present_reading = input("Input Present Reading: ")
previous_reading = input("Input Previous Reading: ")
consumption = int(input("Input Consumption: "))

billing_period = input("Input Billing Period: ")
payment_due_date = input("Input Payment Due Date: ")

service_information = ServiceInformation(contract_account_number, name, service_address, tin, rate_class, business_area)
metering_information = MeteringInformation(reading_date, present_reading, previous_reading, consumption)
billing_summary_information = BillingSummaryInformation(billing_period, reading_date, payment_due_date, consumption)

billing_summary_information.BillingSummaryComputation()

service_information.DisplayServiceInformation(contract_account_number, name, service_address, tin, rate_class, business_area)
metering_information.DisplayMeteringInformation(reading_date, present_reading, previous_reading, consumption)
billing_summary_information.DisplayBillingSummaryInformation(billing_period, reading_date, payment_due_date, consumption)
