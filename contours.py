import cv2 as cv

img=cv.imread('C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg')
#cv.imshow("cat",img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

canny=cv.Canny(img,125,175)

cv.imshow("canny",canny)
contours, hierarchies= cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.waitKey(0)