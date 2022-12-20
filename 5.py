import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("x_ray.jpg",0) #0 for gray scale &1 for RGB

#Gray level slicing
# s = 255 r>=50 && r<=100
#else s=r or s=0
s = np.array(img)
rows,columns = img.shape
print(rows,columns)

start = 100
end = 200
new_value = 255

for r in range(rows):
    for c in range(columns):
        if(img[r,c]>=start and img[r,c]<=end):
            s[r,c]=new_value
        else:
            s[r,c]=0
 
cv2.imshow("original",img)
cv2.imshow("Gray level scaling",s)
cv2.waitKey(0)


#contrast stretching convrt img to black & white img
#img2 = [[100,50,150,25],[120,70,170,45],[170,120,220,85],[250,200,255,165]]
#img2 = np.asarray(img2)
img2 = cv2.imread("x_ray.jpg",0)
n = img2.copy()

rows,columns = img2.shape
print(rows,columns)

for rows in range(rows):
    for columns in range(columns):
        if(img2[rows,columns]>=0 and img2[rows,columns]<=50):
            n[rows,columns] = round((((img2[rows,columns]-0)*(100-0))/(50-0))+0)
            
        elif(img2[rows,columns]>=50 and img2[rows,columns]<=100):
             n[rows,columns] = round((((img2[rows,columns]-50)*(200-100))/(100-50))+100)
             
        else:
             n[rows,columns] = round((((img2[rows,columns]-100)*(255-200))/(255-100))+200)
             
print(n)
plt.subplot(1, 2,1)
plt.imshow(img2 , cmap=plt.cm.gray)

plt.subplot(1, 2,2)
plt.imshow(n , cmap=plt.cm.gray)

