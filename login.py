from tkinter import Label, Entry, Button, Tk, Radiobutton, IntVar, StringVar, Toplevel, Canvas, X
from ldap_server import LdapService
from CA.ca_client import CaClient, handle_cert_local
from chat import *

import time


class LoginPage:

    def Login(self, event=None):

        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            self.error_label.config(
                text="Please complete the required field!", fg="#0F0F0F", bg="#33FF33")
        else:
            ldap_s = LdapService(admin_pwd="<ur_admin_pwd>")
            result = ldap_s.login(username=self.USERNAME.get(),
                                  password=self.PASSWORD.get())
            if not result:
                # self.USERNAME.set("")
                # self.PASSWORD.set("")
                # self.error_label.config(
                #     text="Sucess", fg="#33FF33", bg="#336633")

                client = CaClient(self.USERNAME)
                client.connect()
                client.verify_cert()

                if client.cert_is_ok == "Ok":
                    self.HomeWindow()
                else:
                    self.error_label.config(
                        text="Access denied -- Pirate Alert --", fg="#0F0F0F", bg="#33FF33")

            else:
                self.error_label.config(
                    text=result, fg="#0F0F0F", bg="#33FF33")

    def HomeWindow(self):
        username = self.USERNAME.get()
        self.root.withdraw()
        c = Chatroom()
        c.run(user=username)

    def navigate_to_signup(self):
        from signup import SignupPage
        self.root.withdraw()
        s = SignupPage()
        s.main()

    def main(self):
        # main frame
        self.root = Tk()
        self.root.geometry('500x300')
        self.root.title("Login Form")

        # data binding
        self.USERNAME = StringVar(self.root)
        self.PASSWORD = StringVar(self.root)

        # Login form
        label_0 = Label(self.root, text="LOGIN", width=20, font=("bold", 20))
        label_0.place(x=90, y=30)

        # subtitle text
        sub_label = Label(self.root, text="Discuss your favorite technology with the community!",
                          width=45, font=("bold", 12))
        sub_label.place(x=45, y=65)

        # self.USERNAME label & entry
        label_1 = Label(self.root, text="Username *",
                        width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        entry_1 = Entry(self.root, textvariable=self.USERNAME)
        entry_1.place(x=240, y=130)

        # self.PASSWORD label & entry
        label_2 = Label(self.root, text="Password *",
                        width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        entry_2 = Entry(self.root, textvariable=self.PASSWORD, show="*")
        entry_2.place(x=240, y=180)

        # Submit button
        btn = Button(self.root, text='Connect', width=20, bg='brown',
                     fg='white', command=self.Login)
        btn.place(x=180, y=250)
        btn.bind('<Return>', self.Login)

        # Register button
        btn_2 = Button(self.root, text='Signup', width=10, command=self.navigate_to_signup, bg='#0F0F0F',
                       fg='#33FF33', borderwidth=0, font="Verdana 10 underline")
        btn_2.place(x=350, y=250)

        # Error label
        self.error_label = Label(self.root, width=60, font=("bold", 8))
        self.error_label.place(x=65, y=220)

        # theme color hacker
        self.root.config(bg="#0F0F0F")
        label_0.config(bg="#0F0F0F", fg="#33FF33")
        label_1.config(bg="#0F0F0F", fg="#33FF33")
        sub_label.config(bg="#225522", fg="#33FF33")
        label_2.config(bg="#0F0F0F", fg="#33FF33")
        entry_1.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        entry_2.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        btn.config(bg="#0F0F0F", fg="#FFFFFF",
                   activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.error_label.config(bg="#0F0F0F")

        # it is use for display the registration form on the window
        self.root.resizable(200, 120)
        self.root.mainloop()
        print("login form seccussfully created...")


l = LoginPage()
l.main()
