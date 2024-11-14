# This program scrapes a webpage to extract the last paragraph's text as a string.

# Imports BeautifulSoup for parsing HTML content
from bs4 import BeautifulSoup  

# Imports pandas for data manipulation and analysis
import pandas as pd            

# Imports requests to handle HTTP requests
import requests                

# Defines the URL to scrape
page_link = "//3083218.youcanlearnit.net/rainieststate.html"  

# Sends a GET request to the URL and retrieves the HTML page content
page_read = requests.get(page_link)  

# Parses the HTML content using BeautifulSoup
soup = BeautifulSoup(page_read.content)  

# Extracts the text of the last paragraph in the HTML
state_result = soup.select_one("p:last-of-type").string  

# Removes any leading or trailing whitespace from the extracted text
state_result = state_result.strip()

# Creates a dictionary to store state data, with the key 0 for the column header and key 1 for the data
state_data = {0: ['State'], 1: [state_result]}

# Converts the dictionary to a pandas DataFrame for easier manipulation
state_data = pd.DataFrame(state_data)

# Reads tables from the HTML page, specifically looking for a table that matches the title "Capital"
table = pd.read_html(page_link, match="Capital")

# Extracts the table that matches, using .pop() to get the first element from the list of tables
table = table.pop()

# Combines the extracted table with the state data DataFrame
table = pd.concat([table, state_data])

# Renames the columns for clarity: "info" for the first column and "stat" for the second
table = table.rename(columns={0: "info", 1: "stat"})

# Reshapes the DataFrame to have "info" values as columns and their corresponding "stat" values as rows
table = table.pivot(columns="info", values="stat")

# Displays the updated table
table

# Fills missing values in the DataFrame by backfilling (moving values backward to fill empty spots)
table_fill = table.bfill()

# Drops all rows except the first, effectively keeping only the first filled row
table_fill.drop(range(1, len(table_fill)))
