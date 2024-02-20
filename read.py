import cv2 as cv

img = cv.imread("C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg")

capture=cv.VideoCapture("C:\\Users\\Vishal\\Desktop\\OpenCV\\dog.mp4")

while True:
    isTrue, frame= capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.imshow('Cat',img)
# cv.waitKey(0)  # Wait indefinitely for a key press
# cv.destroyAllWindows()