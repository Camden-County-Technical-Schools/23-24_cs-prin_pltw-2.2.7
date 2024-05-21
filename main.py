# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
# Modify the do_command function:
#   to use the new button as needed
def do_command(command): 
    global command_textbox,url_entry
    url_val = url_entry.get()
    if (len(url_val) == 0):
        url_val = "::1"
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' '+url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)
    command_textbox.update()


root = tk.Tk()
root.title('Web searcher ')
root.geometry("960x540")
frame = tk.Frame(root)
frame.pack()
#bg = PhotoImage(file="Web searcher.png")

# Create a canvas
'''
my_canvas = Canvas (root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)


blue_frame = tk.Frame( bg="green", width=360, height=480)
blue_frame.pack(side=tk.LEFT, padx=50, pady=100)
# set up button to run the do_command function
'''

# creates the frame with label for the text box
frame_URL = tk.Frame(root,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter website ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    fg="mediumpurple3",
    #image= img ,
    bg="black",
      activebackground="gray")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)
ping_btn = tk.Button(frame_URL, text="ping", command=lambda:do_command("ping -c5"))
ping_btn.pack(side=tk.RIGHT)
nmap_btn = tk.Button(frame_URL, text="nmap", command=lambda:do_command("nmap "))
nmap_btn.pack(side=tk.RIGHT)
nslookup_btn = tk.Button(frame_URL, text="nslookup", command=lambda:do_command("nslookup"))
nslookup_btn.pack(side=tk.RIGHT)
frame = tk.Frame(root,  bg="black") # change frame color

frame.pack()
command_textbox = tksc.ScrolledText(frame, height=50, width=100)
command_textbox.pack()
root.mainloop()
# Adds an output box to GUI.

# Makes the command button pass it's name to a function using lambda

