# Does the string containes all the letter of the alphabet?

from string import ascii_lowercase  

def check_string(original_str):
    missing = ""
    for i in ascii_lowercase:
        if i not in original_str.lower():
            missing += i

    if len(missing) > 0:
        return f"The string is missing the following letters {missing}"
    else:
        return "The string containes all the letters"
    
# Get the input string
original_str = input("String: ")

# Call the function and start the action
results = check_string(original_str)
print(results)