# pip install pdf2docx

# Import the Converter class from the pdf2docx library
from pdf2docx import Converter

# Define the input PDF file path (ensure the file exists in the specified location)
pdf_file = "test_file.pdf"

# Define the output DOCX file path (the converted file will be saved with this name)
docx_file = "test_file.docx"

# Create a Converter object to handle the conversion process
cv = Converter(pdf_file)

# Convert the PDF to DOCX and save it to the specified output path
cv.convert(docx_file)

# Close the Converter to release resources
cv.close()

# Print a confirmation message upon successful conversion
print(f"Conversion complete: {docx_file}")