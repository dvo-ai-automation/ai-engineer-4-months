from PIL import Image
from PIL import ImageOps
import sys
import os

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if input[1] == output[1]:
            if input[1].lower() in [".jpg", ".jpeg", ".png"]:
                pic = Image.open(sys.argv[1])
                shirt = Image.open("shirt.png")
                size = shirt.size
                pic = ImageOps.fit(pic, size)
                pic.paste(shirt, shirt)
                Image.save(sys.argv[2])
            else:
                sys.exit("Invalid extension")
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

