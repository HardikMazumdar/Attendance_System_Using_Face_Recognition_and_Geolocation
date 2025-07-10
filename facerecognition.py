import cv2
import numpy as np
import face_recognition
import os
class FaceRecognition:
    def findEncodings(listOfImages):
        encodeList=[]
        for image in listOfImages:
            image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(image)[0]
            encodeList.append(encode)
        return encodeList
    def Recognise():
        isVerified=False
        folderPath='./faces'
        images=[]
        names=[]
        listOfImages=os.listdir(folderPath)
        for image in listOfImages:
            img = cv2.imread('{}/{}'.format(folderPath,image))
            images.append(img)
            names.append(os.path.splitext(image)[0])
        print(names)
        #now we will find the encodings
        listOfEncodings=FaceRecognition.findEncodings(images)
        print("Encoding complete")

        #detect and encode faces from webcam
        scale = 0.25
        box_multiplier = 1/scale
        cap = cv2.VideoCapture(0)
        while True:
            flag=False
            success,frame=cap.read()
            curr_image = cv2.resize(frame,(0,0),None,scale,scale)
            curr_image = cv2.cvtColor(curr_image,cv2.COLOR_BGR2RGB)
            face_location = face_recognition.face_locations(curr_image,model='hog')
            face_encoding = face_recognition.face_encodings(curr_image,face_location)
            for encodeFace,faceLocation in zip(face_encoding,face_location):
                matches = face_recognition.compare_faces(listOfEncodings,encodeFace,tolerance=0.6)
                faceDis = face_recognition.face_distance(listOfEncodings,encodeFace)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name=names[matchIndex]
                    isVerified=True
                else:
                    name='Unknown'
                y1,x2,y2,x1 = faceLocation
                y1=int(y1*box_multiplier)
                y2=int(y2*box_multiplier)
                x1=int(x1*box_multiplier)
                x2=int(x2*box_multiplier)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame,(x1,y2-20),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                cv2.imshow("Webcam", frame)
                cv2.waitKey(3000)
                flag=True
                return name,isVerified,cap,cv2
# print(FaceRecognition.Recognise())