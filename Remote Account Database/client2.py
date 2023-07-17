import customtkinter as tk
import assets.APIs.client_api as ca


tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry('325x300')


email_lab = tk.CTkLabel(root, text='Email:')
email_lab.grid(row=0,column=0)

email_entry = tk.CTkEntry(root)
email_entry.grid(row=0,column=1)

pass_lab = tk.CTkLabel(root, text='Password:')
pass_lab.grid(row=1,column=0)

pass_entry = tk.CTkEntry(root)
pass_entry.grid(row=1,column=1)



def submit():
    email = email_entry.get()
    password = pass_entry.get()
    print(f'Email:{email} Password:{password}')
    response = ca.check_database_api('localhost',25565,'check_database',email,password)
    print(f'Response: {response}')

submit_button = tk.CTkButton(root, text='Submit', command=submit)
submit_button.grid(row=2)

root.mainloop()