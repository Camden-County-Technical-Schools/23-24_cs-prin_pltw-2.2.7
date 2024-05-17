# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

window = tk.Tk()

def do_command():
    subprocess.call("ping localhost")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function
blue_frame = tk.Frame(window, bg="orange", width=800, height=800)
blue_frame.pack(side=tk.LEFT, padx=10, pady=10)

#text box 1
entry_blue = tk.Entry(blue_frame)
entry_blue.pack(pady=5)

#drop down
exchange_rates = {
    "nslookup",
    "nmap",
    "man",
    }

currency_var = tk.StringVar()
currency_var.set("Select a tool")
currency_choice = tk.OptionMenu(window, currency_var, *exchange_rates)
currency_choice.pack(padx=10, pady=5)


# button
calculation_button = tk.Button(window, text="Convert", command=do_command)
calculation_button.pack(pady=5)
    
#output box
command_textbox = tksc.ScrolledText(frame, height=5, width=5)
command_textbox.grid(row=10, column=5)







root.mainloop()
