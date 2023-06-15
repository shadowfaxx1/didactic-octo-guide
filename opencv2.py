from configparser import Interpolation
from platform import release
import cv2 as cv

img=cv.imread('C:\\Users\\kaifk\\OneDrive\\Pictures\\Camera Roll\\IMG_1200.JPG')

def rescale(frame , scale=0.11):

    width=int(frame.shape[1] *scale)
    height=int(frame.shape[0] *scale) 
    dim=(width,height)

    return cv.resize(img,dim,interpolation=cv.INTER_AREA)

fr=rescale(img)
cv.imshow('food',fr)

cv.waitKey(0) & ord('d')
