import cv2 as cv

img=cv.imread('C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg')
#cv.imshow("cat",img)
# gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
# cv.waitKey(0)
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)
# cv.waitKey(0)
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)
# cv.waitKey(0)

# #BGR to  RGB
# rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("rgb",rgb)
# cv.waitKey(0)

img1=cv.imread("C:\\Users\\Vishal\\Desktop\\divya1.jpg")
cv.imshow("img1",img1)
r,b,g=cv.split(img1)
cv.imshow("red",r)
cv.imshow("green",b)
cv.imshow("blue",g)
cv.waitKey(0)

blurred_img = cv.bilateralFilter(img1, d=9, sigmaColor=75, sigmaSpace=75)

# Display the original and blurred images
cv.imshow('Original', img)
cv.imshow('Blurred', blurred_img)
cv.waitKey(0)
cv.destroyAllWindows()