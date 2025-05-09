import tkinter as tk

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

# Create main window
root = tk.Tk()
root.title("Weight Converter")

# Input field
tk.Label(root, text="Enter weight:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# Options Converter
conversion = tk.StringVar(value="kgs_to_lbs")
tk.Radiobutton(root, text="kgs_to_lbs", variable=conversion, value="kgs_to_lbs").grid(row=1, column=2, columnspan=2, sticky="w", padx=10)
tk.Radiobutton(root, text="lbs_to_kgs", variable=conversion, value="lbs_to_kgs").grid(row=2, column=2, columnspan=2, sticky="w", padx=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_weight)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()
