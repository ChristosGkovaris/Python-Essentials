# Retrieve and combine JSON image data into a single DataFrame.

# Imports pandas for data manipulation and analysis
import pandas as pd            

# Imports requests to handle HTTP requests
import requests                

# Sets the base URL for the API endpoint to retrieve image data by ID
base_link = 'https://pixelford.com/api/image/id/'

# Initializes an empty list to store individual DataFrames for each API response
pixelford_list = []

# Loops through IDs 1 to 20 to retrieve data for each image
for i in range(1, 21):
    individual_link = base_link + str(i)                        # Constructs the URL for each specific image ID
    initial_link = requests.get(individual_link)                # Sends a GET request to the constructed URL
    json_results = initial_link.json()                          # Parses the JSON response from the API
    pixelford_list.append(pd.DataFrame.from_dict(json_results)) # Converts JSON data to a DataFrame and appends it to the list

# Concatenates all DataFrames in the list into a single DataFrame
pixelford_df = pd.concat(pixelford_list)