import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access command-line arguments

def main():
    filename = check_filename()  # Check and get the filename from the command-line arguments
    print(check_line(filename))  # Count and print the number of lines in the file that are not comments or empty

def check_line(filename):
    linecounter = 0  # Initialize a counter for lines that are not comments or empty
    if not os.path.isfile(filename):  # Check if the file exists
        sys.exit(f"{filename} file does not exist")  # Exit if the file does not exist
    else:
        with open(filename, "r") as file:  # Open the file for reading
            for line in file:  # Iterate through each line in the file
                line = line.lstrip()  # Remove leading whitespace
                if line.startswith("#") or line.strip() == "":  # Check if the line is a comment or empty
                    pass  # Ignore comments and empty lines
                else:
                    linecounter += 1  # Increment the counter for valid lines
    return linecounter  # Return the count of valid lines

def check_filename():
    if len(sys.argv) < 2:  # Check if there are too few command-line arguments
        sys.exit("Too few command-line arguments")  # Exit with an error message
    elif len(sys.argv) > 2:  # Check if there are too many command-line arguments
        sys.exit("Too many command-line arguments")  # Exit with an error message
    elif not sys.argv[1].endswith(".py"):  # Check if the file is not a Python file
        sys.exit("Not a python file")  # Exit with an error message
    else:
        return sys.argv[1]  # Return the filename

if __name__ == "__main__":
    main()  # Call the main function to start the program
