import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Payroll")
root.geometry('630x900')

class gui_design ():
    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Quicksand', 22, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#f0f0f0', font=('Arial', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='gray27', bg='#f0f0f0', font=('Arial', 8))
        self.lbl.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(root, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=7, text=text_value, bg=bg_value, fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=2, text=text_value, bg=bg_value, fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

design = gui_design()
design.heading_design(170, 20, "PALADAN'S PAYROLL")

design.label_design(20, 80, "EMPLOYEE BASIC INFO:")
design.image_design("C:\\Users\\NewPC\\Downloads\\9a56bf4fb9dfbd75aa0f91b62840f3fa.jpg", 25, 100, 160, 160)
design.label_design2(30, 270, 'Employee Number:')
design.textbox_design(150, 270)
design.label_design2(30, 310, 'Search Employee:')
design.button_design(150, 305, "SEARCH", 10, 'red3')
design.label_design2(30, 350, 'Department:')
design.textbox_design(150, 350)
design.label_design(20, 380, "BASIC INCOME:")
design.label_design2(30, 410, 'Rate / Hour:')
design.textbox_design(150, 410)
design.label_design2(30, 440, 'No. of Hours / Cut Off:')
design.textbox_design(150, 440)
design.label_design2(30, 470, 'Income / Cut Off:')
design.textbox_design(150, 470)
design.label_design(20, 500, "OTHER INCOME:")
design.label_design2(30, 530, 'Rate / Hour:')
design.textbox_design(150, 530)
design.label_design2(30, 560, 'No. of Hours / Cut Off:')
design.textbox_design(150, 560)
design.label_design2(30, 590, 'Income / Cut Off:')
design.textbox_design(150, 590)
design.label_design(20, 620, "SUMMARY INCOME:")
design.label_design2(30, 650, 'GROSS INCOME:')
design.textbox_design(150, 650)
design.label_design2(30, 680, 'NET INCOME')
design.textbox_design(150, 680)

design.label_design2(350, 100, 'First Name:')
design.textbox_design(480, 100)
design.label_design2(350, 130, 'Middle Name:')
design.label_design2(350, 160, 'Surname:')
design.textbox_design(480, 130)
design.textbox_design(480, 160)
design.label_design2(350, 190, 'Civil Status:')
design.label_design2(350, 220, 'Qualified Dependents')
design.label_design2(350, 235, 'Status:')
design.textbox_design(480, 190)
design.textbox_design(480, 220)
design.label_design2(350, 265, 'Paydate:')
design.textbox_design(480, 265)
design.label_design2(350, 295, 'Employee Status:')
design.label_design2(350, 325, 'Designation:')
design.textbox_design(480, 295)
design.textbox_design(480, 325)
design.label_design(335, 380, "REGULAR DEDUCTIONS:")
design.label_design2(350, 410, 'SSS Contribution:')
design.label_design2(350, 440, 'PhilHealth Contribution:')
design.label_design2(350, 470, 'Pagibig Contribution:')
design.label_design2(350, 500, 'Income Tax Contribution:')
design.textbox_design(480, 410)
design.textbox_design(480, 440)
design.textbox_design(480, 470)
design.textbox_design(480, 500)
design.label_design(335, 530, "OTHER DEDUCTIONS:")
design.label_design2(350, 560, 'SSS Loan:')
design.label_design2(350, 590, 'Pagibig Loan:')
design.label_design2(350, 620, 'Faculty Savings Deposit:')
design.label_design2(350, 650, 'Faculty Savings Loan:')
design.label_design2(350, 680, 'Salary Loan:')
design.label_design2(350, 710, 'Other Loans:')
design.textbox_design(480, 560)
design.textbox_design(480, 590)
design.textbox_design(480, 620)
design.textbox_design(480, 650)
design.textbox_design(480, 680)
design.textbox_design(480, 710)
design.label_design(335, 740, "DEDUCTION SUMMARY")
design.label_design2(350, 770, 'Total Deductions:')
design.textbox_design(480, 770)
design.button_design2(335, 800, 'GROSS INCOME', 12, 'turquoise1')
design.button_design2(428, 800, 'NET INCOME', 11, 'turquoise1')
design.button_design2(513, 800, 'SAVE', 6, 'turquoise')
design.button_design2(563, 800, 'UPDATE', 7, 'turquoise')
design.button_design2(621, 800, 'NEW', 4, 'gold')

root.mainloop()