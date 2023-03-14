import tkinter as tk
import assets.APIs.client_api as ca

root = tk.Tk()
root.geometry('250x300')


email_lab = tk.Label(root, text='Email:')
email_lab.grid(row=0,column=0)

email_entry = tk.Entry(root)
email_entry.grid(row=0,column=1)

pass_lab = tk.Label(root, text='Password:')
pass_lab.grid(row=1,column=0)

pass_entry = tk.Entry(root)
pass_entry.grid(row=1,column=1)



def submit():
    email = email_entry.get()
    password = pass_entry.get()
    print(f'Email:{email} Password:{password}')
    response = ca.check_database_api('localhost',25565,'check_database',email,password)
    print(response)

submit_button = tk.Button(root, text='Submit', command=submit)
submit_button.grid(row=2)

root.mainloop()