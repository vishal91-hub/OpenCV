import cv2 as cv

# Get the OpenCV version
print("OpenCV version:", cv.__version__)
img= cv.imread("C:\\Users\\Vishal\\Desktop\\mmm.jpg")
cv.imshow("person",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
haar_cas=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), thickness=2)

cv.imshow("detected face",img)

cv.waitKey(0)