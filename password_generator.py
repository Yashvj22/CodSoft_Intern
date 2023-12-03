''' A password generator is a useful tool that generates strong and random passwords for users. This project aims to create 
a password generator application using Python, allowing users to specify the length and complexity of the password '''

import tkinter as tk
import random
import string
window = tk.Tk()
window.title("Password Generator")
window.geometry('250x300')

def generate_password():
    password = ""
    password_length = int(length_entry.get())
    if uppercase_var.get():
        password += string.ascii_uppercase
    if lowercase_var.get():
        password += string.ascii_lowercase
    if digits_var.get():
        password += string.digits
    if special_chars_var.get():
        password += string.punctuation
    if not (uppercase_var.get() or lowercase_var.get() or digits_var.get() or special_chars_var.get()):
        password_result.config(text="Please select at least one option.")
    else:
        password = ''.join(random.choice(password) for _ in range(password_length))
        password_result.config(text="Generated Password: " + password)
def clear():
    length_entry.delete(0, tk.END)
    uppercase_var.set(False)
    lowercase_var.set(False)
    digits_var.set(False)
    special_chars_var.set(False)
    password_result.config(text="")

length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window, bg="lavender")
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var, selectcolor="yellow" )
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var, selectcolor="yellow" )
lowercase_checkbox.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(window, text="Digits", variable=digits_var, selectcolor="yellow" )
digits_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var, selectcolor="yellow" )
special_chars_checkbox.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg = "skyblue")
generate_button.pack()
clear_button = tk.Button(window, text="Clear", command=clear, bg="red")
clear_button.pack()

password_result = tk.Label(window, text="")
password_result.pack()
window.mainloop()