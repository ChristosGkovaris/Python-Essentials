# Read, select, and clean numeric columns from a CSV dataset.

# Imports pandas for data manipulation and analysis
import pandas as pd

# Reads in the data from a CSV file
data = pd.read_csv('your_data.csv')

# Checks the data types of each column
data_types = data.dtypes

# Selects columns with numeric data types (integers and floats only)
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns

# Creates a subset of the data with only the selected numeric variables
selected_variables = data[numeric_columns]

# Drops the 'separated_ny' column from the selected variables if it exists
selected_variables = selected_variables.drop(columns=['separated_ny'])

# Checks the final data types of the selected variables
final_data_types = selected_variables.dtypes