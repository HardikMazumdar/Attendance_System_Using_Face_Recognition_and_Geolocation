import cv2
class Image:
    def CaptureImage():
        name = input("Please enter your name : ")
        empno = int(input("{}, Please enter your employee no : ".format(name)))
        if not (empno >= 10000 and empno <= 99999):
            print("Invalid emp no")
            print("Please start registration again")
            exit(1) 
        cap = cv2.VideoCapture(0)
        while True:
            success,frame = cap.read()
            cv2.imshow("Frame",frame)
            if cv2.waitKey(1) == ord('c'):
                filename = 'faces/'+str(empno)+'.jpg'
                cv2.imwrite(filename, frame)
                print("Image Saved- ",filename)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        return name, empno,filename