import tkinter as tk
from tkinter import ttk

def convert_weight():
    try:
        weight = float(entry.get())
        if conversion.get() == "kgs_to_lbs":
            result = weight * 2.205
            result_label.config(text=f"{result:.2f} lbs")
        elif conversion.get() == "lbs_to_kgs":
            result = weight / 2.205
            result_label.config(text=f"{result:.2f} kgs")
    except ValueError:
        result_label.config(text="Enter a valid number")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("400x300")
root.resizable(False, False)

#Style
style = ttk.Style()
style.theme_use("clam")

# Title
title_label = ttk.Label(root, text="Weight Converter", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Input Frama
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

# Input field
ttk.Label(input_frame, text="Enter weight:").grid(row=0, column=0, padx=5, pady=5)
entry = ttk.Entry(input_frame, width=15)
entry.grid(row=0, column=1, padx=5, pady=5)

# Options Converter
conversion = tk.StringVar(value="kgs_to_lbs")
radio_frame = ttk.Frame(root)
radio_frame.pack(pady=5)

ttk.Radiobutton(radio_frame, text="kgs_to_lbs", variable=conversion, value="kgs_to_lbs").grid(row=1, column=2, columnspan=2, sticky="w", padx=10)
ttk.Radiobutton(radio_frame, text="lbs_to_kgs", variable=conversion, value="lbs_to_kgs").grid(row=2, column=2, columnspan=2, sticky="w", padx=10)

# Button Frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Convert button
convert_button = ttk.Button(button_frame, text="Convert", command=convert_weight)
convert_button.grid(row=0, column=0, padx=10)

# Clear button
clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=10)

# Result (use tk.Label for better alignment control)
result_label = tk.Label(button_frame, text="", font=("Arial", 18), anchor="center", bg="white", fg="black", width=20)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


# Run the app
root.mainloop()
