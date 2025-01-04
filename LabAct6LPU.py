import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("LPU Assessment Form")
root.geometry('750x900')

#Creating of functions for the widgets
class gui_design ():
    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Arial', 12, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=22, height=0, fg='black', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=10, height=0, fg='black', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=8, height=0, fg='black', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=10, height=0, fg='black', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=30, height=0, fg='black', font=('Arial', 10))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#f0f0f0', font=('Arial', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='#f0f0f0', font=('Arial', 10))
        self.lbl.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#f0f0f0', font=('Arial', 8, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='#f0f0f0', font=('Arial', 8))
        self.lbl.place(x=x, y=y)

    def label_design5(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='#f0f0f0', font=('Arial', 9, 'bold'))
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

#Calling of functions for the design
design.label_design(550, 30, 'OFFICE OF THE REGISTRAR')
design.image_design("C:\\Users\\NewPC\\Downloads\\lpubg4.png", 20, -30, 200, 200)
design.heading_design(255, 100, 'CERTIFICATE OF ENROLMENT')
design.label_design2(295, 120, '1st Semester, 2024-2025')
design.label_design2(20, 150, 'NAME:')
design.textbox_design(100, 150)
design.label_design2(20, 180, 'COURSE:')
design.textbox_design(100, 180)
design.label_design2(450, 150, 'STUDENT NO:')
design.textbox_design(570, 150)
design.label_design2(450, 180, 'ACAD. YEAR:')
design.textbox_design(570, 180)
design.label_design2(20, 220, 'SECTION')
design.label_design2(200, 220, 'SUBJECT')
design.label_design2(380, 220, 'UNITS')
design.label_design2(520, 220, 'ASSESSMENT OF FEES')
design.textbox_design2(20, 250)
design.textbox_design2(20, 280)
design.textbox_design2(20, 310)
design.textbox_design2(20, 340)
design.textbox_design2(20, 370)
design.textbox_design3(120, 250)
design.textbox_design3(120, 280)
design.textbox_design3(120, 310)
design.textbox_design3(120, 340)
design.textbox_design3(120, 370)
design.textbox_design4(370, 250)
design.textbox_design4(370, 280)
design.textbox_design4(370, 310)
design.textbox_design4(370, 340)
design.textbox_design4(370, 370)
design.textbox_design4(370, 400)
design.label_design(290, 400, 'Total Units:')
design.label_design3(520, 250, 'Tuition Fee Lecture')
design.label_design3(520, 270, 'Athletic')
design.label_design3(520, 290, 'Audio-Visual Library')
design.label_design3(520, 310, 'AUSG')
design.label_design3(520, 330, 'Cultural Fee')
design.label_design3(520, 350, 'Energy Cost')
design.label_design3(520, 370, 'Guidance')
design.label_design3(520, 390, 'Insurance Fee')
design.label_design3(520, 410, 'Learning Management System')
design.label_design3(520, 430, 'Library Fee')
design.label_design3(520, 450, 'Medical and Dental')
design.label_design3(520, 470, 'Registration')
design.label_design3(520, 490, 'RSO')
design.label_design3(520, 510, 'Student Activities Fee')
design.label_design3(520, 530, 'Student Nurturance Fee')
design.label_design3(520, 550, 'Technology Fee')
design.label_design3(520, 570, 'Test Papers')
design.textbox_design5(670, 250)
design.label_design3(690, 270, '843.00')
design.label_design3(690, 290, '79.00')
design.label_design3(690, 310, '50.00')
design.label_design3(690, 330, '400.00')
design.label_design3(690, 350, '1,900.00')
design.label_design3(690, 370, '350.00')
design.label_design3(690, 390, '57.00')
design.label_design3(690, 410, '750.00')
design.label_design3(690, 430, '1,454.00')
design.label_design3(690, 450, '500.00')
design.label_design3(690, 470, '226.00')
design.label_design3(690, 490, '50.00')
design.label_design3(690, 510, '250.00')
design.label_design3(690, 530, '345.00')
design.label_design3(690, 550, '316.00')
design.label_design3(690, 570, '100.00')
design.label_design4(520, 590, 'Assessment Amt.:')
design.label_design4(520, 610, 'Downpayment:')
design.label_design4(520, 640, 'Total Due:')
design.textbox_design5(670, 590)
design.textbox_design5(670, 610)
design.textbox_design5(670, 640)
design.label_design3(580, 670, 'Schedule of Payment')
design.label_design3(575, 690, 'of outstanding balance')
design.label_design3(565, 710, 'after downpayment prior to:')
design.label_design4(520, 730, 'PRELIMS')
design.label_design4(520, 750, 'MIDTERMS')
design.label_design4(520, 770, 'FINALS')
design.textbox_design5(670, 730)
design.textbox_design5(670, 750)
design.textbox_design5(670, 770)
design.label_design5(520, 790, 'THIS IS A TEMPORARY ASSESSMENT')
design.label_design5(160, 790, 'NON-SCHOLAR STUDENT')
design.label_design4(200, 770, 'Registrar')
design.textbox_design(155, 750)

root.mainloop()