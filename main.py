# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded


import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import webbrowser
import random

def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        #url_val = "127.0.0.1"
        url_val = "::1"
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def duck_on_quack():
    global command_textbox
    command_textbox.insert(tk.END, "duck\n")

root = tk.Tk()
root.configure(bg="lightgray")  # Set background color of root window
frame = tk.Frame(root, bg="lightgray")
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100, bg="black", fg="white", font=("Helvetica", 12))
command_textbox.pack()

nslook_btn = tk.Button(frame, text="nslookup", command=lambda:do_command("nslookup"), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
nslook_btn.pack(pady=5)

nmap_btn = tk.Button(frame, text="nmap", command=lambda:do_command("nmap"), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
nmap_btn.pack(pady=5)
# set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=lambda:do_command("ping -c5"), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
ping_btn.pack(pady=5)

quack_btn = tk.Button(frame, text="quack", command=duck_on_quack, bg="mediumpurple3", fg="white", font=("Helvetica", 12))
quack_btn.pack(pady=5)

traceroute_btn = tk.Button(frame, text="traceroute", command=lambda:do_command("traceroute"), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
traceroute_btn.pack(pady=5)


whois_btn = tk.Button(frame, text="whois", command=lambda:do_command("whois"), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
whois_btn.pack(pady=5)







# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10, bg="black")
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("Comic Sans MS", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=("Comic Sans MS", 14), bg="white", fg="black")
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root, bg="black")
frame.pack()

save_btn = tk.Button(frame, text="save", command=lambda:mSave(), bg="mediumpurple3", fg="white", font=("Helvetica", 12))
save_btn.pack(pady=5)

root.mainloop()
