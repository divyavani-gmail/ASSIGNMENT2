# 8. Select the rows where the birds is a Cranes and the age is less than 4

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find({"birds":"Cranes","age":{"$lt":4}})
print(list(myquery))