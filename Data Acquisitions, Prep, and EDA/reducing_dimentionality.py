# Perform PCA, visualize explained variance of components using bar plot.

# Imports necessary libraries for data manipulation, visualization, and PCA
import matplotlib.pyplot as plt        # For creating plots
import numpy as np                     # For numerical operations
import pandas as pd                    # For data manipulation
import seaborn as sns                  # For advanced plotting
from sklearn.decomposition import PCA  # For Principal Component Analysis

# Reads in the data from a CSV file
data = pd.read_csv('your_data.csv')

# Selects only the numeric variables (columns with numbers)
numeric_data = data.select_dtypes(include=[np.number])

# Drops specific columns ('days_to_separate', 'separated_ny') from the numeric data if needed
numeric_data = numeric_data.drop(columns=['days_to_separate', 'separated_ny'])

# Initializes the PCA with 4 components (dimensions)
pca = PCA(n_components=4)

# Fits the PCA model to the numeric data
pca.fit(numeric_data)

# Retrieves the explained variance ratio for each principal component
explained_variance_ratio = pca.explained_variance_ratio_

# Creates a DataFrame for plotting the explained variance ratio for each component
components = ['Component 1', 'Component 2', 'Component 3', 'Component 4']
explained_variance_df = pd.DataFrame({
    'Component': components,
    'Explained Variance Ratio': explained_variance_ratio
})

# Plots the explained variance ratio for each principal component using a bar plot
sns.barplot(x='Component', y='Explained Variance Ratio', data=explained_variance_df)

plt.xlabel('Principal Components')                         # Label for the x-axis
plt.ylabel('Explained Variance Ratio')                     # Label for the y-axis
plt.title('Explained Variance by Principal Components')    # Title of the plot
plt.show()                                                 # Displays the plot