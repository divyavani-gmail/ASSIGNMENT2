# 16. In the 'birds' column, change the 'plovers' entries to 'trumpeters'.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]


myquery  = {"birds":"plovers"}
newvalue = {"$set":{"birds":"trumpeters"}}  
result = mycol.update_many(myquery,newvalue)

print(list(mycol.find({},{"birds":1,"_id":0})))
