# String replacement

def replace_string(original_str, old_str, new_str):
    return original_str.replace(old_str, new_str)

# Get user inputs
original_str = input("Give the original string: ")
old_str = input("String to replace: ")
new_str = input("String used as a replacement: ")

# Call the function and print the result
results = replace_string(original_str, old_str, new_str)
print(results)