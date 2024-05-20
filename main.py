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
    fg="black",
    bg="yellow")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="yellow") # change frame color
frame.pack()

def do_command(command):
    global command_textbox, url_entry
    
     # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    # use url_val
    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

ping_btn = tk.Button(frame, text="ping", command=lambda:do_command("ping -c5"))
ping_btn.pack()

nmap_btn = tk.Button(frame, text="nmap", command=lambda:do_command("nmap"))
nmap_btn.pack()

nslookup_btn = tk.Button(frame, text="nslookup", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

# save function

def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

save_btn = tk.Button(frame, text="SAVE", command=lambda:mSave())
save_btn.pack()

root.mainloop()
