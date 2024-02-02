import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(entry_length.get())
    include_uppercase = var_uppercase.get()
    include_lowercase = var_lowercase.get()
    include_numbers = var_numbers.get()
    include_symbols = var_symbols.get()

    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        result_var.set("Please select at least one option.")
    else:
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(generated_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_length = ttk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=5, pady=5)

entry_length = ttk.Entry(root)
entry_length.grid(row=0, column=1, padx=5, pady=5)

var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

check_uppercase = ttk.Checkbutton(root, text="Uppercase Letters", variable=var_uppercase)
check_uppercase.grid(row=1, column=0, columnspan=2, pady=5, sticky='w')

check_lowercase = ttk.Checkbutton(root, text="Lowercase Letters", variable=var_lowercase)
check_lowercase.grid(row=2, column=0, columnspan=2, pady=5, sticky='w')

check_numbers = ttk.Checkbutton(root, text="Numbers", variable=var_numbers)
check_numbers.grid(row=3, column=0, columnspan=2, pady=5, sticky='w')

check_symbols = ttk.Checkbutton(root, text="Symbols", variable=var_symbols)
check_symbols.grid(row=4, column=0, columnspan=2, pady=5, sticky='w')

btn_generate = ttk.Button(root, text="Generate Password", command=generate_password)
btn_generate.grid(row=5, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_var, font=('Arial', 12))
label_result.grid(row=6, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()