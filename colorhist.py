import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
img=cv.imread("C:\\Users\\Vishal\\Desktop\\mmm.jpg")
img1=cv.imread("C:\\Users\\Vishal\\Desktop\\divya1.jpg")
plt.figure()
plt.title("colour histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors=("b","g","r")
for i, col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
