import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Vishal\\Desktop\\mmm.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("lap",lap)
cv.waitKey(0)

#sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow("sobel",sobelx)
cv.imshow("sobel1",sobely)
com_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("sobel_co",com_sobel)
cv.waitKey(0)