from tkinter import Label, Entry, Button, Tk, Radiobutton, IntVar, StringVar, Toplevel, Canvas, X
from ldap_server import LdapService
from CA.ca_client import CaClient, handle_cert_local
from chat import *
import time


class SignupPage:

    def Register(self, event=None):
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "" or self.EMAIL.get() == "" or self.UID.get() == "":
            self.error_label.config(
                text="Please complete the required field!", fg="#0F0F0F", bg="#33FF33")

        else:
            # user object
            user_obj = {
                'username': self.USERNAME.get(),
                'password': self.PASSWORD.get(),
                'email': self.EMAIL.get(),
                'gender': self.GENDER.get(),
                'group_id': 500,  # default gid
                'uid': self.UID.get()  # student card
            }
            print(user_obj)
            # instantiate the ldap service
            # ldap_s = LdapService(admin_pwd="<ur_admin_pwd>")
            ldap_s = LdapService(admin_pwd="<ur_admin_pwd>")
            result = ldap_s.register(user_obj)

            if not result:
                # HomeWindow()
                # self.USERNAME.set("")
                # self.PASSWORD.set("")
                # self.EMAIL.set("")
                # self.GENDER.set("")
                # self.UID.set("")

                self.error_label.config(
                    text="Sucess", fg="#33FF33", bg="#336633")

                time.sleep(1)

                # handle certificate
                client = CaClient(self.USERNAME)
                client.connect()
                client.request_cert()
                result = handle_cert_local('CA/client_cert.pem')
                if result:
                    self.HomeWindow()
                else:
                    self.error_label.config(
                        text="Error occured while obtaining SSL certificate", fg="#0F0F0F", bg="#33FF33")

            else:
                self.error_label.config(
                    text=result, fg="#0F0F0F", bg="#33FF33")

    def HomeWindow(self):
        username = self.USERNAME.get()
        self.root.withdraw()
        c = Chatroom()
        c.run(user=username)

    def navigate_to_login(self):
        self.root.withdraw()
        from login import LoginPage
        l = LoginPage()
        l.main()

    def main(self):
        # main frame
        self.root = Tk()
        self.root.geometry('500x450')
        self.root.title("Registration Form")

        # data binding
        self.USERNAME = StringVar(self.root)
        self.EMAIL = StringVar(self.root)
        self.PASSWORD = StringVar(self.root)
        self.GENDER = StringVar(self.root)
        self.UID = StringVar(self.root)

        # Registration form
        label_0 = Label(self.root, text="Registration form",
                        width=20, font=("bold", 20))
        label_0.place(x=90, y=53)

        # FullName label & entry
        label_1 = Label(self.root, text="Username *",
                        width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        entry_1 = Entry(self.root, textvariable=self.USERNAME)
        entry_1.place(x=240, y=130)

        # self.EMAIL label & entry
        label_2 = Label(self.root, text="Email *",
                        width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        entry_2 = Entry(self.root, textvariable=self.EMAIL)
        entry_2.place(x=240, y=180)

        # self.PASSWORD label & entry
        label_2_ = Label(self.root, text="Password *",
                         width=20, font=("bold", 10))
        label_2_.place(x=68, y=230)
        entry_2_ = Entry(self.root, textvariable=self.PASSWORD, show="*")
        entry_2_.place(x=240, y=230)

        # self.GENDER label & radio-box
        label_3 = Label(self.root, text="Gender",
                        width=20, font=("bold", 10))
        label_3.place(x=70, y=280)

        optionMale = Radiobutton(self.root, text="Male", padx=5, variable=self.GENDER,
                                 value=1)
        optionMale.place(x=235, y=280)
        optionFemale = Radiobutton(self.root, text="Female", padx=20,
                                   variable=self.GENDER, value=2)
        optionFemale.place(x=290, y=280)

        # Age label & entry
        label_4 = Label(self.root, text="Student ID *",
                        width=20, font=("bold", 10))
        label_4.place(x=70, y=330)
        entry_3 = Entry(self.root, textvariable=self.UID)
        entry_3.place(x=240, y=330)

        # Error label
        self.error_label = Label(self.root, width=60, font=("bold", 8))
        self.error_label.place(x=65, y=370)

        # Submit button
        btn = Button(self.root, text='Submit', width=20, command=self.Register, bg='brown',
                     fg='white')
        btn.place(x=180, y=400)

        # Login button
        btn_2 = Button(self.root, text='Login', width=10, command=self.navigate_to_login, bg='#0F0F0F',
                       fg='#33FF33', borderwidth=0, font="Verdana 10 underline")
        btn_2.place(x=350, y=400)

        # theme color hacker
        self.root.config(bg="#0F0F0F")
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
        self.error_label.config(bg="#0F0F0F")

        # it is use for display the registration form on the window
        self.root.mainloop()
        print("registration form  seccussfully created...")


# s = SignupPage()
# s.main()
