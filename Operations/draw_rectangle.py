# Define a function to draw a rectangle using recursion
def rectangle(height, width):
    # Base case: if height is 0, stop the recursion
    if height == 0:  
        return
    
    # Print a row of the rectangle with '#' repeated 'width' times
    print(width * "# ")  

    # Recursive call with reduced height
    rectangle(height - 1, width)  

# Get user input for height and width of the rectangle
# Input for the height of the rectangle
height = int(input("Height: "))  

# Input for the width of the rectangle
width = int(input("Width: "))  

# Call the rectangle function to draw the rectangle
rectangle(height, width)