# ⚖️ Weight Converter App with Python + Tkinter

This project is a simple desktop application built using Python and Tkinter, designed to convert weight values between kilograms (kgs) and pounds (lbs). Users can input a numeric weight, choose a conversion direction, and get instant results in a user-friendly interface.

---

## 🚀 Features

🧮 Converts between kilograms and pounds (bidirectional) <br>
📥 Input field for entering any weight value <br>
🔘 Radio buttons to select conversion type: kgs ➡ lbs or lbs ➡ kgs <br>
🎯 "Convert" button to execute the calculation <br>
📢 Displays formatted output with units (e.g., "72.60 lbs") <br>
❌ Error handling for invalid (non-numeric) input <br>
🪟 Clean and simple layout using Tkinter widgets <br>
🛠️ Easy to extend with more unit types or conversion logic <br>

---

## 🖥️ Technologies Used

- Python 3.x
- Tkinter (for GUI interface)
- Math module (for π constant and scientific functions like sqrt, tan, cos, and sen)
- PyCharm (recommended IDE)

---

## 📂 Project Structure

- **main.py**: Main application script. Handles both UI layout and logic. Key responsibilities:

🖼️ Builds GUI layout using labels, entries, buttons, and radio buttons <br>

🔁 Uses .config() to dynamically update result text <br>

🧠 Performs conversion logic: kg → lbs and lbs → kg <br>

❌ Handles ValueError when user input is not a number <br>

📏 Uses precise float conversion and formatting for output display <br>

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/WeightConversion.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the calculator app.

`python3 main.py`

---

# 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Calculator/issues).
