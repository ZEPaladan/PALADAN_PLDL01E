import tkinter as tk

from ProjectFinal import user_acc_gui_design

root = tk.Tk()
root.title("User Account Information")
root.geometry('860x500')


design = user_acc_gui_design(root)

#Call for the designs of the user account information page to create the GUI
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
