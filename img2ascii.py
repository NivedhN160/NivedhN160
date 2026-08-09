import sys
from PIL import Image

def image_to_ascii(image_path, width=45):
    # ASCII characters used to build the output text, from dark to light
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Resize image
    aspect_ratio = image.height / image.width
    # Adjust for character aspect ratio (characters are roughly twice as tall as they are wide)
    new_height = int(aspect_ratio * width * 0.5)
    image = image.resize((width, new_height))
    
    # Convert to grayscale
    image = image.convert("L")
    
    # Convert pixels to ascii
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    
    # Format into lines
    ascii_lines = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    
    print("ascii_art = [")
    for line in ascii_lines:
        print(f'    "{line}",')
    print("]")

if __name__ == "__main__":
    image_to_ascii("1782466891470.jpg")
