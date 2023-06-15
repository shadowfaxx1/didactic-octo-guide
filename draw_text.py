import cv2 as cv
import numpy as np 


img=np.zeros((500,500,3),dtype='uint8') #uint8 is datatype of img  #prvdiing 3 as an argument for width 

cap=cv.imread('photos.jpg')
cv.imshow(' ',img)

img[:]=	75,80,180
img[0:100,100:200] =212,112,121
img[200:400 ,200:400]=0,255,255   #here we have filled a square by providing the pixel to the cv function and producing a yellow sqaure
img[100:200,100:200]=0,255,0
img[0:100,0:100]=113,25,78

#drawing rectangle 
cv.rectangle(img,(0,0),(200,499),(175,88,102),thickness=7)
# cv.rectangle(img,(0,0),(200,499),(175,88,102),thickness=-1 or cv.FILLED) #this will make a color block rect
# cv.rectangle(img,(0,0),(img.shape[1]//3,img.shape[0]//2),(0,255,0),thickness= cv.FILLED)

#drawing circle 
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),90,(78,155,67),thickness=-1)

#drawing line 
cv.line()
cv.line(img,(0,0),(250,250),(255,255,255),thickness=4)

#text writing on img 
cv.putText(img,'hello world', (225,225) ,cv.FONT_HERSHEY_TRIPLEX,1.0,(101,101,101),thickness=3)
cv.putText()
cv.imshow(' ',img)

# cv.imshow('' ,cap)
cv.waitKey(0)


