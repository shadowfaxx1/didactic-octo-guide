import cv2 as cv

img=cv.imread("photos/bridge.jpg")
cv.imshow('img',img)

cv.waitKey(0)
