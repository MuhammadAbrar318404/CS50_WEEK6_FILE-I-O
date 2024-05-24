import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access command-line arguments
import csv  # Import the csv module to read and write CSV files

def main():
    filename1, filename2 = check_filename()  # Check and get the filenames from the command-line arguments
    write_2nd_file(filename1, filename2)  # Write the second CSV file based on the first CSV file

def write_2nd_file(filename1, filename2):
    collection_name = []  # Initialize a list to store names from the first CSV file
    collection_house = []  # Initialize a list to store house information from the first CSV file
    separated_row = []  # Initialize a list to store rows with separated first and last names
    if not os.path.isfile(filename1):  # Check if the first file exists
        sys.exit(f"Could not read {filename1} ")  # Exit if the first file does not exist
    else:
        with open(filename1, "r") as file1:  # Open the first CSV file for reading
            reader = csv.DictReader(file1)  # Create a CSV reader object
            for row in reader:  # Iterate through each row in the CSV file
                collection_name.append(row["name"])  # Add the name to the collection
                collection_house.append(row["house"])  # Add the house information to the collection
        for _ in range(len(collection_name)):  # Iterate through each name in the collection
            last_name, first_name = collection_name[_].replace("\"", "").split(",")  # Split the name into first and last names
            separated_row.append([first_name.strip(), last_name.strip(), collection_house[_]])  # Append the separated names to the list
        with open(filename2, "w") as file2:  # Open the second CSV file for writing
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])  # Create a CSV writer object
            writer.writeheader()  # Write the header to the CSV file
            for i in separated_row:  # Iterate through each separated row
                writer.writerow({"first": i[0], "last": i[1], "house": i[2]})  # Write the row to the CSV file

def check_filename():
    if len(sys.argv) < 3:  # Check if there are too few command-line arguments
        sys.exit("Too few command-line arguments")  # Exit with an error message
    elif len(sys.argv) > 3:  # Check if there are too many command-line arguments
        sys.exit("Too many command-line arguments")  # Exit with an error message
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:  # Check if the files are not CSV files
        sys.exit("Not a csv file")  # Exit with an error message
    else:
        return sys.argv[1], sys.argv[2]  # Return the filenames

if __name__ == "__main__":
    main()  # Call the main function to start the program
