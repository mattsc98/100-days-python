from tkinter import *
from tkinter import messagebox

from password_gen import pass_generator

LOGO_PATH = 'Day 29\\password-manager\\logo.png'
DATA_FILE = 'Day 29\\password-manager\\data.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password = pass_generator()
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    empty = None
    
    if len(website) == 0:
        empty = messagebox.showerror(title=website, message=f'Website field left empty')
    elif len(password) == 0:
        empty = messagebox.showerror(title=website, message=f'Pass field left empty')    
    
    if empty is None:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n{website} \n{password} \nIs it okay to save?')

        if is_ok:    
            with open(DATA_FILE, 'a') as data:
                data.write(f'{website} | {email} | {password}' + "\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
email_input.insert(0, "matt@email.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=gen_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()