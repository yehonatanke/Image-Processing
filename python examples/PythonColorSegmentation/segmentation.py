# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:11:18 2015

@author: azariac
"""



import numpy as np
import cv2


print 'hello - start of program'
# img = cv2.imread('images/tia.jpg',cv2.IMREAD_COLOR)
img = cv2.imread('tia.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)

crop_img = img[50:60, 95:120] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", crop_img)

d1,d2,d3 = crop_img.shape
print(d1,d2,d3)
b = np.zeros([d1*d2,d3])


for i in range(d1):
    for j in range(d2):
        k=i*d2+j
 #       print k
        b[k,:] = crop_img[i,j,:]


c=np.cov(b.T)
from numpy.linalg import inv
cm1=inv(c)
meanC=np.array(cv2.mean(crop_img))
d1,d2,d3 = img.shape
mask=np.zeros([d1,d2])
epsilon=100;
for i in range(d1):
    for j in range(d2):
        v=np.array(img[i,j,:]) 
        v1=meanC.T
        v1=v1[:3]
        v=v-v1
        dis=np.dot(np.dot(v, cm1),v.T)
        if dis>epsilon:
            mask[i,j]=1
            
out_img=img
for i in range(d1):
    for j in range(d2):
        if mask[i,j]==1:
            out_img[i,j,:]=np.zeros([3])
            
cv2.imshow("output", out_img)          
            

k=cv2.waitKey(0)


print 'destroy all windows'    
cv2.destroyAllWindows()

#cv2.imwrite('images/tia_out.jpg',out_img)
cv2.imwrite('tia_out.jpg',out_img)