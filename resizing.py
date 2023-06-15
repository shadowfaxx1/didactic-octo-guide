from calendar import c
import cv2 as cv 


def rescale(frame,scale=1.25):
    #works for video,img,and live video 
    width=int(frame.shape[1]*scale -1)
    height=int(frame.shape[0]*scale)

    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
    
def change_res(width=19,height=20):
    cap.set(3,width)
    cap.set(4,height)
    
cap=cv.VideoCapture(0)



while(True):
    istrue,frame=cap.read()
    frame_res=rescale(frame)
    
    cv.imshow('resized kok',frame_res)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()
