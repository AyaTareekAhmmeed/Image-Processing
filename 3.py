from PIL import Image
from skimage import io, filters
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mplt
import numpy as np

#read img using pillow
img = Image.open('rgb.jpg')

#img resizing
s_img = img.resize((150,200))
plt.imshow(s_img)
s_img.save("s_img.jpg")

#img cropping
c_img = img.crop((0,0,100,150))
plt.imshow(c_img)
c_img.save("c_img.jpg")

#img rotate
r_img = img.rotate(90)
plt.imshow(r_img)
r_img.save("r_img.jpg")

#copy img on another img
cp_img = c_img.copy()
img.paste(cp_img,(100,100))
plt.imshow(img)
img.save("img.jpg")