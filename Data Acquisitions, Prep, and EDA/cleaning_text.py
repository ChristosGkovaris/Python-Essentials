# Separate words in camelCase strings by adding spaces with regex.

# Imports pandas for data manipulation and analysis
import pandas as pd

# Creates a dictionary with a list of strings that have no spaces between words
painful_strings = {'painful_strings': ['usePython', 'pandasForLife', 'Python is helpful']}

# Converts the dictionary to a DataFrame
long_strings = pd.DataFrame(data=painful_strings)

# Uses regex to add a space between lowercase and uppercase letters in each string
long_strings['painful_strings'] = long_strings['painful_strings'].str.replace(
    pat='([a-z])([A-Z])',  # Pattern to find lowercase letter followed by an uppercase letter
    repl='\\1 \\2'  # Adds a space between matched lowercase and uppercase letters
)

# Displays the modified DataFrame
long_strings