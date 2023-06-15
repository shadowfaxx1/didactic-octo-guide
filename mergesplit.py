import cv2 as cv
import numpy as np 

img1=cv.imread('photos/mum.jpeg')
img=cv.resize(img1,(500,500),cv.INTER_CUBIC)
# we are splittiing the image into the color channels of 3 B G R so here what we are doing is that calling split method and putting 
#each image as a differnt channel

#all these images are in grayscale showing a dark or light component to display the channels 
b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('greeb',g)
cv.imshow('red',r)
print(img.shape)# we are printing out the pixel along with the channels 
print(b.shape)
print(g.shape)
print(r.shape)

#here merging the 3 block channels together 

merge=cv.merge([b,g,r])
cv.imshow('mer',merge)

#we have another method of doing it with the color that requires a blank img and we put the b g r values in merge method lets c

#creating a blank img
blank=np.zeros(img.shape[:2],dtype='uint8')

blue=cv.merge([b,blank,blank])  # putting bgr values in their respective blocks BGR 
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
xcv.imshow('blue',blue)
cv.imshow('greeb',green)
cv.imshow('red',red)
cv.waitKey(0)

