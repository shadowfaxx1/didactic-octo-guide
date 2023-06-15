import cv2 as cv
import numpy as np

img=cv.imread('photos/mum.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
resize=cv.resize(gray,(700,800),interpolation=cv.INTER_CUBIC)
cv.imshow('resize' ,resize)
blue=cv.GaussianBlur(resize,(3,3),cv.BORDER_ISOLATED)
# cany=cv.Canny(blue,120,155)
# cv.imshow('canny' ,cany)
blank=np.zeros(img.shape,dtype='uint8')
blank2=cv.resize(blank,(700,800),interpolation=cv.INTER_CUBIC)

cv.imshow('b;ck',blank2)
#threshold method which converts the img into binary of 1 and 0 so the displayed image is b & w so we declare the intensity 
#in this method of white and black alone with the imh 

ret,thresh=cv.threshold(blue,100,180,cv.THRESH_BINARY)
cv.imshow('thres',thresh)

#getting the contours basically they are the edges in the image which connect 

contours,heirechy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'contour count of img are{len(contours)}')
#we can now draw the contours over our blank image using cv.drawcontours mehtod 
#but this method has a draw back so we can use cany function to directly illustrate the img with edges its like a mirror image of 
#that of cany function 

draw=cv.drawContours(blank2,contours,-1,(255,0.0),1)
cv.imshow('draw',draw)

cv.waitKey(0)



