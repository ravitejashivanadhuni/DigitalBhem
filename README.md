# Graphical BMI Calculator

This project is a graphical BMI (Body Mass Index) calculator implemented in Python using the Tkinter library for the GUI and SQLite for data storage.

## Features

- User-friendly GUI to input weight and height.
- Calculates and displays BMI along with the health category.
- Stores BMI records in a SQLite database.
- Displays historical BMI data.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x: [Download Python](https://www.python.org/downloads/)

## Installation

1. Clone this repository or download the `bmi_calculator.py` file.
2. Open a terminal or command prompt and navigate to the directory containing `bmi_calculator.py`.

## Required Libraries

Install the required libraries using pip:

```bash
pip install tkinter sqlite3
```
# Steps to Run Locally
1. Ensure Python is Installed: Download and install Python from the official Python website.
2. Install Required Libraries:
bash
```
pip install tkinter sqlite3
```
3.Save the Script:
Save the simplified advanced graphical BMI calculator code to a file named gui_bmi_calculator.py.
4.Run the Script:
On Windows: Double-click the gui_bmi_calculator.py file or run it from Command Prompt.
On macOS/Linux: Open a terminal, navigate to the directory containing gui_bmi_calculator.py, and run:
bash
```
python gui_bmi_calculator.py
```
# Usage
1.Enter Weight and Height:

Enter your weight in kilograms in the "Weight (kg)" field.
Enter your height in meters in the "Height (m)" field.

2.Calculate BMI:

Click the "Calculate BMI" button.
Your BMI and health category will be displayed.

3.View History:

Click the "Show History" button to view all previous BMI records stored in the database.
# Code Explanation
## Imports:

tkinter is imported for creating the GUI.
sqlite3 is imported for database operations.
## Database Functions:

create_db(): Creates a SQLite database and a table for storing BMI records if they don't already exist.
insert_data(weight, height, bmi, category): Inserts a new BMI record into the database.
## BMI Calculation and Classification:

calculate_bmi(): Reads user input, calculates BMI, classifies it, updates the result label, and stores the record in the database.
classify_bmi(bmi): Classifies the BMI value into categories such as Underweight, Normal weight, Overweight, and Obesity.
Display History:

show_history(): Fetches and displays historical BMI records in a new window.
## GUI Setup:

The main window is created using tk.Tk().
Widgets (labels, entry fields, buttons) are created and placed using grid layout.
The database is initialized by calling create_db().
The application is run using root.mainloop().
# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# Acknowledgments
Inspired by various BMI calculators and Python GUI tutorials.
Thanks to the Python and Tkinter documentation for the guidance.
