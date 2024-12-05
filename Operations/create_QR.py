# pip install qrcode[pil]

# Import the qrcode library for generating QR codes
import qrcode

# Generate a QR code with the text "Let's connect!"
qr = qrcode.make("Let's connect!")

# Save the generated QR code as an image file
qr.save("my_qr_for_linkedin.png")

# Print a confirmation message after saving the QR code
print("QR Code generated and saved as 'my_qr_for_linkedin.png'")