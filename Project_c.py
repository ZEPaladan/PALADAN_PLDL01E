import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()
root.title("User Account Information")
root.geometry('860x500')

class gui_design ():
    def __int__(self, frame1):
        frame1 = ''
    def frames(self, x, y):
        self.frame1 = Frame(root, width=840, height=235, border=0, bg='light gray')
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
        self.lbl = Label(root, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=2, text=text_value, bg=bg_value, cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y, text_value, width_value, bg_value):
        self.bg_value = bg_value
        self.width_value = width_value
        self.text_value = text_value
        self.upload_button = Button(width=width_value, pady=2, text=text_value, bg=bg_value, fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def combo_field(self, x, y, combo_values):
        self.n = tk.StringVar()
        self.combo_fields = ttk.Combobox(root, width=30, textvariable=self.n)
        self.combo_fields['values'] = combo_values
        self.combo_fields.place(x=x, y=y)
        self.combo_fields.current()


design = gui_design()

design.heading_design(220, 20, 'USER ACCOUNT INFORMATION')
design.frames(10, 150)
design.image_design("C:\\Users\\NewPC\\Downloads\\9a56bf4fb9dfbd75aa0f91b62840f3fa.jpg", 20, 100, 120, 120)
design.label_design2(170, 160, 'First Name')
design.textbox_design(170, 180)
design.label_design2(320, 160, 'Middle Name')
design.textbox_design(320, 180)
design.label_design2(470, 160, 'Last Name')
design.textbox_design(470, 180)
design.label_design2(620, 160, 'Suffix')
design.textbox_design2(620, 180)
design.label_design2(725, 160, 'Department')
design.textbox_design2(725, 180)
design.label_design2(20, 240, 'Designation')
design.textbox_design3(20, 260)
design.label_design2(280, 240, 'Username')
design.textbox_design3(280, 260)
design.label_design2(540, 240, 'Password')
design.textbox_design3(540, 260)
design.label_design2(20, 290, 'Confirm Password')
design.textbox_design3(20, 310)
design.label_design2(280, 290, 'User Type')
design.textbox_design(280, 310)
design.label_design2(425, 290, 'User Status')
design.textbox_design(425, 310)
design.label_design2(570, 290, 'Employee Number')
design.textbox_design3(570, 310)
design.button_design(20, 350, 'Update', 9, 'deep sky blue')
design.button_design(100, 350, 'Delete', 9, 'gold')
design.button_design(180, 350, 'Cancel', 9, 'white')

root.mainloop()
