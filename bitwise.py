import cv2 as cv
import numpy as np 

def open():
    blank=np.zeros((500,500),dtype='uint8')
    rect=cv.rectangle(blank.copy(),(30,30),(470,470),255,-1,)
    circle=cv.circle(blank.copy(),(250,250),250,255,-1)
    cv.imshow('rect',rect)
    cv.imshow('circle',circle)

    #here is the bitwise operator and 
    #which returns 0 if any one of the perimeter is 0 
    #that is the intersection 



    bit_and=cv.bitwise_and(rect,circle)
    cv.imshow('and',bit_and)


    #bitwise OR 
    #takes the union
    #intersecting and non intersecting 

    bit_or=cv.bitwise_or(rect,circle)
    cv.imshow('bit_or',bit_or)

    #bitwise XOR 
    #return the zeros bit only 
    #non intersecting
    bit_XOR=cv.bitwise_xor(rect,circle)
    cv.imshow("xor",bit_XOR)

    #bitwise not 

    bit_not=cv.bitwise_not(rect)
    bit_not_circle=cv.bitwise_not(circle)
    cv.imshow('bit_not_rect',bit_not)
    cv.imshow('bit_not_circle',bit_not_circle)





    cv.waitKey(0)


if __name__ == '__main__':
    open()
    # put some test code here
