# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="yellow") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="black",
    bg="yellow")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="yellow") # change frame color
frame.pack()

# set up the buttons for ping, nmap, nslookup
radio_var_red = tk.StringVar()

radio_button1_red = tk.Radiobutton(frame, text="ping", variable=radio_var_red, value="ping")
radio_button1_red.pack(pady=5)

radio_button2_red = tk.Radiobutton(frame, text="nmap", variable=radio_var_red, value="nmap")
radio_button2_red.pack(pady=5)

radio_button3_red = tk.Radiobutton(frame, text="nslookup", variable=radio_var_red, value="nslookup")
radio_button3_red.pack(pady=5)

def do_command():
    print("selected: " + radio_var_red.get())
    #subprocess.call("ping localhost")

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="do command", command=do_command)
ping_btn.pack()

root.mainloop()
