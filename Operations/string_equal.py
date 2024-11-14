# Are two strings equal?

def check_strings(string1, string2):
    # The function returns TRUE if the strings are equal
    return string1 == string2

# Get the two input strings for checking
string1 = input("Give the first string: ")
string2 = input("Give the second string: ")

# Call the function and start the action
results = check_strings(string1, string2)
print(results)