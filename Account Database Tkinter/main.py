from tkinter import *
from datetime import datetime
from csv import *
time = datetime.now()

def login():
    def submit():
        email = username_entry.get()
        password = password_entry.get()
        info = [email,password]
        with open('accountdatabase.csv', 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                if row == info:
                    def actions():
                        def request():
                            def submit():
                                message = message_entry.get()
                                info = [email,message]
                                with open('request.csv', 'a') as file:
                                    writer_object = writer(file)
                                    writer_object.writerow(info)
                                    file.close()
                                    complete_register = Label(request, text="Your request has been sent!")
                                    complete_register.grid(row=0,column=1)
                            request = Tk()
                            request.title("Leaf Co. Request")
                            request.geometry("600x600")
                            header = Label(request, text="Leaf Co.")
                            header.grid(row=0,column=0,padx=30,pady=10)
                            message_lab = Label(request, text="Message: ")
                            message_lab.grid(row=1)
                            message_entry = Entry(request, width=30)
                            message_entry.grid(row=1,column=1)
                            submit_btn = Button(request, text="Submit", command=submit)
                            submit_btn.grid(row=2,column=0)
                            request.mainloop()
                        def logout():
                            exit()
                        def remove_account():
                            def yes():
                                info = [email,password]
                                with open("accountdatabase.csv", "r") as file:
                                    lines = file.readlines()
                                with open("accountdatabase.csv", "w") as file:
                                    for line in lines:
                                        if line == info:
                                            file.write("")
                                exit()
                            def no():
                                actions()
                            reaccount = Tk()
                            reaccount.title("Leaf Co. Remove Account")
                            reaccount.geometry("600x600")
                            header = Label(reaccount, text="Leaf Co.")
                            header.grid(row=0)
                            confirm_lab = Label(reaccount, text="Are you sure you want to remove this account? ")
                            confirm_lab.grid(row=1)
                            yes_btn = Button(reaccount, text="Yes, I'm sure", command=yes)
                            yes_btn.grid(row=1,column=1)
                            no_btn = Button(reaccount, text="No, Don't do it", command=no)
                            no_btn.grid(row=1,column=2)
                        actions = Tk()
                        actions.title("Leaf Co. Actions")
                        actions.geometry("600x600")
                        header = Label(actions, text="Leaf Co.")
                        header.grid(row=0,column=0,padx=30,pady=10)
                        action_lab = Label(actions, text="What action do you want to perform?")
                        action_lab.grid(row=0,column=1)
                        request_btn = Button(actions, text="1. Send Request", command=request)
                        request_btn.grid(row=1)
                        logout_btn = Button(actions, text="2. Logout", command=logout)
                        logout_btn.grid(row=2)
                        remove_account_btn = Button(actions, text="3. Remove Account", command=remove_account)
                        remove_account_btn.grid(row=3)
                        actions.mainloop()
                    actions()

    login = Tk()
    login.title("Leaf Co. Login")
    login.geometry("600x600")
    header = Label(login, text="Leaf Co.")
    header.grid(row=0,column=0,padx=30,pady=10)
    user_lab = Label(login, text="Email: ")
    user_lab.grid(row=1,column=0,padx=30,pady=10)
    username_entry = Entry(login, width=30)
    username_entry.grid(row=1,column=1)
    pass_lab = Label(login, text="Password: ")
    pass_lab.grid(row=2,column=0,padx=30,pady=10)
    password_entry = Entry(login, width=30, bg="black")
    password_entry.grid(row=2,column=1)
    submit_btn = Button(login, text="Submit", command=submit)
    submit_btn.grid(row=3,column=0)
    login.mainloop()

def register():
    def submit():
        email = username_entry.get()
        password = password_entry.get()
        password2 = passwordcon_entry.get()
        if password == password2:
            info = [email,password]
            with open('accountdatabase.csv', 'a') as file:
                writer_object = writer(file)
                writer_object.writerow(info)
                file.close()
                complete_register = Label(register, text="Your account has been created!")
                complete_register.grid(row=0,column=1)
    register = Tk()
    register.title("Leaf Co. Register")
    register.geometry("600x600")
    header = Label(register, text="Leaf Co.")
    header.grid(row=0,column=0,padx=30,pady=10)
    user_lab = Label(register, text="Email: ")
    user_lab.grid(row=1,column=0,padx=30,pady=10)
    username_entry = Entry(register, width=30)
    username_entry.grid(row=1,column=1)
    pass_lab = Label(register, text="Password: ")
    pass_lab.grid(row=2,column=0,padx=30,pady=10)
    password_entry = Entry(register, width=30, bg="black")
    password_entry.grid(row=2,column=1)
    passcon_lab = Label(register, text="Confirm Password: ")
    passcon_lab.grid(row=3,column=0,padx=30,pady=10)
    passwordcon_entry = Entry(register, width=30, bg="black")
    passwordcon_entry.grid(row=3,column=1)
    submit_btn = Button(register, text="Submit", command=submit)
    submit_btn.grid(row=4,column=0)
    register.mainloop()

def home():
    home = Tk()
    home.title("Leaf Co.")
    home.geometry("600x600")
    header = Label(home, text="Leaf Co.")
    header.grid(row=0,column=0,padx=30,pady=10)
    login_btn = Button(home, text="Login", command=login)
    login_btn.grid(row=0,column=1, padx=10)
    register_btn = Button(home, text="Register", command=register)
    register_btn.grid(row=0,column=2, padx=10)
    home.mainloop()



home()
