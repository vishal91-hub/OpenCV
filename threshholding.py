import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\Vishal\\Desktop\\divya1.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

threshold, thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("thres",thresh)
threshold, thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("thres",thresh_inv)
cv.waitKey(0)

#adaptive thresholding

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,5)
cv.imshow("thres-add",adaptive_thresh)
cv.waitKey(0)