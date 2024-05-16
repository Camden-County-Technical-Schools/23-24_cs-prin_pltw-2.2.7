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

root.mainloop()

