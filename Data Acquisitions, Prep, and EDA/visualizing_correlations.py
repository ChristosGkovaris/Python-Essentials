# Generate and visualize correlation heatmap of numeric data in dataset.

# Imports necessary libraries for data manipulation, visualization, and numerical operations
import pandas as pd               # For data manipulation
import seaborn as sns             # For advanced data visualization
import matplotlib.pyplot as plt   # For plotting figures
import numpy as np                # For numerical operations

# Reads the data from a CSV file
data = pd.read_csv('your_data.csv')

# Selects only numeric columns from the data
numeric_data = data.select_dtypes(include=[np.number])

# Drops the 'separated_ny' column from the numeric data
numeric_data = numeric_data.drop(columns=['separated_ny'])

# Calculates the correlation matrix for the numeric variables
correlation_matrix = numeric_data.corr()

# Creates a mask for the upper triangle of the correlation matrix to avoid redundant information
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Sets up the matplotlib figure with specified size
f, ax = plt.subplots(figsize=(11, 9))

# Generates a custom diverging colormap for the heatmap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draws the heatmap for the correlation matrix with the mask, customized colormap, and additional settings
sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})