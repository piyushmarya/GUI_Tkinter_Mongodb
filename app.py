from tkinter import *
from db import MongoOperations

db_object = MongoOperations()


class GuiLogin:

    def __init__(self):
        self.main_window = Tk()
        self.e1 = Entry(self.main_window)
        self.e2 = Entry(self.main_window)

    def fetch_forgot_pass_form(self, e3, e4, e5, window):
        username = e3.get()
        password = e4.get()
        repass = e5.get()
        if username == "" or password == "" or repass == "":
            print("Enter all Fields")
        elif password != repass:
            print("Entered passwords do not match")
        else:
            db_object.update_data_in_db(username, password)
            window.destroy()

    def forgot_pass_form(self):
        window = Tk()
        e3 = Entry(window)
        e4 = Entry(window)
        e5 = Entry(window)
        window.configure(background='light green')
        window.title("Forgot Password form")
        window.geometry("400x200")
        heading = Label(window, text="Form", bg="light green")
        name = Label(window, text='Username', bg="light green")
        password = Label(window, text='Password', bg="light green")
        repass = Label(window, text="Re Enter Pass", bg="light green")
        submit = Button(window, text='Submit', width=10, fg="Blue",
                        command=lambda: self.fetch_forgot_pass_form(e3, e4, e5, window))

        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        password.grid(row=3, column=0)
        repass.grid(row=4, column=0)
        e3.grid(row=1, column=1, ipadx="50")
        e4.grid(row=3, column=1, ipadx="50")
        e5.grid(row=4, column=1, ipadx="50")
        submit.grid(row=10, column=1, padx=10)
        window.mainloop()

    def fetch_signin_values(self):
        if self.e1.get() == "" or self.e2.get() == "":
            print("Enter Fields")
        elif db_object.fetch_data_from_db(self.e1.get(), self.e2.get()):
            print("Logged in Successfully")
        else:
            print("incorrect username/password")

    def fetch_signup(self, e3, e4, e5, window):
        username = e3.get()
        password = e4.get()
        email = e5.get()
        if username == "" or password == "" or email == "":
            print("Enter Fields")
        elif db_object.dump_data_to_db(username, password, email):
            print("Sign Up successfully")
            window.destroy()
        else:
            print("User already Exists")
            print("Change Username")

    def login_form(self):
        self.main_window.configure(background='light green')
        self.main_window.title("SignIn form")
        self.main_window.geometry("500x300")
        heading = Label(self.main_window, text="Form", bg="light green")
        name = Label(self.main_window, text='Username', bg="light green")
        password = Label(self.main_window, text='Password', bg="light green")
        submit = Button(self.main_window, text='Sign In', width=10, fg="Blue", command=self.fetch_signin_values)
        submit1 = Button(self.main_window, text='Sign Up', width=10, fg="Blue", command=self.signup_form)
        submit2 = Button(self.main_window, text="Forgot Password", fg="blue", command=self.forgot_pass_form)
        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        password.grid(row=3, column=0)
        self.e1.grid(row=1, column=1, ipadx="50")
        self.e2.grid(row=3, column=1, ipadx="50")
        submit.grid(row=10, column=1, padx=10)
        submit1.grid(row=11, column=1)
        submit2.grid(row=14, column=1)
        self.main_window.mainloop()

    def signup_form(self):
        window = Tk()
        e3 = Entry(window)
        e4 = Entry(window)
        e5 = Entry(window)
        window.configure(background='light green')
        window.title("SignUp form")
        window.geometry("800x400")
        heading = Label(window, text="Form", bg="light green")
        name = Label(window, text='Username', bg="light green")
        password = Label(window, text='Password', bg="light green")
        email = Label(window, text='Email', bg="light green")
        submit = Button(window, text='Submit', width=10, fg="Blue",
                        command=lambda: self.fetch_signup(e3, e4, e5, window))
        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        password.grid(row=3, column=0)
        email.grid(row=4, column=0)
        e3.grid(row=1, column=1, ipadx="50")
        e4.grid(row=3, column=1, ipadx="50")
        e5.grid(row=4, column=1, ipadx="50")
        submit.grid(row=10, column=1, padx=10)
        window.mainloop()


if __name__ == "__main__":
    obj = GuiLogin()
    obj.login_form()
