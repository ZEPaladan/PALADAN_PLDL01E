import tkinter as tk

root = tk.Tk()
root.title("Login Page")
root.geometry('300x260')

from ProjectFinal import login_page_gui_design

design = login_page_gui_design()

#Call for the designs of the login page to create the GUI
design.heading_design(120, 20, "LOGIN")
design.label_design(10, 80, 'Username')
design.textbox_design(100, 80)
design.label_design(10, 130, 'Password')
design.textbox_design(100, 130)
design.button_design(100, 180, 'Login', 15, 'deep sky blue')

root.mainloop()