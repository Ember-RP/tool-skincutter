import sys
import os
import re
from PIL import Image

def process_image(file_path):
    # Check if the file is a PNG
    if not file_path.lower().endswith('.png'):
        print(f"File {file_path} is not a PNG file.")
        return

    # Check if the file name has two terms separated by capitalization and ends with "##_#.png"
    file_name = os.path.basename(file_path)
    match = re.match(r'^(.*?)(\d+_\d+)\.png$', file_name)
    if not match:
        print(f"File {file_path} does not match the required pattern '##_#.png'.")
        return

    terms = []
    term = ""
    for char in match.group(1):
        if char.isupper() and term:
            terms.append(term)
            term = char
        else:
            term += char
    terms.append(term)
    
    if len(terms) < 2:
        print(f"File {file_path} does not have two terms separated by capitalization.")
        return

    number_suffix = match.group(2)

    # Open the image
    image = Image.open(file_path)
    width, height = image.size

    # Check if the image has a square aspect ratio
    if width != height:
        print(f"File {file_path} does not have a square aspect ratio.")
        return

    # Convert the source image to 8-bit depth and save it
    image = image.convert('P', palette=Image.ADAPTIVE)
    image.save(file_path)
    print(f"Converted and saved source file {file_path} to 8-bit depth.")

    # Define the base size (512x512) and the pieces to cut
    base_size = 512
    pieces = [
        ("NakedPelvisSkin", (256, 128), (256, 192)),
        ("FaceLower", (256, 128), (0, 0)),
        ("FaceUpper", (256, 64), (0, 128))
    ]

    # Calculate the scaling factor
    scale_factor = width / base_size

    # Cut and save the pieces
    for piece_name, (base_piece_width, base_piece_height), (base_x, base_y) in pieces:
        piece_width = int(base_piece_width * scale_factor)
        piece_height = int(base_piece_height * scale_factor)
        x = int(base_x * scale_factor)
        y = height - int(base_y * scale_factor) - piece_height  # Adjust y-coordinate from bottom left
        piece = image.crop((x, y, x + piece_width, y + piece_height))
        
        # Convert the piece to 8-bit depth
        piece = piece.convert('P', palette=Image.ADAPTIVE)
        
        piece_file_name = f"{terms[0]}{terms[1]}{piece_name}{number_suffix}.png"
        piece.save(piece_file_name)
        print(f"Saved {piece_file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please drag and drop PNG files onto this script.")
    else:
        for file_path in sys.argv[1:]:
            process_image(file_path)
