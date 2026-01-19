import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_size(path):
    total_size = 0
    try:
        if os.path.isfile(path):
            return os.path.getsize(path)
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)
    except PermissionError:
        return 0
    return total_size

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def analyze():
    path = folder_path.get()
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Invalid directory")
        return

    output.delete(1.0, tk.END)
    items = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        size = get_size(full_path)
        items.append((item, size))

    items.sort(key=lambda x: x[1], reverse=True)

    for i, (name, size) in enumerate(items[:5], start=1):
        output.insert(tk.END, f"{i}. {name} - {format_size(size)}\n")

def browse():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

root = tk.Tk()
root.title("Disk Usage Analyzer")

folder_path = tk.StringVar()

tk.Label(root, text="Select Folder:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=50).pack()
tk.Button(root, text="Browse", command=browse).pack(pady=5)
tk.Button(root, text="Analyze", command=analyze).pack(pady=5)

output = tk.Text(root, height=10, width=60)
output.pack(pady=10)

root.mainloop()
