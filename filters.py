#import the sub-module Image from the module pillow
from PIL import Image

#opens file in Image class using a given filename
def load_img(filename):
    im = Image.open(filename)
    return im

def obamicon(im):
    pixels = im.getdata()
    newpixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for p in pixels:
        intensity = sum(p)
        if intensity < 182:
            newpixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newpixels.append(red)
        elif intensity >= 364 and intensity < 546:
            newpixels.append(lightBlue)
        elif intensity > 546:
            newpixels.append(yellow)
    newimage = Image.new("RGB", im.size)
    newimage.putdata(newpixels)
    return newimage

def grayscale(im):
    #stores list of pixels in the image in the variable "pixels"
    pixels = im.getdata()
    newpixels = []
    #find sum of all pixels and find average of each color: RGB(red, green, blue)
    for p in pixels:
        total = sum(p)
        avg = total // 3
        newpixels.append((avg, avg, avg))

    newim = Image.new("RGB", im.size)
    newim.putdata(newpixels)
    return newim

def invertcolors(im):
    pixels = im.getdata()
    newpixels =[]

    for p in pixels:
        red = p[0]
        green = p[1]
        blue = p[2]
        newpixels.append((255-red, 255-green, 255-blue))
    image2 = Image.new("RGB", im.size)
    image2.putdata(newpixels)
    return image2

#shows image from the given filename above
#not capitalized "image" is the object
#capitalized "Image" is the class
def show_img(im):
    im.show()

#saves image from the shown image above
def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)
