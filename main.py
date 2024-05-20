import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog

def do_command():
    global command_textbox
    url_val = url_entry.get()
    if not url_val:  # If no URL is provided, default to localhost
        url_val = "localhost"
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"Pinging {url_val}...\n")
    command_textbox.update()

    p = subprocess.Popen(["ping", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results.decode())
    command_textbox.insert(tk.END, cmd_errors.decode())

def mSave():
    filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    if filename:
        with open(filename, mode='w') as file:
            text_to_save = command_textbox.get("1.0", tk.END)
            file.write(text_to_save)

root = tk.Tk()
root.geometry("900x500")
root.title("URL Checker")

frame_URL = tk.Frame(root, pady=10, bg="pink1")
frame_URL.pack()

url_label = tk.Label(frame_URL, text="ENTER URL NOW!: ", compound="center", font=("comic sans", 14), bd=0, relief=tk.FLAT, cursor="heart", fg="maroon1", bg="hotpink1")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=("comic sans", 14))
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root, bg="pink")
frame.pack()

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

ping_btn = tk.Button(frame, text="CLICK MEEEEEEEEEEEEEE", command=do_command, cursor="heart", fg="deeppink2", bg="thistle1")
ping_btn.pack()

save_btn = tk.Button(frame, text="SAVE ME", command=mSave, cursor="heart", fg="deeppink2", bg="thistle1")
save_btn.pack()

# Create the main application window
"""root = tk.Tk()"""
root.title("")
root.configure(bg="#FF0000")
# Function to execute when the button is clicked
def quit_program():
    root.quit()

# Create a button widget to quit the program
quit_button = tk.Button(root, text="Click to Self Destruct", command=quit_program)
quit_button.pack()  # Place the button in the window
quit_button.configure(fg="deeppink1")



# Function to execute when an option is selected from the dropdown menu
def on_select(value):
    messagebox.showinfo("Selection", f"You selected: {value}")

# Create the main application window
"""root = tk.Tk()"""
root.title("man")
root.geometry("150x30")
root.configure(bg="#FFC0CB")
# Define options for the dropdown menu
options = ["ping", "nslookup", "nmap"]

# Create a Tkinter variable to store the selected option
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set default value

# Create a dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *options, command=on_select)
dropdown.configure(fg="deeppink1")
dropdown.pack()

root.mainloop()

