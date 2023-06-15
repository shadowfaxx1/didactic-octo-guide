import cv2 as cv
import numpy as np 

img=cv.imread('photos/bridge.jpg')

def translate(img,x,y):
    trans=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])

    return cv.warpAffine(img,trans,dim)

trans1=translate(img,100,100)

cv.imshow('trans',trans1)


#rotating 
def rotate(img,angle,rotat=None):
    height,width=(img.shape[:2])
    if rotat is None:
        rotat=(width//2,height//2)

    rotmat=cv.getRotationMatrix2D(rotat,angle,1.0)
    dim=(height,width)


    return cv.warpAffine(img,rotmat,dim)

gray=cv.cvtColor(trans1,cv.COLOR_BGR2GRAY)
rotated=rotate(gray,18)
resize=cv.resize(rotated,(500,500),interpolation=cv.INTER_CUBIC)



flip=cv.flip(img,0)
# cv.imshow('flip',flip)
cv.imshow('rotated',resize)

cv.waitKey(0)

    