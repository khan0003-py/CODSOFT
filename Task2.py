import tkinter as tk

def click_button(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda b=button: click_button(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter event loop
root.mainloop()
