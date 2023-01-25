from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Edited password generator code made in Day5 so that we don't have to type anything from console


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for _ in range(nr_letters)]
    password_list2 = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_list1 + password_list2 + password_list3

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # convert to string like this instead of above loop(more pythonic)
    password_answer = "".join(password_list)

    # print(f"Your password is: {password}")

    # display password_answer in password entry
    password_entry.insert(0, password_answer)

    # using pyperclip to copy text we want to place in clipboard
    pyperclip.copy(password_answer)


# --------------------------------------- SAVE PASSOWRD ----------------------------------- #

def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    if website and password:
        is_ok = messagebox.askokcancel(title=website, message=f"The are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save? ")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Opss", message="Please don't leave any fields empty!")


# --------------------------------------- UI SETUP ----------------------------------- #

window = Tk()
window.title("Password Manager.")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=51)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "paulomg1996@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
