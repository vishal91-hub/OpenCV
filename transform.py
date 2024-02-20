import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg")
cv.imshow("cat",img)
cv.waitKey(0)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# positive x --right
# positve y-- down

translated=translate(img,50,50)
cv.imshow('translated',translated)
cv.waitKey(0)

def rotate(img,angle, rotPoint=None):
    (height,width)=img.shape[0:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotted=rotate(img,45)
cv.imshow("rott",rotted)
cv.waitKey(0)