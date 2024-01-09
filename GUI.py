import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((250, 250), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

# Create the main window
root = tk.Tk()
root.title("Image Display GUI")

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Create a button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create an empty input field
input_field = tk.Entry(root)
input_field.pack()

# Create a dummy button
dummy_button = tk.Button(root, text="Dummy Button")
dummy_button.pack()

# Run the application
root.mainloop()
