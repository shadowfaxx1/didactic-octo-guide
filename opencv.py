import cv2 as cv
# reading images
# img=cv.imread('photos.jpg')
# cv.imshow('photos',img)

#reading videos
cap=cv.VideoCapture('koko.mp4')
while(True):
    isTrue,frame=cap.read()
    cv.imshow('koko',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()
#cv.waitKey(0)

print(0xFF)
