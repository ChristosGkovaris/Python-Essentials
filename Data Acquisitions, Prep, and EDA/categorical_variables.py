# Pivot, encode, and merge department and job level data into DataFrame.

# Imports pandas for data manipulation and analysis
import pandas as pd

# Reads in the data from a CSV file
data = pd.read_csv('your_data.csv')

# Creates a 'row_id' column, giving each row a unique identifier
data['row_id'] = range(len(data))

# Converts the 'department' column into a wide format (pivot table), filling missing values with 0
department_wide = data.pivot(index='row_id', columns='department', values='department').fillna(0)

# Converts the 'job_level' column into a wide format (pivot table), filling missing values with 0
job_level_wide = data.pivot(index='row_id', columns='job_level', values='job_level').fillna(0)

# Function to encode values: converts non-zero values to 1, and zero values to 0
def value_encoder(df, variable):
    df[variable] = df[variable].apply(lambda x: 1 if x != 0 else 0)
    return df

# Applies the value_encoder function to each column in the 'department_wide' DataFrame
for col in department_wide.columns:
    department_wide = value_encoder(department_wide, col)

# Applies the value_encoder function to each column in the 'job_level_wide' DataFrame
for col in job_level_wide.columns:
    job_level_wide = value_encoder(job_level_wide, col)

# Joins the new encoded 'department_wide' DataFrame back to the original 'data' DataFrame
encoded_data = data.join(department_wide, on='row_id', rsuffix='_dept')

# Joins the new encoded 'job_level_wide' DataFrame back to the 'encoded_data' DataFrame
encoded_data = encoded_data.join(job_level_wide, on='row_id', rsuffix='_job')