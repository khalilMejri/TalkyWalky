from tkinter import Label, Entry, Button, Tk, Radiobutton, IntVar

# main frame
root = Tk()
root.geometry('500x400')
root.title("Registration Form")

# Registration form
label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

# FullName label & entry
label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=240, y=130)

# Email label & entry
label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root)
entry_2.place(x=240, y=180)

# Gender label & radio-box
label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()

optionMale = Radiobutton(root, text="Male", padx=5, variable=var,
                         value=1)
optionMale.place(x=235, y=230)
optionFemale = Radiobutton(root, text="Female", padx=20,
                           variable=var, value=2)
optionFemale.place(x=290, y=230)

# Age label & entry
label_4 = Label(root, text="Age:", width=20, font=("bold", 10))
label_4.place(x=70, y=280)
entry_3 = Entry(root)
entry_3.place(x=240, y=280)

# Submit button
btn = Button(root, text='Submit', width=20, bg='brown',
             fg='white')
btn.place(x=180, y=350)

# theme color hacker
root.config(bg="#0F0F0F")
label_0.config(bg="#0F0F0F", fg="#33FF33")
label_1.config(bg="#0F0F0F", fg="#33FF33")
label_2.config(bg="#0F0F0F", fg="#33FF33")
label_3.config(bg="#0F0F0F", fg="#33FF33")
label_4.config(bg="#0F0F0F", fg="#33FF33")
entry_1.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_3.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_2.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
optionFemale.config(bg="#0F0F0F", fg="#33FF33")
optionMale.config(bg="#0F0F0F", fg="#33FF33")
btn.config(bg="#0F0F0F", fg="#FFFFFF",
           activebackground="#0F0F0F", activeforeground="#FFFFFF")

# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
