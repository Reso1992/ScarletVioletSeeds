import csv
import json
import tkinter as tk
from tkinter import filedialog

def convert_csv_to_json():
    # Initialize Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog to select CSV file
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not csv_file_path:
        return

    # Open file dialog to select JSON file destination
    json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not json_file_path:
        return

    # Remove specified columns while converting CSV to JSON
    remove_columns = ["EC", "PID", "Height", "Weight", "Scale", "Drops"]

    # Define the new column headers
    new_columns = ["Prefix", "Stars", "Difficulty", "Seed", "Species", "Shiny", "Tera Type", "HP", "Atk", "Def", "SpA", "SpD",
                   "Spe", "Ability", "Nature", "Gender", "Rewards"]

    # Initialize the JSON data
    json_data = []

    # Read CSV file and convert to JSON
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Remove specified columns
            for col in remove_columns:
                row.pop(col, None)

            # Add Prefix, Stars, and Difficulty columns
            row = {"Prefix": "%ra", "Stars": "3", "Difficulty": "6", **row}

            # Append row to JSON data
            json_data.append(row)

    # Write JSON data to file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Conversion completed successfully!")

# Run the conversion function
convert_csv_to_json()
