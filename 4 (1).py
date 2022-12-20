from skimage import io
from matplotlib import pyplot as plt
import numpy as np



#img negative s= (l-1)-r
img = io.imread("B2DBy.jpg")

width , hight,r = img.shape
n_img = np.array(img)

for w in range(width):
    for h in range(hight):
        n_img[w,h]= (226-1)-img[w,h]
        
        
plt.subplot(1, 2,1)
plt.imshow(img , cmap=plt.cm.gray)

plt.subplot(1, 2,2)
plt.imshow(n_img , cmap=plt.cm.gray)

#log transformation s =c*log(1+r)
c =1.3 #conestant 
log_img = np.array(img)

for w in range(width):
    for h in range(hight):
        log_img[w,h]=( c*np.log(1 +(img[w,h]/255.0)))*255.0 #/255.0 for scaling data
        
        
plt.subplot(1, 2,1)
plt.imshow(img , cmap=plt.cm.gray)

plt.subplot(1, 2,2)
plt.imshow(log_img , cmap=plt.cm.gray)



#power low transformation for brightness  s = (c*r)**gamma
c =1 #conestant 
gamma = 0.4
power_img = np.array(img)

for w in range(width):
    for h in range(hight):
        power_img[w,h]=( c*((img[w,h]/255.0)**gamma))*255.0 #/255.0 for scaling data 
        
        
plt.subplot(1, 2,1)
plt.imshow(img , cmap=plt.cm.gray)

plt.subplot(1, 2,2)
plt.imshow(power_img , cmap=plt.cm.gray)
