# The Python Imaging Library adds image processing capabilities to your Python interpreter.

from PIL import Image
from PIL import ImageFilter

img = Image.open(r"Images\0.png")                       # Creating an Image object.
print(img.size)
print(img.format)

area = (200, 200, 600, 600)                             # Are of work
cropped_img = img.crop(area)
cropped_img.show()

resize_img = img.resize((800, 800))
resize_img.show()

flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flip_img.show()

spin_img = img.transpose(Image.ROTATE_90)
spin_img.show()

img1 = Image.open(r"Images\1.jpg")
img2 = Image.open(r"Images\2.jpeg")

r, g, b = img.split()                                   # Splitting the image channels
r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()

new_img = Image.merge("RGB", (b, r1, g1))               # Combining different image channels and creating a new image
new_img.show()
new_img.save(r"Images\new_img.png")                     # Saving an image

area = (1300, 400, 1600, 694)
img1.paste(img2, area)                                  # Pasting one image on another
img1.show()

bw_img = img.convert("L")                               # Converting the image to other mode like B/W or CMYK
bw_img.show()
cmyk_img = img.convert("CMYK")
cmyk_img.show()

# Some basic filters from ImageFilter
blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()
detail_img = img.filter(ImageFilter.DETAIL)
detail_img.show()
edge_img = img.filter(ImageFilter.FIND_EDGES)
edge_img.show()