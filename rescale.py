import cv2 as cv

# img= cv.imread("C:\\Users\\Vishal\\Desktop\\LSTM\\cat.jpg")
# cv.imshow('cat',img)

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions,interpolation=cv.INTER_LINEAR)


capture=cv.VideoCapture("C:\\Users\\Vishal\\Desktop\\OpenCV\\dog.mp4")

while True:
    isTrue, frame= capture.read()
    #cv.imshow('video',frame)
    frame_resized= rescaleFrame(frame,0.25)
    cv.imshow('video1',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()