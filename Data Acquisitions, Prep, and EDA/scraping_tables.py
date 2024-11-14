# This program retrieves, reads, and extracts a specific HTML table for organized data analysis in Python.

# Pandas handles data manipulation, analysis, cleaning, and organization in Python
import pandas as pd

# Create an object for the link
table_link = "https://3083218.youcanlearnit.net/geographytable.html"

# Reading from the HTML link the table Area
area_data = pd.read_html(table_link, match = "Area")

# Poping out the Area table
area_data = area_data.pop()

area_data