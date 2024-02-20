import os
import cv2 
import numpy as np
DIR="C:\\Users\\Vishal\\Desktop\\OpenCV\\train"
haar_cas=cv2.CascadeClassifier('haar_face.xml')
people=[]
for i in os.listdir(r"C:\Users\Vishal\Desktop\OpenCV\train"):
    people.append(i)

print(people)
features=[]
labels=[]
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv2.imread(img_path)
            gray=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
            faces_rect=haar_cas.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
# train the recognizer on the features list and label list
features=np.array(features,dtype='object')
labels=np.array(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(features,labels)
recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save("labels.npy",labels)

    