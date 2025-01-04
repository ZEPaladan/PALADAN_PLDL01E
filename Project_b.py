import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Employee Registration")
root.geometry('740x1000')

class GuiDesign:
    def __init__(self, root):
        self.root = root

    def frames(self, x, y):
        self.frame1 = Frame(self.root, width=720, height=160, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def frames2(self, x, y):
        self.frame1 = Frame(self.root, width=720, height=125, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def frames3(self, x, y):
        self.frame1 = Frame(self.root, width=720, height=210, border=0, bg='light gray')
        self.frame1.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.heading = Label(self.root, text=text_value, fg='black', font=('Quicksand', 22, 'bold'))
        self.heading.place(x=x, y=y)

    def heading_design2(self, x, y, text_value):
        self.heading = Label(self.root, text=text_value, fg='black', font=('Arial', 12, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(self.root, width=15, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(self.root, width=10, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y, width_value):
        self.textbox = Text(self.root, width=width_value, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.lbl = Label(self.root, text=text_value, bg='#f0f0f0', font=('Arial', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.lbl = Label(self.root, text=text_value, bg='light gray', font=('Arial', 8))
        self.lbl.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(self.root, image=self.bck_pic)
        self.lbl.image = self.bck_pic
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text_value, width_value, bg_value):
        self.upload_button = Button(self.root, width=width_value, pady=1, text=text_value, bg=bg_value, cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y, text_value, width_value, bg_value):
        self.upload_button = Button(self.root, width=width_value, pady=2, text=text_value, bg=bg_value, fg='black', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def combobox_design(self, x, y, width_value):
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.combobox = ttk.Combobox(self.root, values=options, width=width_value)
        self.combobox.set("--select one--")
        self.combobox.place(x=x, y=y)

    def combobox_design2(self, x, y, width_value):
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.combobox = ttk.Combobox(self.root, values=options, width=width_value)
        self.combobox.set("Filipino")
        self.combobox.place(x=x, y=y)

    def combobox_design3(self, x, y, width_value):
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.combobox = ttk.Combobox(self.root, values=options, width=width_value)
        self.combobox.set("dd/mm/yyyy")
        self.combobox.place(x=x, y=y)


design = GuiDesign(root)

design.heading_design(100, 20, 'EMPLOYEE PERSONAL INFORMATION')
design.frames(10, 150)
design.image_design("C:\\Users\\NewPC\\Downloads\\9a56bf4fb9dfbd75aa0f91b62840f3fa.jpg", 10, 100, 120, 120)
design.button_design(15, 230, 'Choose File', 9, 'white')
design.label_design2(90, 230, 'No file chosen')
design.label_design2(170, 160, 'First Name')
design.textbox_design(170, 180)
design.label_design2(320, 160, 'Middle Name')
design.textbox_design(320, 180)
design.label_design2(470, 160, 'Last Name')
design.textbox_design(470, 180)
design.label_design2(620, 160, 'Suffix')
design.textbox_design2(620, 180)
design.label_design2(170, 230, 'Date of Birth')
design.combobox_design3(170, 250, 20)
design.label_design2(320, 230, 'Gender')
design.combobox_design(320, 250, 20)
design.label_design2(470, 230, 'Nationality')
design.combobox_design2(470, 250, 20)
design.label_design2(620, 230, 'Civil Status')
design.combobox_design(620, 250, 12)

design.frames2(10, 320)
design.label_design2(15, 330, 'Department')
design.textbox_design3(15, 350, 35)
design.label_design2(340, 330, 'Designation')
design.textbox_design3(340, 350, 20)
design.label_design2(530, 330, 'Qualified Dep. Status')
design.combobox_design(530, 350, 28)
design.label_design2(15, 380, 'Employee Status')
design.textbox_design3(15, 400, 40)
design.label_design2(385, 380, 'Paydate')
design.combobox_design3(385, 400, 20)
design.label_design2(535, 380, 'Employee Number')
design.textbox_design3(535, 400, 20)

design.frames2(10, 475)
design.heading_design2(10, 450, 'Contact Info')
design.label_design2(15, 480, 'Contact No.')
design.textbox_design3(15, 500, 33)
design.label_design2(320, 480, 'Email')
design.textbox_design3(320, 500, 44)
design.label_design2(15, 530, 'Other (Social Media)')
design.combobox_design(15, 550, 46)
design.label_design2(320, 530, 'Social Media Account ID/No.')
design.textbox_design3(320, 550, 44)

design.frames3(10, 630)
design.heading_design2(10, 605, 'Address')
design.label_design2(15, 635, 'Address Line 1')
design.textbox_design3(15, 655, 78)
design.label_design2(15, 685, 'Address Line 2')
design.textbox_design3(15, 705, 78)
design.label_design2(15, 735, 'City/Municipality')
design.textbox_design3(15, 755, 38)
design.label_design2(365, 735, 'State/Province')
design.textbox_design3(365, 755, 39)
design.label_design2(15, 785, 'Picture Path')
design.textbox_design3(15, 805, 78)

design.button_design2(500, 120, 'Save', 15, 'cyan')
design.button_design2(620, 120, 'Cancel', 15, 'red2')

root.mainloop()
