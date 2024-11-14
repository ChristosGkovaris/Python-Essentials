# Function to check if two strings are anagrams
def is_anagram(first_str, second_str):
    # Initialize empty strings to store only alphabetic characters
    letters1 = ""
    letters2 = ""
    
    # Process the first string
    for letter in first_str.lower():  # Convert to lowercase to ignore case
        # Append only alphabetic characters to letters1
        letters1 += letter if letter.isalpha() else ""
        
    # Process the second string
    for letter in second_str.lower():  # Convert to lowercase to ignore case
        # Append only alphabetic characters to letters2
        letters2 += letter if letter.isalpha() else ""
    
    # Sort both strings and check if they are identical
    return sorted(letters1) == sorted(letters2)

# Get the strings from the user
first_str = input("First string: ")
second_str = input("Second string: ")

# Call the function to check if they are anagrams and print the result
results = is_anagram(first_str, second_str)
print(results)