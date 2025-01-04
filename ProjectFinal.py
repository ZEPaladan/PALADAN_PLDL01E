import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#This class is for methods of the Login Page
class login_page_gui_design ():
    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Quicksand', 16, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', font=('Arial', 12, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#f0f0f0', font=('Arial', 10))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=7, text=text_value, bg=bg_value, fg='black', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

#This class is for methods of the Employee Registration Page
class employee_reg_gui_design ():
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
            self.upload_button = Button(self.root, width=width_value, pady=1, text=text_value, bg=bg_value,
                                        cursor='hand2', border=0)
            self.upload_button.place(x=x, y=y)

        def button_design2(self, x, y, text_value, width_value, bg_value):
            self.upload_button = Button(self.root, width=width_value, pady=2, text=text_value, bg=bg_value, fg='black',
                                        cursor='hand2', border=0)
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

#This class is for methods of the User Account Registration Page
class user_acc_gui_design ():
        def __init__(self, root):
            self.root = root
        def frames(self, x, y):
            self.frame1 = Frame(self.root, width=840, height=235, border=0, bg='light gray')
            self.frame1.place(x=x, y=y)

        def heading_design(self, x, y, text_value):
            self.text_value = text_value
            self.heading = Label(text=text_value, fg='black', font=('Quicksand', 22, 'bold'))
            self.heading.place(x=x, y=y)

        def textbox_design(self, x, y):
            self.textbox = Text(width=15, height=1, fg='black', font=('Arial', 12, 'bold'))
            self.textbox.place(x=x, y=y)

        def textbox_design2(self, x, y):
            self.textbox = Text(width=10, height=1, fg='black', font=('Arial', 12, 'bold'))
            self.textbox.place(x=x, y=y)

        def textbox_design3(self, x, y):
            self.textbox = Text(width=28, height=1, fg='black', font=('Arial', 12, 'bold'))
            self.textbox.place(x=x, y=y)

        def label_design(self, x, y, text_value):
            self.text_value = text_value
            self.lbl = Label(text=text_value, bg='#f0f0f0', font=('Arial', 10, 'bold'))
            self.lbl.place(x=x, y=y)

        def label_design2(self, x, y, text_value):
            self.text_value = text_value
            self.lbl = Label(text=text_value, bg='light gray', font=('Arial', 8))
            self.lbl.place(x=x, y=y)

        def image_design(self, image_location, x, y, length, width):
            self.length = length
            self.width = width
            self.image_location = image_location
            self.image = Image.open(image_location)
            self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
            self.lbl = Label(self.root, image=self.bck_pic)
            self.lbl.place(x=x, y=y)

        def button_design(self, x, y, text_value, width_value, bg_value):
            self.bg_value = bg_value
            self.width_value = width_value
            self.text_value = text_value
            self.upload_button = Button(width=width_value, pady=2, text=text_value, bg=bg_value, cursor='hand2',
                                        border=0)
            self.upload_button.place(x=x, y=y)

        def button_design2(self, x, y, text_value, width_value, bg_value):
            self.bg_value = bg_value
            self.width_value = width_value
            self.text_value = text_value
            self.upload_button = Button(width=width_value, pady=2, text=text_value, bg=bg_value, fg='white',
                                        cursor='hand2', border=0)
            self.upload_button.place(x=x, y=y)

        def combo_field(self, x, y, combo_values):
            self.n = tk.StringVar()
            self.combo_fields = ttk.Combobox(self.root, width=30, textvariable=self.n)
            self.combo_fields['values'] = combo_values
            self.combo_fields.place(x=x, y=y)
            self.combo_fields.current()

#This class is for methods of the Payroll Page
class payroll_gui_design ():
    def __init__(self, root):
        self.root = root
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
        self.lbl = Label(self.root, image=self.bck_pic)
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

