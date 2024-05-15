# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk


def do_command():
    subprocess.call("ping localhost")

# set up button to run the do_command function

#################################################################################################################


class CurrencyConverter:
    def __init__(self, root):
        self.root = root

        self.root.title("Currency Converter")

        # Set window size and position it in the center of the screen
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = int((screen_width - window_width) / 2)
        y_coordinate = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Set background color to dark red
        self.root.configure(bg="dark red")

        

        # Create labels, entry, and comboboxes
        self.amount_label = ttk.Label(root, text="Input Text:", background="dark red", foreground="white")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = ttk.Label(root, text="Select a tool to use:", background="dark red", foreground="white")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_currency_combobox = ttk.Combobox(root, values=[" ", "ping", "nmap", "nslookup"])
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_combobox.current(0)

        self.convert_button = ttk.Button(root, text="GO", command=do_command)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.white_frame = ttk.Label(root, text="Test", background="white") #,width=300, height=400)
        self.white_frame.grid(row=5, column=1, padx=10, pady=10)


        self.file_btn = ttk.Button(root, text="Save to file..", command=do_command)
        self.file_btn.grid(row=6, column=1, padx=10, pady=10)

        
def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()


################################################################################



#root.mainloop()
