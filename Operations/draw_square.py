def square(n):
    # Loop through each row to construct the square
    for i in range(0, n):
        # If it's the first or last row, print a full row of "#" symbols
        if i == 0 or i == (n - 1):
            print("# " * n)
        else:
            # For other rows, print "#" at the beginning and end with spaces in between
            print("# " + "  " * (n - 2) + "#")

# Prompt the user to enter the size of the square
n = int(input("Draw a square of the size: "))
# Call the square function to print the square, and ensure no "None" is printed
square(n)