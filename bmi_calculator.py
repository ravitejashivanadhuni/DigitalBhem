import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_db():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi
                 (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def insert_data(weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO bmi (weight, height, bmi, category, date) VALUES (?, ?, ?, ?, datetime('now'))",
              (weight, height, bmi, category))
    conn.commit()
    conn.close()

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
        label_result.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
        insert_data(weight, height, bmi, category)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def show_history():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bmi")
    rows = c.fetchall()
    history_window = tk.Toplevel()
    history_window.title("BMI History")
    text = tk.Text(history_window)
    text.pack()
    for row in rows:
        text.insert(tk.END, f"Weight: {row[1]} kg, Height: {row[2]} m, BMI: {row[3]:.2f}, Category: {row[4]}, Date: {row[5]}\n")
    conn.close()

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
tk.Label(root, text="Weight (kg)").grid(row=0)
tk.Label(root, text="Height (m)").grid(row=1)

entry_weight = tk.Entry(root)
entry_height = tk.Entry(root)
entry_weight.grid(row=0, column=1)
entry_height.grid(row=1, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="Show History", command=show_history).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Your BMI will be displayed here.")
label_result.grid(row=4, column=0, columnspan=2)

# Initialize database
create_db()

# Run the application
root.mainloop()
