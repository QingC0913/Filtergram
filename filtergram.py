#imports the "filters.py" file
import filters

def main():
    filename = input("Enter the name of the file you want to edit:")
    #use load_img function from the file "filters". "img" is the image from the file in "filename"
    img= filters.load_img(filename)

    #makes the image into gray scale
    newim = filters.grayscale(img)
    filters.save_img(newim, "grayviolin.jpg")

    #makes image into light blue, red, dark blue, and yellow
    newimage = filters.obamicon(img)
    filters.save_img(newimage, "obamiconviolin.jpg")

    #makes image into inverted colors
    image2  = filters.invertcolors(img)
    filters.save_img(image2, "invertedviolin.jpg")

    #else: just shows picture, if not grayscaled
    im = filters.show_img(img)
    filters.save_img(im, "violin.jpg")



#NON TOCCARE!
if __name__ == "__main__":
    main()
