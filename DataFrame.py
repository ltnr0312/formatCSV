# Databricks notebook source
from conversor import Conversor
import tkinter as tk

# Create a tkinter root window (hidden) for file dialog
root = tk.Tk()
root.withdraw()

# Initialize a Conversor object
conversor_instance = Conversor()

# Load a CSV file using a file dialog
conversor_instance.load_csv()

# Preprocess the CSV based on the provided uri
conversor_instance.preprocess_csv()

# Save the DataFrame as a CSV or Excel file with a custom output name
output_format = "csv"  # Choose between 'csv' or 'excel'
output_filename = "dados/csv_converted.csv"  # Provide the custom output file name

# Call the save_converted method with the chosen format and filename
conversor_instance.save_converted(output_format, output_filename)

# If you want to work with the preprocessed DataFrame, you can still use:
processed_csv = conversor_instance.get_dataframe()
print(processed_csv)