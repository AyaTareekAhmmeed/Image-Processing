#model 3
from PIL import Image
import cv2
from matplotlib import pyplot as plt
import numpy as np

#read img using pillow
img = Image.open('x-ray.jpg')
plt.imshow(img)

n_img = np.asarray(img)
print(type(n_img))

#gray scaling
img2 = cv2.imread("x_ray.jpg",0)

s = np.array(img2)
rows,columns = img2.shape
print(rows,columns)

start = 100
end = 200
new_value = 255

for r in range(rows):
    for c in range(columns):
        if(img2[r,c]>=start and img2[r,c]<=end):
            s[r,c]=new_value
        else:
            s[r,c]=0
 
cv2.imshow("org",img2)
cv2.imshow("Gray",s)
cv2.waitKey(0)

#resizing 180,220
resized_img = img.resize((180,220))
plt.imshow(resized_img)
resized_img.save("rx_ray.jpg")

#paste resized into original
resized_img = resized_img.copy()
img.paste(resized_img,(200,200))
plt.imshow(img)
img.save("img2.jpg")

