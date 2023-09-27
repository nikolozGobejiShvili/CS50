import sys
from os.path import splitext
from PIL import Image, ImageOps

image_formats = [".jpg", ".jpeg", ".png"]

def main():
    command_line_argument_check()
    try:
        image = Image.open(sys.argv[1])
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    size = shirt_image.size
    after_image = ImageOps.fit(image, size)
    after_image.paste(shirt_image,shirt_image)
    after_image.save(sys.argv[2])

def command_line_argument_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys_split() == False:
        sys.exit("invalid output")
    if image_format_match() == False:
        sys.exit("Input and output have different extensions")

def sys_split():
    image_format1 = splitext(sys.argv[1])
    image_format2 = splitext(sys.argv[2])
    if image_format1[-1].lower() not in image_formats:
        return False
    if image_format2[-1].lower() not in image_formats:
        return False

def image_format_match():
    image_format1 = splitext(sys.argv[1])
    image_format2 = splitext(sys.argv[2])
    if image_format1[-1].lower() != image_format2[-1].lower():
        return False

if __name__ == "__main__":
    main()