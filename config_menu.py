import tkinter as tk
from tkinter import ttk, messagebox
import os
import importlib.util
from pet import Pet


class ConfigMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Character Configuration")

        # Set dark theme
        self.set_dark_theme()

        # Create a frame with padding to add margin
        self.frame = ttk.Frame(master, padding="10 10 10 10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Ground level input
        self.ground_level_label = ttk.Label(self.frame, text="Ground Level (pixels, >= -1):")
        self.ground_level_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.ground_level_entry = ttk.Entry(self.frame, validate="key", validatecommand=(self.frame.register(self.validate_integer), '%P'))
        self.ground_level_entry.insert(0, "-1")
        self.ground_level_entry.grid(row=0, column=1, pady=5)

        # Pet size input
        self.pet_size_label = ttk.Label(self.frame, text="Pet Size:")
        self.pet_size_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.pet_size_var = tk.StringVar(value="default")
        self.pet_size_dropdown = ttk.Combobox(self.frame, textvariable=self.pet_size_var, state='readonly')
        self.pet_size_dropdown['values'] = ["default"] + [str(i) for i in range(1, 11)]
        self.pet_size_dropdown.grid(row=1, column=1, pady=5)

        # Character selection
        self.character_label = ttk.Label(self.frame, text="Character:")
        self.character_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.character_var = tk.StringVar()
        self.character_dropdown = ttk.Combobox(self.frame, textvariable=self.character_var, state='readonly')
        self.character_dropdown.grid(row=2, column=1, pady=5)

        # Boolean option for BCI headset
        self.bci_var = tk.BooleanVar()
        self.bci_checkbutton = ttk.Checkbutton(self.frame, text="Use BCI Headset", variable=self.bci_var)
        self.bci_checkbutton.grid(row=3, columnspan=2, pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, columnspan=2, pady=10)

        # Load characters
        self.characters = self.load_characters()
        if not self.characters:
            self.character_dropdown['values'] = ["No characters installed"]
            self.character_var.set("No characters installed")
        else:
            self.character_dropdown['values'] = list(self.characters.keys())
            self.character_var.set(list(self.characters.keys())[0])  # Set the first character as the default selection

    def set_dark_theme(self):
        style = ttk.Style()
        style.theme_use('clam')  # Using 'clam' theme as a base
        style.configure('TFrame', background='#2e2e2e')
        style.configure('TLabel', background='#2e2e2e', foreground='white')
        style.configure('TEntry', fieldbackground='#3e3e3e', foreground='white')
        style.configure('TButton', background='#4e4e4e', foreground='white')
        style.configure('TCombobox', fieldbackground='#3e3e3e', foreground='white', background='#4e4e4e')
        style.map('TCombobox', fieldbackground=[('readonly', '#3e3e3e')])
        style.configure('TCheckbutton', background='#2e2e2e', foreground='white')

    def validate_integer(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        try:
            int_val = int(value_if_allowed)
            return int_val >= -1
        except ValueError:
            return False

    def load_characters(self):
        characters = {}
        characters_dir = 'characters'
        for filename in os.listdir(characters_dir):
            if filename.endswith('.py'):
                file_path = os.path.join(characters_dir, filename)
                spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attr in dir(module):
                    char_dict = getattr(module, attr)
                    if isinstance(char_dict, dict) and "name" in char_dict:
                        characters[char_dict["name"]] = char_dict
        return characters

    def submit(self):
        try:
            if self.character_var.get() == "No characters installed":
                raise ValueError("No characters installed")

            ground_level = int(self.ground_level_entry.get())
            pet_size_str = self.pet_size_var.get()
            pet_size = "Default" if pet_size_str == "default" else int(pet_size_str)
            character_name = self.character_var.get()
            use_bci_headset = self.bci_var.get()

            if character_name not in self.characters:
                raise ValueError("Invalid character selected")

            character = self.characters[character_name]
            self.master.destroy()  # Close the window after submission
            pet = Pet(pet_size, ground_level, character, use_bci_headset)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfigMenu(root)
    root.mainloop()
