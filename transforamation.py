from turtle import left, right, up
import cv2 as cv 
import numpy as np 

img=cv.imread('photos/bridge-53769__480.jpg')

# shifting image by some pixel 
def translate(img ,x ,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimension)

# -x = left
# -y=down 
# x=right
# y=up

trans=translate(img,-200,-100)
cv.imshow('trans',trans)

#rotating an image by some angle -45 for clockwise and 45 for counter clockwise
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]  #for width and height

    if rotPoint is None :
        rotPoint=(width//2,height//2)    
    rotmat=cv.getRotationMatrix2D(rotPoint,angle,1.0) 
    dim=(width,height)
    return cv.warpAffine(img,rotmat,dim)

rotated=rotate(img,45)
cv.imshow('rotate',rotated_2)
#these below texts show the rotation resizing and grayscale conversion on a single image 
gray=cv.cvtColor(trans1,cv.COLOR_BGR2GRAY)
rotated=rotate(gray,18)
resize=cv.resize(rotated,(500,500),interpolation=cv.INTER_CUBIC)


#we can flip the img just by taking this attribute cv.flip()
flip=cv.flip(img,0)

cv.waitKey(0)

