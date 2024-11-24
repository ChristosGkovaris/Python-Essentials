# Importing the time module for adding delay between prints
import time  

# Function to print the string progressively
def print_continuously(target):
    # Initialize an empty string to build progressively
    result = ""

    # Loop through each letter in the input string  
    for letter in target:  
        # Add the current letter to the result
        result += letter

        # Print the progressively built string
        print(result)  

        # Optional delay for better visual effect
        time.sleep(0.1)  


# Get input from the user
input_string = input("Enter a string: ")  

# Print the original input for reference
print("Input:", input_string)  

# Call the function to display the string progressively
print_continuously(input_string)  