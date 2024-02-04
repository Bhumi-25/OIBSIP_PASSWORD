import tkinter as tk
from tkinter import StringVar, Checkbutton, IntVar

import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Set the background color to light sky blue
        self.root.configure(bg='#87CEEB')

        self.length_label = tk.Label(root, text="Password Length:", font=("Arial", 12, 'bold'), bg='#87CEEB')
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = StringVar()
        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.use_letters_var = IntVar()
        self.use_numbers_var = IntVar()
        self.use_symbols_var = IntVar()

        self.letters_cb = Checkbutton(root, text="Include Letters", variable=self.use_letters_var, font=("Arial", 12, 'bold'), bg='#87CEEB')
        self.letters_cb.grid(row=1, column=0, columnspan=2, pady=5, sticky="W")

        self.numbers_cb = Checkbutton(root, text="Include Numbers", variable=self.use_numbers_var, font=("Arial", 12, 'bold'), bg='#87CEEB')
        self.numbers_cb.grid(row=2, column=0, columnspan=2, pady=5, sticky="W")

        self.symbols_cb = Checkbutton(root, text="Include Symbols", variable=self.use_symbols_var, font=("Arial", 12, 'bold'), bg='#87CEEB')
        self.symbols_cb.grid(row=3, column=0, columnspan=2, pady=5, sticky="W")

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 12, 'bold'))
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.password_var = StringVar()
        # Set the font to bold and size 20
        self.password_label = tk.Label(root, textvariable=self.password_var, font=("Arial", 20, 'bold'), wraplength=300, bg='#87CEEB')
        self.password_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12, 'bold'))
        self.copy_button.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            use_letters = bool(self.use_letters_var.get())
            use_numbers = bool(self.use_numbers_var.get())
            use_symbols = bool(self.use_symbols_var.get())

            characters = ""
            if use_letters:
                characters += string.ascii_letters
            if use_numbers:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if not characters:
                self.password_var.set("Please select at least one character type.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(f"Generated Password: {password}")

        except ValueError:
            self.password_var.set("Invalid input. Please enter a valid number for password length.")

    def copy_to_clipboard(self):
        password = self.password_var.get().split(": ")[1]
        pyperclip.copy(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
