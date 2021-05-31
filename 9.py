# 9. Select the rows the age is between 2 and 4(inclusive)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find({"age":{"$gte":2 ,"$lte":4}})
print(list(myquery))