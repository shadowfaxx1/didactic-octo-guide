import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt


img1=cv.imread("photos/bridge.jpg")
#we plotted this image in to the matplot lib and it shows completly different color saturation as for the bgr
img=cv.resize(img1,(500,500),cv.INTER_CUBIC)
# plt.imshow(img)
# plt.show()
cv.imshow('imh',img)
# different types of color spaces 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# eroding=cv.erode(gray_bgr,(7,7),iterations=5)
# cv.imshow('eroding',eroding)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('bgr+hsv',hsv_bgr)
cv.waitKey(0)