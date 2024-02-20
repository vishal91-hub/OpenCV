import cv2 as cv

img=cv.imread('C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg')
#cv.imshow("cat",img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

# blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
# cv.waitKey(0 )

canny=cv.Canny(img,125,175)
cv.imshow("can",canny)
cv.waitKey(0 )

#resize same as earlier
#cropping
cropped=img[0:200,0:500]
cv.imshow('crop',cropped)
cv.waitKey(0)