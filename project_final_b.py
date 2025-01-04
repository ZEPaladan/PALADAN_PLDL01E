import tkinter as tk

from ProjectFinal import employee_reg_gui_design

root = tk.Tk()
root.title("Employee Registration")
root.geometry('740x1000')

design = employee_reg_gui_design(root)

#Call for the designs of the employee registration page to create the GUI
design.heading_design(100, 20, 'EMPLOYEE PERSONAL INFORMATION')

#Design of Frame 1
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

#Desing of Frame 2
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


#Design of Frame 3
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

#Buttons
design.button_design2(500, 120, 'Save', 15, 'cyan')
design.button_design2(620, 120, 'Cancel', 15, 'red2')

root.mainloop()