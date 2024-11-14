# Format a String

def calc_string(num1, num2):
    # Perform the addition
    operation_result = (num1+num2)

    return operation_result

# Get the numbers for addition
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Call the function and start the action
results = calc_string(num1, num2)
print(f"The sum of {num1} and {num2} is {results}")