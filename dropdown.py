import tkinter as tk
from tkinter import messagebox

# Function to execute when an option is selected from the dropdown menu
def on_select(value):
    messagebox.showinfo("Selection", f"You selected: {value}")

# Create the main application window
root = tk.Tk()
root.title("man")
root.geometry("150x30")
# Define options for the dropdown menu
options = ["ping", "nslookup", "nmap"]

# Create a Tkinter variable to store the selected option
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set default value

# Create a dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *options, command=on_select)
dropdown.pack()

# Start the Tkinter event loop
root.mainloop()
