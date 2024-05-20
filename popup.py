import tkinter as tk

def show_popup(event=None):
    # Calculate popup position based on button position
    x = root.winfo_rootx() + button.winfo_x() + button.winfo_width() // 2
    y = root.winfo_rooty() + button.winfo_y() - 50
    
    # Create the popup
    popup = tk.Toplevel(root)
    popup.geometry("+{}+{}".format(x, y))
    
    # Add content to the popup
    popup_label = tk.Label(popup, text="Popup message")
    popup_label.pack(pady=10)
    
    # Make the popup grab the focus
    popup.grab_set()

root = tk.Tk()
root.title("Popup Button Example")
root.geometry("50x75")
# Load an image for the button
button_image = tk.PhotoImage(file="IMG_i.png")
button_image.subsample(7, 7)

# Create a button with the image
button = tk.Button(root, image=button_image, command=show_popup, bd=0)
button.image = button_image  # Keep a reference to the image to prevent it from being garbage collected
button.pack(pady=20)

root.mainloop()
