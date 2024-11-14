# Calculate and apply Z-scores to data.

# Imports pandas for data manipulation and analysis
import pandas as pd

# Reads in the data from a CSV file
data = pd.read_csv('your_data.csv')

# Defines a function to calculate the Z-score for a given variable
def z_score_maker(variable):
    mean = variable.mean()  # Calculates the mean of the variable
    std_dev = variable.std()  # Calculates the standard deviation of the variable
    # Returns the Z-score by subtracting the mean and dividing by the standard deviation
    return (variable - mean) / std_dev

# Applies the z_score_maker function to the 'age' column and stores the result in a new column 'age_z_score'
data['age_z_score'] = z_score_maker(data['age'])