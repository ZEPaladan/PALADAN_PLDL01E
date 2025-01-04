import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Meralco Bill")
root.geometry('900x900')

#Creating functions for the widgets
class gui_design ():
    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Quicksand', 22, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=19, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', font=('Arial', 16, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='gray64', bg='#f0f0f0', font=('Franklin Gothic Medium Cond', 16))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='#f0f0f0', font=('Arial', 8))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='#f0f0f0', font=('Franklin Gothic Medium Cond', 12))
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

#Calling of the functions for the design
design.label_design2(20, 20, 'JUAN DELA CRUZ')
design.label_design2(20, 35, '123 MALIWANAG STREET, BARANGAY KAUNLARAN')
design.label_design2(20, 50, 'STA. LUCIA, MANILA')
design.label_design2(20, 65, 'METRO MANILA')

design.label_design2(20, 90, 'CORINTHIAN EXECUTIVE REGENCY')
design.label_design2(20, 105, 'Meter No.: 123AB456789')
design.label_design2(20, 120, 'Route Seq.: 1234 56 7890')
design.label_design2(160, 120, 'Print Seq.: 12345')

design.label_design(20, 135, 'Your electric bill')
design.label_design2(20, 165, 'Billing Period')
design.label_design2(230, 165, 'Bill Date')
design.textbox_design2(20, 181)
design.textbox_design2(230, 181)
design.label_design2(20, 210, 'Date of Meter Reading')
design.label_design2(20, 260, 'Date of Next Meter Reading')
design.textbox_design2(20, 226)
design.textbox_design2(20, 276)
design.label_design2(20, 310, 'Customer Type')
design.textbox_design2(20, 326)
design.label_design2(20, 360, 'Your rate this month')
design.textbox_design2(20, 376)
design.label_design2(230, 210, 'Electric Meter Number')
design.textbox_design2(230, 226)
design.label_design2(230, 260, 'Current Reading')
design.textbox_design2(230, 276)
design.label_design2(230, 310, 'Previous Reading')
design.textbox_design2(230, 326)
design.label_design2(230, 360, 'Actual Consumption')
design.textbox_design2(230, 376)

design.label_design2(450, 20, 'ESPANA-TUTUBAN BUSINESS CENTER')
design.label_design2(450, 35, 'LUBIRAN STREET BACOOD, STA. MESA')
design.label_design2(450, 50, 'MANILA, 1016 METRO MANILA')
design.label_design2(450, 65, 'TIN 000-101-528-000-VAT')
design.label_design2(450, 105, 'Invoice No.: 1234567890123')

design.label_design2(450, 165, 'Customer Account Number (CAN)')
design.textbox_design2(450, 181)
design.label_design2(830, 165, 'Due Date')
design.textbox_design2(710, 181)
design.label_design2(450, 210, 'Please Pay')
design.textbox_design3(450, 230)


design.label_design3(450, 310, 'Bill Computation Summary')
design.label_design2(450, 340, 'Remaining Balance from the previous bill')
design.textbox_design4(750, 340)
design.label_design2(450, 370, 'Charges for this billing period')
design.label_design2(450, 390, 'Generation')
design.label_design2(450, 410, 'Transmission')
design.label_design2(450, 430, 'System Loss')
design.label_design2(450, 450, 'Distribution (Meralco)')
design.label_design2(450, 470, 'Subsidies')
design.label_design2(450, 490, 'Government Taxes')
design.label_design2(450, 510, 'Universal Charges')
design.label_design2(450, 530, 'FiT-All (Renewable)')
design.label_design2(450, 550, 'Applied Credits')
design.label_design2(450, 570, 'Other Charges')
design.label_design2(450, 590, 'Installment Due')
design.textbox_design4(750, 370)
design.textbox_design4(750, 390)
design.textbox_design4(750, 410)
design.textbox_design4(750, 430)
design.textbox_design4(750, 450)
design.textbox_design4(750, 470)
design.textbox_design4(750, 490)
design.textbox_design4(750, 510)
design.textbox_design4(750, 530)
design.textbox_design4(750, 550)
design.textbox_design4(750, 570)
design.textbox_design4(750, 590)

design.label_design3(450, 630, 'Total Amount Due')
design.textbox_design2(710, 630)

design.image_design("C:\\Users\\NewPC\\Downloads\\meralcobg.png", 750, 20, 120, 120)

root.mainloop()