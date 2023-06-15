import cv2 as cv

#we are discussing about the various blurs right now 
#blurs are used to smoothen the image and reduce the noise 



img1 =cv.imread('photos/cat.jpg')
img=cv.resize(img1,(500,500),cv.INTER_CUBIC)
cv.imshow('img',img)
#that is our old friend gaussian blur where we pur in the kernel size along with the border isolated keyword a grid or window works on the img
#To blur it and it moves as the kernel we provide 
#works as the averaging blur but it gives the weight to the surrounding pixel 



gaus_blur=cv.GaussianBlur(img,(3,3),cv.BORDER_REPLICATE) 

cv.imshow('gaus_blur',gaus_blur)
# averaging blur 
# the window has a size refered to as the kernel size so essentially the blur is applied to the middle or centre pixel as 
# reuslt of the surrounding pixel 
# * * * 
# * center pixel *
# * * * 
#it averages the pixel intensity of the surrounding pixel  around the centre
#higher the kernel size more blurry img 
aver_blur=cv.blur(img,(3,3))
cv.imshow('aver_blur',aver_blur)

#median blur 
# it basically is same as averaging but it takes the median rather than the averaging 
#not suitable for higher kernel 

med_blur=cv.medianBlur(img,3) #only an integer not a tuple as opencv knows its a tuple 
cv.imshow('med_bkur',med_blur)


#bilateral blurring 
# its the most effective used in adavanaced computer projects 
#takes a diamter not kernel 
#sigmacolor larger value means more pixelated color will be considered while blurring 
#sigmaspace larger value means it hinder the blur more by spacing 
bilateral_blur = cv.bilateralFilter(img,40,100,100) 
cv.imshow('bilateral',bilateral_blur)
cv.waitKey(0)

