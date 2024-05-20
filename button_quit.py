import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("")

# Function to execute when the button is clicked
def quit_program():
    root.quit()

# Create a button widget to quit the program
quit_button = tk.Button(root, text="Click to Self Destruct", command=quit_program)
quit_button.pack()  # Place the button in the window

# Start the Tkinter event loop
root.mainloop()
