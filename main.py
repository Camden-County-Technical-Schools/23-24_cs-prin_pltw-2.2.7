# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk

def do_command(combobox, amount_entry, command_textbox):
    # If url_entry is blank, use localhost IP address
    url_val = amount_entry.get()
    if (len(url_val) == 0):
        url_val = "::1"

    # clear the information from the output textbox
    command_textbox.delete(1.0, tk.END)

    # get the command from the combobox
    command = combobox.get()
    if (command == " "):
        command_textbox.insert(tk.END, "Please select a tool!\n")
        # if no command given, exit this function
        return
    else:
        command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    # execute the command
    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #v2

    # display information about the command in the output textbox
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)
    return

def do_save():
    print("Saving ...")
    return

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
        self.from_currency_combobox = ttk.Combobox(root, values=[" ", "ping -c5", "nmap", "nslookup"])
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_combobox.current(0)

        self.result_label = ttk.Label(root, text="Result:", background="dark red", foreground="white")
        self.result_label.grid(row=5, column=0, padx=10, pady=10)

        self.command_textbox = tksc.ScrolledText(root, height=5, width=30)
        self.command_textbox.grid(row=5, column=0)

        self.convert_button = ttk.Button(root, text="GO", command=lambda:do_command(self.from_currency_combobox,
                                        self.amount_entry, self.command_textbox))
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        #self.white_frame = ttk.Label(root, text="Test", background="white") #width=300, height=400)
        #self.white_frame.grid(row=5, column=1, padx=10, pady=10)

        self.file_btn = ttk.Button(root, text="Save to file..", command=lambda:do_save())
        self.file_btn.grid(row=9, column=1, padx=20, pady=10)

        
def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
