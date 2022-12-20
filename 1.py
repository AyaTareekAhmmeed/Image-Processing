from skimage import io, filters
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float

#read img
img = io.imread("Desktop/rgb.jpg")
print(img)
plt.imshow(img)

#img filtering
g_img = filters.gaussian(img,sigma=5)
plt.imshow(g_img)

#creating random img
r_img = np.random.random([300,300])
plt.imshow(r_img)

#scaling pixels
f_img = img_as_float(img)
plt.imshow(f_img)

#drow on img
img[0:100,0:100,:]=[255,0,0] #red 
img[100:200,0:100,:]=[255,255,255] #white
img[200:300,0:100,:]=[0,0,0] #black
plt.imshow(img)

#chanel img
c_img = img[:,:,0]
plt.imshow(c_img)

#creat img
board = np.zeros([1000,1000])
board[100:400,100:200]=1
plt.imshow(board,cmap=plt.cm.gray) #cmap=plt.cm.gray for gray scale