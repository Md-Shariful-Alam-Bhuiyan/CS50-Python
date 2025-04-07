from PIL import Image, ImageFilter

def main():
    with Image.open("costume_1.gif") as img:
        print(img.size)
        print(img.format)
        # For roatating the image
        img = img.rotate(180)
        # convert image mood from palette("P") to "RGB" hence image.filter() doesn't work on palette based image such as gif
        img = img.convert('RGB')
        img = img.filter(ImageFilter.BLUR) # to blur the image
        img = img.filter(ImageFilter.FIND_EDGES) # to get such image that reflects the edges of the actual image
        # saving the image within a new file with the desired format of the image
        img.save("out.gif")



main()
