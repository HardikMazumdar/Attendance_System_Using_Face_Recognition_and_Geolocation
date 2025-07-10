from dotenv import load_dotenv
load_dotenv()
from capture_image import Image
from detectLocation import Location
from mongodb import MongoDB
name,empno,imgPath= Image.CaptureImage()
print("Success!!\nEmployee {} having number {} has been registered".format(name,empno))
lat, long, city, state = Location.locationCoordinates()
print("Your location has been saved as {}\n{}\n{}\n{}\n".format(lat,long,city,state))
try:
    MongoDB.insertOneItem(name,empno,imgPath,lat,long,city,state)
    print("Registration successful !!")
except Exception as err:
    print("Execution Failed !!!!!")
    print(err)
finally:
    print("Registration over!!")