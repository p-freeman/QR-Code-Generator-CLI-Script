import pyqrcode
import png
import os
from datetime import datetime

# Prompt the user for input
data = input("Enter the text to be converted to a QR code: ")

# Prompt the user for a custom name
custom_name = input("Enter a custom name for the QR code (leave empty for default naming): ")

# Get the current datetime
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H%M%S")

# Create the filename based on user input
if custom_name.strip():
    filename = f"qrcode_images/{date_str} {custom_name.strip()}.png"
    svg_filename = f"qrcode_images/{date_str} {custom_name.strip()}.svg"
else:
    filename = f"qrcode_images/{date_str}_{time_str}.png"
    svg_filename = f"qrcode_images/{date_str}_{time_str}.svg"

# Create the directory if it doesn't exist
os.makedirs("qrcode_images", exist_ok=True)

# Create the QR code
qr = pyqrcode.create(data)

# Save the QR code as a PNG file
qr.png(filename, scale=6)

# Ask if the user wants to create an SVG file
create_svg = input("Do you want to create an SVG file as well? (yes/no): ").strip().lower()
if create_svg == 'yes':
    qr.svg(svg_filename, scale=6)

print(f"QR code generated and saved as {filename}")
if create_svg == 'yes':
    print(f"SVG file also generated and saved as {svg_filename}")
