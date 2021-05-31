# 6. select the rows where the number of visits is less than 4
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find({"visits":{"$lt":4}})
print(list(myquery))
