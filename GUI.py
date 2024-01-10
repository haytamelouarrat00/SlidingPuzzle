import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk

from slidingpuzzle import split_and_shuffle_image


class SlidingPuzzleSolverGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.file_path = None
        self.photo = None
        self.master = master
        self.master.title("Sliding Puzzle Solver")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Labels and Buttons
        self.image_label = tk.Label(self)
        self.image_label.grid(row=0, column=0, columnspan=3)

        self.button_browse = tk.Button(self, text="Browse", command=self.open_image)
        self.button_browse.grid(row=1, column=0)

        self.input_label = tk.Label(self, text="Number of Tiles:")
        self.input_label.grid(row=1, column=1)

        self.input_field = tk.Entry(self)
        self.input_field.grid(row=1, column=2)

        self.button_shuffle = tk.Button(self, text="Shuffle", command=self.shuffle_image)
        self.button_shuffle.grid(row=2, column=0)

        self.button_solve = tk.Button(self, text="Solve", command=self.solve_puzzle)
        self.button_solve.grid(row=2, column=1)

    def open_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            image = Image.open(self.file_path)
            image = image.resize((400, 400), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)

    def shuffle_image(self):
        if hasattr(self, 'photo') and self.input_field.get():
            count = int(self.input_field.get())
            new_image = split_and_shuffle_image(self.file_path, count)  # Get the shuffled image
            self.photo = ImageTk.PhotoImage(new_image)  # Convert it to PhotoImage
            self.image_label.config(image=self.photo)  # Update the displayed image
            self.image_label.image = self.photo

    def solve_puzzle(self):
        # Implement your puzzle solving logic here
        pass


def main():
    root = tk.Tk()
    app = SlidingPuzzleSolverGUI(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
