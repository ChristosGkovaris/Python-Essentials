# Load data and generate descriptive statistics.

# Imports pandas for data manipulation and analysis
import pandas as pd

# Sets the display option to show all columns in the DataFrame output
pd.set_option('display.max_columns', None)

# Reads in the data from a CSV file
data = pd.read_csv('your_data.csv')

# Produces descriptive statistics (like mean, std, min, max, etc.) for all variables
descriptive_stats = data.describe(include='all')  # 'include="all"' includes both numeric and non-numeric columns