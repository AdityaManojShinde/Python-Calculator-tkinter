import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create the main window
root = tk.Tk()
root.title("Excel to Web Form By Aditya.m.s")
root.geometry("220x210")

logo_image = tk.PhotoImage(file="images/logo.png")

# Set the window icon to the logo image
root.wm_iconphoto(True, logo_image)

# Function to select an Excel file
# Create a text box widget to display the input and output
textbox = tk.Entry(root, width=30)
textbox.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Define a function to add a character to the text box
def add_character(character):
    current_text = textbox.get()
    textbox.delete(0, tk.END)
    textbox.insert(0, current_text + character)

# Define a function to clear the text box
def clear():
    textbox.delete(0, tk.END)

# Define a function to calculate the result
def calculate():
    try:
        result = eval(textbox.get())
        textbox.delete(0, tk.END)
        textbox.insert(0, result)
    except:
        textbox.delete(0, tk.END)
        textbox.insert(0, "Error")

# Create buttons for each digit and operator
button_1 = tk.Button(root, text="1", width=5, command=lambda: add_character("1"))
button_2 = tk.Button(root, text="2", width=5, command=lambda: add_character("2"))
button_3 = tk.Button(root, text="3", width=5, command=lambda: add_character("3"))
button_4 = tk.Button(root, text="4", width=5, command=lambda: add_character("4"))
button_5 = tk.Button(root, text="5", width=5, command=lambda: add_character("5"))
button_6 = tk.Button(root, text="6", width=5, command=lambda: add_character("6"))
button_7 = tk.Button(root, text="7", width=5, command=lambda: add_character("7"))
button_8 = tk.Button(root, text="8", width=5, command=lambda: add_character("8"))
button_9 = tk.Button(root, text="9", width=5, command=lambda: add_character("9"))
button_0 = tk.Button(root, text="0", width=5, command=lambda: add_character("0"))
button_decimal = tk.Button(root, text=".", width=5, command=lambda: add_character("."))
button_add = tk.Button(root, text="+", width=5, command=lambda: add_character("+"))
button_subtract = tk.Button(root, text="-", width=5, command=lambda: add_character("-"))
button_multiply = tk.Button(root, text="*", width=5, command=lambda: add_character("*"))
button_divide = tk.Button(root, text="/", width=5, command=lambda: add_character("/"))
button_clear = tk.Button(root, text="Clear", width=12, command=clear)
button_equals = tk.Button(root, text="=", width=12, command=calculate)

# Add the buttons to the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4,column=0)
button_decimal.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_clear.grid(row=5, column=0, columnspan=2)
button_equals.grid(row=5, column=2, columnspan=2)

# Define a function to adjust the button size based on the window size
def resize_buttons(event):
        width = event.width
        height = event


# Start the main loop
root.mainloop()
