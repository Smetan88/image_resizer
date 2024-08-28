# image_resizer.py
# Author: Taras Smetaniuk, Nestle
# Created: 28.08.2024
# Description: This script resizes and compresses images in a user-selected folder.
# Version: 1.1

import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import webbrowser

def check_installation(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resize_and_compress_images(input_folder, output_folder, target_size, compression_level, resize=True):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                output_subfolder = os.path.dirname(output_path)
                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)
                with Image.open(input_path) as img:
                    if resize:
                        img.thumbnail(target_size)
                    img.save(output_path, optimize=True, quality=compression_level)

def select_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

def resize_and_compress():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    compression_level = compression_slider.get()
    resize = resize_var.get() == 1  # Check if the resize option is selected
    
    if resize:
        if width_entry.get().strip() and height_entry.get().strip():
            target_width = int(width_entry.get())
            target_height = int(height_entry.get())
            target_size = (target_width, target_height)
        else:
            result_label.config(text="Please enter both width and height or uncheck resize option.")
            return
    else:
        target_size = None  # No resizing

    resize_and_compress_images(input_folder, output_folder, target_size, compression_level, resize)
    result_label.config(text="Process complete!")

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing...")
    check_installation("Pillow")

root = tk.Tk()
root.title("Image Resizer and Compressor")


logo_path = resource_path("logo.png")
try:
    logo = Image.open(logo_path)
    logo = logo.resize((350, 100)) 
    logo = ImageTk.PhotoImage(logo)
    logo_label = ttk.Label(root, image=logo)
    logo_label.grid(row=0, column=0, columnspan=3, pady=10)
except FileNotFoundError:
    print("Logo file not found!")

tk.Label(root, text="Input Folder:").grid(row=1, column=0, sticky="w")
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=select_input_folder).grid(row=1, column=2)

tk.Label(root, text="Output Folder:").grid(row=2, column=0, sticky="w")
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=2, column=2)

tk.Label(root, text="Target Width:").grid(row=3, column=0, sticky="w")
width_entry = tk.Entry(root)
width_entry.grid(row=3, column=1)

tk.Label(root, text="Target Height:").grid(row=4, column=0, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=4, column=1)

resize_var = tk.IntVar(value=1)  
resize_checkbox = tk.Checkbutton(root, text="Resize Images", variable=resize_var)
resize_checkbox.grid(row=5, column=0, columnspan=2, sticky="w")

tk.Label(root, text="Compression Level (1-100):").grid(row=6, column=0, sticky="w")
compression_slider = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
compression_slider.set(85) 
compression_slider.grid(row=6, column=1, columnspan=2, sticky="w")

tk.Label(root, text="(Recommended: 85)").grid(row=7, column=1, sticky="w")

tk.Button(root, text="Resize and Compress", command=resize_and_compress).grid(row=8, column=0, columnspan=3)

result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=3)

github_link = tk.Label(root, text="GitHub Repository", fg="blue", cursor="hand2")
github_link.grid(row=10, column=0, columnspan=3)
github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Smetan88/image_resizer"))

root.mainloop()
