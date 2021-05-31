# 15. Replace the priority column values with'yes' should be 1 and 'no' should be 0

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery_yes = {"priority":"yes"}
newvalue_1= {"$set":{"priority":1}}
result_1 = mycol.update_many(myquery_yes,newvalue_1)

myquery_no = {"priority":"no"}
newvalue_0 = {"$set":{"priority":0}}
result = mycol.update_many(myquery_no,newvalue_0)

print(list(mycol.find())) 

