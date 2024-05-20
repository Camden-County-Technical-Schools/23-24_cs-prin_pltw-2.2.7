# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename



root = tk.Tk()
frame = tk.Frame(root)
frame.grid()



################################################################Code added from second box in pltw

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.grid(row=0, column= 1)

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

#frame = tk.Frame(root,  bg="black") # change frame color
#frame.pack()


#####################################################checkboxes to select the process wanted


#default off values
ping_selected = IntVar()
nmap_selected = IntVar()
nslookup_selected = IntVar()

#checkboxes themselves
#ping
ping_check = tk.Checkbutton(frame, text='ping',variable=ping_selected, onvalue=1, offvalue=0)
ping_check.grid(row=4,column=1)

#nmap
nmap_check = tk.Checkbutton(frame, text='nmap',variable=nmap_selected, onvalue=3, offvalue=2)
nmap_check.grid(row=5,column=1)
#nslookup
nslookup_check = tk.Checkbutton(frame, text='nslookup',variable=nslookup_selected, onvalue=5, offvalue=4)
nslookup_check.grid(row=6,column=1)


######################################################code for doing the selected command.
def do_command():
    command = "Errrmmm what the sigma.  chat is this real?"
    if ping_selected.get() == 1:
        command="ping -c5"

    T.delete(1.0, tk.END)
    T.insert(tk.END, command + " working....\n")
    T.update()

    p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #v2

    cmd_results, cmd_errors = p.communicate()
    T.insert(tk.END, cmd_results)
    T.insert(tk.END, cmd_errors)
#####################################################Button code exists by default


# set up button to run the do_command function
proceed_btn = tk.Button(frame, text="proceed", command=do_command)
proceed_btn.grid(row=7,column=1)

##################################################Text widget where output will go
# Create text widget and specify size.
global T
T = tksc.ScrolledText(frame, height = 10, width = 40)

T.grid(row=5,column=0)

T.insert(tk.END, "output")


root.mainloop()
