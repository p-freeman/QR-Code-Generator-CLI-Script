# QR-Code-Generator-CLI-Script

This script generates QR codes from user input and saves them as PNG and optionally as SVG files. The generated files are saved in a subfolder named `qrcode_images`.

## Requirements

- Python 3.x
- `pyqrcode` library
- `pypng` library

## Installation

1. Make sure Python 3 and pip are installed on your system.
2. Install the required libraries:
    ```sh
    pip3 install pyqrcode pypng
    ```

## Usage

1. Run the script:
    ```sh
    python3 generate_qr_cli.py
    ```
2. Follow the prompts:
    - Enter the text to be converted to a QR code.
    - Optionally, enter a custom name for the QR code. If left empty, the filename will be generated based on the current date and time.
    - Choose whether to create an SVG file in addition to the PNG file.

3. The QR code image files will be saved in the `qrcode_images` subfolder. If a custom name is provided, the file will be named in the format `YYYY-MM-DD name.png` and optionally `YYYY-MM-DD name.svg`. If no custom name is provided, the file will be named in the format `YYYY-MM-DD_HHMMSS.png` and optionally `YYYY-MM-DD_HHMMSS.svg`.

## Example

$ python3 generate_qr_cli.py  
Enter the text to be converted to a QR code: https://example.com  
Enter a custom name for the QR code (leave empty for default naming): example  
Do you want to create an SVG file as well? (yes/no): yes  
QR code generated and saved as qrcode_images/2024-07-17 example.png  
SVG file also generated and saved as qrcode_images/2024-07-17 example.svg
