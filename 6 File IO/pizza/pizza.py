import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access command-line arguments
import csv  # Import the csv module to read CSV files
from tabulate import tabulate  # Import the tabulate module to create formatted tables

def main():
    filename = check_filename()  # Check and get the filename from the command-line arguments
    print(check_line(filename))  # Read and format the contents of the CSV file

def check_line(filename):
    table = []  # Initialize a list to store rows from the CSV file
    if not os.path.isfile(filename):  # Check if the file exists
        sys.exit(f"{filename} file does not exist")  # Exit if the file does not exist
    else:
        with open(filename, "r") as file:  # Open the CSV file for reading
            reader = csv.reader(file)  # Create a CSV reader object
            for row in reader:  # Iterate through each row in the CSV file
                table.append(row)  # Add the row to the table list
    table = tabulate(table, headers='firstrow', tablefmt='grid')  # Format the table using tabulate
    return table  # Return the formatted table as a string

def check_filename():
    if len(sys.argv) < 2:  # Check if there are too few command-line arguments
        sys.exit("Too few command-line arguments")  # Exit with an error message
    elif len(sys.argv) > 2:  # Check if there are too many command-line arguments
        sys.exit("Too many command-line arguments")  # Exit with an error message
    elif not sys.argv[1].endswith(".csv"):  # Check if the file is not a CSV file
        sys.exit("Not a csv file")  # Exit with an error message
    else:
        return sys.argv[1]  # Return the filename

if __name__ == "__main__":
    main()  # Call the main function to start the program
