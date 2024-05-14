# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    subprocess.call("ping localhost")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()



################################################################Code added from second box in pltw

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()


#####################################################dropdown to select the process wanted
combo = tk.OptionMenu(master= frame, text= "process", variable= "ping", )
combo.pack()

################################################Button code exists by default


# set up button to run the do_command function
proceed_btn = tk.Button(frame, text="proceed", command=do_command)
proceed_btn.pack()



root.mainloop()
