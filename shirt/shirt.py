import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    suffixes = (".jpg",".jpeg",".png")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line Arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif sys.argv[1].lower().endswith(suffixes) and not sys.argv[2].lower().endswith(suffixes):
        sys.exit("Invalid output")
        
    elif not sys.argv[1].lower().endswith(suffixes) or not sys.argv[2].lower().endswith(suffixes):
        sys.exit("Invalid input")

    elif extention(sys.argv[1]).lower() != extention(sys.argv[2]).lower():
        sys.exit("Input and output have different extensions")
    else:
        pass

    try:
        image = Image.open(sys.argv[1])
        shirt_image = Image.open("shirt.png")
        size = shirt_image.size
        new_image = ImageOps.fit(image, size)
        new_image.paste(shirt_image, shirt_image)
        new_image.save(sys.argv[2])


    except FileNotFoundError:
        sys.exit("Input does not exist")



def extention(file):
    file1 = splitext(file)
    return file1[1]



if __name__ == '__main__':
    main()
