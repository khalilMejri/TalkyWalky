from tkinter import Label, Entry, Button, Tk, Radiobutton, IntVar, StringVar, Toplevel, Canvas
from ldap_server import LdapService
import time


def Login(event=None):
    if USERNAME.get() == "" or PASSWORD.get() == "":
        error_label.config(
            text="Please complete the required field!", fg="#0F0F0F", bg="#33FF33")
    else:
        ldap_s = LdapService(admin_pwd="<ur_admin_pwd>")
        result = ldap_s.login(username=USERNAME.get(), password=PASSWORD.get())
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


def Back():
    Home.destroy()
    root.deiconify()


# main frame
root = Tk()
root.geometry('500x300')
root.title("Login Form")

# data binding
USERNAME = StringVar(root)
PASSWORD = StringVar(root)

# Login form
label_0 = Label(root, text="LOGIN", width=20, font=("bold", 20))
label_0.place(x=90, y=30)

# subtitle text
sub_label = Label(root, text="Discuss your favorite technology with the community!",
                  width=45, font=("bold", 12))
sub_label.place(x=45, y=65)

# Username label & entry
label_1 = Label(root, text="Username *", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root, textvariable=USERNAME)
entry_1.place(x=240, y=130)

# Password label & entry
label_2 = Label(root, text="Password *", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root, textvariable=PASSWORD, show="*")
entry_2.place(x=240, y=180)

# Submit button
btn = Button(root, text='Connect', width=20, bg='brown',
             fg='white', command=Login)
btn.place(x=180, y=250)
btn.bind('<Return>', Login)

# Error label
error_label = Label(root, width=60, font=("bold", 8))
error_label.place(x=65, y=220)

# theme color hacker
root.config(bg="#0F0F0F")
label_0.config(bg="#0F0F0F", fg="#33FF33")
label_1.config(bg="#0F0F0F", fg="#33FF33")
sub_label.config(bg="#225522", fg="#33FF33")
label_2.config(bg="#0F0F0F", fg="#33FF33")
entry_1.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
entry_2.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
btn.config(bg="#0F0F0F", fg="#FFFFFF",
           activebackground="#0F0F0F", activeforeground="#FFFFFF")
error_label.config(bg="#0F0F0F")


# it is use for display the registration form on the window
root.resizable(200, 120)
root.mainloop()
print("login form seccussfully created...")
