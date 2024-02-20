import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg")
#cv.imshow("cat",img)

cv.waitKey(0)
blank=np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank',blank)

# blank[200:345,300:400]=0,0,255
# cv.imshow('Green',blank)
# cv.waitKey(0)
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
cv.imshow("rec",blank)
cv.waitKey(0)