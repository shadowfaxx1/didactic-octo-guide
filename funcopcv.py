import cv2 as cv

img=cv.imread('photos/bridge-53769__480.jpg')
cv.imshow('real',img)

#now lets get the gray scale on this image using cv.cvtcolor

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#now we will apply blur on this image using gaussian blur there are a lot of method but here using gaussian 
# we pass the src a tuple of 2*2 that should be odd increasing the value of tuple results in increment of blur intensity 
#blur can be used to increase the intensity and various up and downs in an image 

blur =cv.GaussianBlur(img ,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#egde cascade 
#to find the edges in an image 
# we are using canny method 
edge=cv.Canny(img,225,225)

cv.imshow('edges',edge)

edge2=cv.Canny(img,100,100)
cv.imshow('edges',edge2)


edge3=cv.Canny(img,500,500)
cv.imshow('edges',edge3)

#next we are dealing with dialating the image it takes the edged image
#edge cascade

dialted=cv.dilate(edge3,(3,3),iterations=3)
cv.imshow('dialted',dialted) 

#we can reverse the dialted image back into the edged image it takes dialted image and iteration and a tuple 
#thats called eroding 

eroding=cv.erode(dialted,(3,3),iterations=3)
cv.imshow('eroded',eroding)

#resizing the image doesnt care about the aspaect ratio we can also use interpolation as linear area or cubic 

resize=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR_EXACT)
cv.imshow('resize',resize)

# we can crop the image by array slicing and get a poortiong of it 
crop=img[20:225,225:500]
cv.imshow('croppped',crop)
cv.waitKey(0)