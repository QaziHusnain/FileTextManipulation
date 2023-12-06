import os
import re
import tkinter as tk
from tkinter import filedialog


def search_and_replace(directory, search_pattern, replace_pattern):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()

            updated_content = re.sub(search_pattern, replace_pattern, content)

            with open(file_path, 'w') as file:
                file.write(updated_content)


def perform_search_replace():
    directory = directory_var.get()
    search_pattern = search_var.get()
    replace_pattern = replace_var.get()
    search_and_replace(directory, search_pattern, replace_pattern)
    result_label.config(text="Search and replace completed.")


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_var.set(directory)


if __name__ == "__main__":
    # GUI setup
    root = tk.Tk()
    root.title("Text File Manipulation")

    # Directory Entry
    directory_var = tk.StringVar()
    directory_label = tk.Label(root, text="Select Directory:")
    directory_entry = tk.Entry(root, textvariable=directory_var, width=40)
    directory_entry.grid(row=0, column=1, padx=10, pady=10)
    directory_label.grid(row=0, column=0, padx=10, pady=10)

    # Browse Button
    browse_button = tk.Button(root, text="Browse", command=browse_directory)
    browse_button.grid(row=0, column=2, padx=10, pady=10)

    # Search Pattern Entry
    search_var = tk.StringVar()
    search_label = tk.Label(root, text="Search Pattern:")
    search_entry = tk.Entry(root, textvariable=search_var, width=40)
    search_entry.grid(row=1, column=1, padx=10, pady=10)
    search_label.grid(row=1, column=0, padx=10, pady=10)

    # Replace Pattern Entry
    replace_var = tk.StringVar()
    replace_label = tk.Label(root, text="Replace Pattern:")
    replace_entry = tk.Entry(root, textvariable=replace_var, width=40)
    replace_entry.grid(row=2, column=1, padx=10, pady=10)
    replace_label.grid(row=2, column=0, padx=10, pady=10)

    # Search and Replace Button
    search_replace_button = tk.Button(root, text="Search and Replace", command=perform_search_replace)
    search_replace_button.grid(row=3, column=1, pady=20)

    # Result Label
    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=1, pady=10)

    root.mainloop()
