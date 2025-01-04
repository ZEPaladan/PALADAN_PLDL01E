import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Login Page")
root.geometry('300x260')

class gui_design ():
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


design = gui_design()
design.heading_design(120, 20, "LOGIN")
design.label_design(10, 80, 'Username')
design.textbox_design(100, 80)
design.label_design(10, 130, 'Password')
design.textbox_design(100, 130)
design.button_design(100, 180, 'Login', 15, 'deep sky blue')

root.mainloop()