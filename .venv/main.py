from PIL import Image, ImageFilter, ImageEnhance
#

with Image.open("blue.jpg") as picture:
#    picture.show()   #this command opens up the picture viewing program and shows as the picture

    black_white = picture.convert('L') #this command makes the original picture black and white
    black_white.save("black_white.jpg") #this command saves the new picture and creates a new picture under the name in the parenthesis

    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT) #this command makes a mirrored version of the original picture
    mirror.save("mirror.jpg")

    blur = picture.filter(ImageFilter.BLUR) #this command makes a blurredd version of the original picture
    blur.save("blur.jpg")



#   Enhance
    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(2.8) #with this command we specify how much we want to enhance the contrast of our image
    #in the command above, if i put a negative value it will show the image witrh a negative effect
    contrast.save("contrast.jpg")
    #if i change the name in the parenthesis a new image will be created with the name in the parenthesis. The previous file will still exist


    color = ImageEnhance.Color(picture).enhance(2.8) #with this command we specify how much we want to enhance the color of our image
    color.save("color.jpg")