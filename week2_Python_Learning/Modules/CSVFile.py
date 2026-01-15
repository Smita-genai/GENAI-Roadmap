"""
CSV File operations module.
Demonstrates reading and writing CSV files using the csv standard library module.
Includes functions for writing data to CSV and reading data from CSV files.
"""

import csv


def write_csv(filename, data):
    """
    Write data to a CSV file.
    
    Args:
        filename (str): Path to the CSV file to write
        data (list): List of lists containing rows to write
    """
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def read_csv(filename):
    """
    Read data from a CSV file.
    
    Args:
        filename (str): Path to the CSV file to read
    """
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    # Write CSV File
    data = [
        ['Name', 'Age', 'Location'],
        ['Smith', 25, 'UK&E']
    ]
    write_csv('example.csv', data)
    
    # Read CSV File
    read_csv('example.csv')
