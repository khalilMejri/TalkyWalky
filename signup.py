from tkinter import Label, Entry, Button, Tk, Radiobutton, IntVar, StringVar, Toplevel, Canvas
from ldap_server import LdapService
import time


def Register(event=None):
    if USERNAME.get() == "" or PASSWORD.get() == "" or EMAIL.get() == "" or UID.get() == "":
        error_label.config(
            text="Please complete the required field!", fg="#0F0F0F", bg="#33FF33")
    else:
        # user object
        user_obj = {
            'username': USERNAME.get(),
            'password': PASSWORD.get(),
            'email': EMAIL.get(),
            'gender': GENDER.get(),
            'group_id': 500,  # default gid
            'uid': UID.get()  # student card
        }

        # instantiate the ldap service
        ldap_s = LdapService(admin_pwd="<ur_admin_pwd>")
        result = ldap_s.register(user_obj)
        if not result:
            # HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            error_label.config(text="Sucess", fg="#33FF33", bg="#336633")

        else:
            error_label.config(text=result, fg="#0F0F0F", bg="#33FF33")


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!",
                     font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)


# main frame
root = Tk()
root.geometry('500x450')
root.title("Registration Form")

# data binding
USERNAME = StringVar(root)
EMAIL = StringVar(root)
PASSWORD = StringVar(root)
GENDER = StringVar(root)
UID = StringVar(root)

# Registration form
label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

# FullName label & entry
label_1 = Label(root, text="Username *", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root, textvariable=USERNAME)
entry_1.place(x=240, y=130)

# Email label & entry
label_2 = Label(root, text="Email *", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root, textvariable=EMAIL)
entry_2.place(x=240, y=180)

# Password label & entry
label_2_ = Label(root, text="Password *", width=20, font=("bold", 10))
label_2_.place(x=68, y=230)
entry_2_ = Entry(root, textvariable=PASSWORD, show="*")
entry_2_.place(x=240, y=230)

# Gender label & radio-box
label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=280)
var = IntVar()

optionMale = Radiobutton(root, text="Male", padx=5, variable=GENDER,
                         value=1)
optionMale.place(x=235, y=280)
optionFemale = Radiobutton(root, text="Female", padx=20,
                           variable=GENDER, value=2)
optionFemale.place(x=290, y=280)

# Age label & entry
label_4 = Label(root, text="Student ID *", width=20, font=("bold", 10))
label_4.place(x=70, y=330)
entry_3 = Entry(root, textvariable=UID)
entry_3.place(x=240, y=330)

# Error label
error_label = Label(root, width=60, font=("bold", 8))
error_label.place(x=65, y=350)

# Submit button
btn = Button(root, text='Submit', width=20, command=Register, bg='brown',
             fg='white')
btn.place(x=180, y=380)

# theme color hacker
root.config(bg="#0F0F0F")
label_0.config(bg="#0F0F0F", fg="#33FF33")
label_1.config(bg="#0F0F0F", fg="#33FF33")
label_2.config(bg="#0F0F0F", fg="#33FF33")
label_2_.config(bg="#0F0F0F", fg="#33FF33")
label_3.config(bg="#0F0F0F", fg="#33FF33")
label_4.config(bg="#0F0F0F", fg="#33FF33")
entry_1.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_3.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_2.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_2_.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
optionFemale.config(bg="#0F0F0F", fg="#33FF33")
optionMale.config(bg="#0F0F0F", fg="#33FF33")
btn.config(bg="#0F0F0F", fg="#FFFFFF",
           activebackground="#0F0F0F", activeforeground="#FFFFFF")
error_label.config(bg="#0F0F0F")

# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
