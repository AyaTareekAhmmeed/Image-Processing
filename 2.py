from PIL import Image
from skimage import io, filters
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mplt
import numpy as np

#read img using pillow
img = Image.open('rgb.jpg')
plt.imshow(img)
print(img)
print(type(img))
print(img.format)
print(img.mode)
print(img.size)

#convert img to numpy array
n_img = np.asarray(img)
print(type(n_img))

#read img using matplotlib
#matplotlib convert img to numpy array without converter
m_img = mplt.imread("rgb.jpg")
plt.imshow(m_img)
plt.colorbar()
print(type(m_img))
print(m_img.shape)

#reading img using skimage
s_img = io.imread("rgb.jpg")
print(s_img)

#reading img using opencv
#opencv read img as BGR not RGB 
c_img = cv2.imread("rgb.jpg",0)
c2_img = cv2.imread("rgb.jpg",1)
plt.imshow(c_img)
plt.imshow(c2_img)
#to make cv read img as RGB we use
plt.imshow(cv2.cvtColor(c2_img,cv2.COLOR_BGR2RGB))
cv2.imshow("grey img:",c_img)
cv2.imshow("color img:",c2_img)
cv2.waitKey(0) #to avoid runtime error

