from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
import ssl
import os
from datetime import date
uri = os.getenv('mongodb_url')

class MongoDB:
    def connectDB():
        try:
            client = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=False)
            print("Connected")
            test = client['test']
            return test,client
        except Exception as err:
            print(err)
    def insertOneItem(name,empno,imgPath,lat,long,city,state):
            client=None
            try:
                print("Database found")
                test,client=MongoDB.connectDB()
                collection = test['employee-records']
                print("Collection created")
                employeeData={
                    "name":name,
                    "empno":empno,
                    "imagePath":imgPath,
                    "location":{
                        "latitude":lat,
                        "longitude":long,
                        "city":city,
                        "state":state
                    }
                }
                collection.insert_one(employeeData)
            except Exception as err:
                 raise err
            finally:
                if client:
                     client.close() 
    def findRecord(empno):
        client=None
        try:
            conn,client=MongoDB.connectDB()
            collection=conn['employee-records']
            employees = list(collection.find({"empno":empno}))
            return employees
        except Exception as err: 
             raise err
        finally:
            if client:
                client.close()   
    def insertAttendance(name,empno,imgVerified,locVerified):
        client=None
        isPresent=imgVerified and locVerified
        record={
              "Date":str(date.today()),
              "Name":name,
              "Employee No":empno,
              "Image Verified":imgVerified,
              "Location Verified":locVerified,
              "Present":isPresent
         }
        try:
                conn,client=MongoDB.connectDB()
                collection=conn['attendance']
                collection.insert_one(record)
        except Exception as err:
             raise err
        finally:
             if client: 
                  client.close()

         
# MongoDB.insertOneItem("Hardik",10101,"img.jpg",10,11,"Haldia","West Bengal")