import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
img=cv.imread("C:\\Users\\Vishal\\Desktop\\mmm.jpg")
img1=cv.imread("C:\\Users\\Vishal\\Desktop\\divya1.jpg")
cv.imshow("divya",img)
blank=np.zeros(img.shape[0:2],dtype='uint8')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray1=cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
regray=cv.resize(gray1,(img.shape[1],img.shape[0]))
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask=cv.bitwise_and(gray,regray,mask=circle)
cv.imshow("Mask",mask)
#GrayImageHistogram
gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
cv.waitKey(0)
plt.figure()
plt.title("GrayscaleImage")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.show()


