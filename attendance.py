# this code detects face and geolocation and gives attendance
from facerecognition import FaceRecognition
from detectLocation import Location
from mongodb import MongoDB
import threading
locVerified=False
threads=[]
empno,imgVerified,cap,cv2=FaceRecognition.Recognise()
if cap is None or cv2 is None:
    print("Webcam couldn't open")
    exit(1)
if not imgVerified:
    print("You are not registered. Please register yourself")
    exit(1)
currLat,currLong,currCity,currState = Location.locationCoordinates()
empno=int(empno)
employees = MongoDB.findRecord(empno)
if len(employees) ==0:
    print("Data not found")
    exit(1)
name=""
found=False
for i in employees:
    name=i['name']
    loc=i['location']
    if loc['latitude'] == currLat and loc['longitude']==currLong and loc['city'] == currCity and loc['state']==currState:
        locVerified=True
        found=True
        break
if found:
    print("Employee {} , Employee no {} is present".format(name,empno))
else:
    print("Employee {} , Employee no {} is present".format(name,empno))
try:
    MongoDB.insertAttendance(name,empno,imgVerified,locVerified)
    print("Attendance given")
except Exception as err:
    print("Execution failed!!")
    print(err)
finally:
    print("Execution over")
    cap.release()
    cv2.destroyAllWindows()