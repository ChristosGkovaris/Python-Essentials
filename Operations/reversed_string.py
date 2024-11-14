# Reverse a string

def reverse_string(input_str):
    return ''.join(reversed(input_str))

# Give the input string
input_str = input("Give the reversed string: ")

# Call the function and start the action
results = reverse_string(input_str)
print(results)




# ======================
# Solution 2

# Use slicing
# return input_str[::-1]

# ======================