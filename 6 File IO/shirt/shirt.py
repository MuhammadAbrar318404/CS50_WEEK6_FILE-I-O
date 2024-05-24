import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access command-line arguments
from PIL import Image, ImageOps  # Import the Image and ImageOps modules from the PIL library

def main():
    filename1, filename2 = check_filename()  # Check and get the filenames from the command-line arguments
    new_image(filename1, filename2)  # Create a new image based on the input image and shirt image

def new_image(filename1, filename2):
    if not os.path.isfile(filename1):  # Check if the input image file exists
        sys.exit(f"Could not read {filename1} ")  # Exit with an error message if the file does not exist
    else:
        shirtfile = Image.open("shirt.png")  # Open the shirt image file
        new_image = Image.open(filename1)  # Open the input image file
        new_image = ImageOps.fit(new_image, shirtfile.size, bleed=0.0, centering=(0.5, 0.5))  # Resize the input image to fit the shirt size
        new_image.paste(shirtfile, (0, 0), shirtfile)  # Paste the shirt image onto the resized input image
        new_image.save(filename2)  # Save the new image to the output file

def check_filename():
    name1, ext_in = sys.argv[1].split(".")  # Split the input filename and its extension
    name2, ext_out = sys.argv[2].split(".")  # Split the output filename and its extension
    if len(sys.argv) < 3:  # Check if there are too few command-line arguments
        sys.exit("Too few command-line arguments")  # Exit with an error message
    elif len(sys.argv) > 3:  # Check if there are too many command-line arguments
        sys.exit("Too many command-line arguments")  # Exit with an error message
    elif ext_in.lower() not in ["jpeg", "jpg", "png"]:  # Check if the input file extension is valid
        sys.exit("Invalid extension")  # Exit with an error message
    elif ext_in.lower() != ext_out.lower():  # Check if the output file extension matches the input file extension
        sys.exit("Output file is not in input file format")  # Exit with an error message
    else:
        return sys.argv[1], sys.argv[2]  # Return the input and output filenames

if __name__ == "__main__":
    main()  # Call the main function to start the program
