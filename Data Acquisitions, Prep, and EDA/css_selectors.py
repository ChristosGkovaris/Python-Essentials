# This program scrapes a webpage to extract and count specific names and roles data.

# Imports BeautifulSoup for parsing HTML content
from bs4 import BeautifulSoup  

# Imports pandas for data manipulation and analysis
import pandas as pd            

# Imports requests to handle HTTP requests
import requests                

# Defines the URL to scrape
base_link = "https://hplussport.net/#people"  

# Sends a GET request to the URL and retrieves the HTML page content
page_read = requests.get(base_link)  

# Parses the HTML content using BeautifulSoup
soup = BeautifulSoup(page_read.content)  

# Selects elements with the class "card-name" (assumed to contain names)
board_names = soup.select(".card-name")  

# Gets the number of elements with class "card-name"
len(board_names)  

# Selects elements with the class "card-title" (assumed to contain roles)
board_roles = soup.select(".card-title") 

# Gets the number of elements with class "card-title"
len(board_roles)  