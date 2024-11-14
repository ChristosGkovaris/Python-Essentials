# Retrieve and format API data.

# Imports pandas for data manipulation and analysis
import pandas as pd            

# Imports requests to handle HTTP requests
import requests                

# Sends a GET request to the API endpoint and retrieves JSON data
response = requests.get("https://3083218.youcanlearnit.net/rank.json?_=1662342121475")

# Converts the JSON response to a DataFrame using from_dict
state_data = pd.DataFrame.from_dict(response.json())

# Extracts the 'data' field from the JSON and converts it to a DataFrame with specified columns
state_data = pd.DataFrame(state_data['data'].to_list(), columns=['rank', 'state', 'rainfall'])

# Displays the final DataFrame with rank, state, and rainfall data
state_data