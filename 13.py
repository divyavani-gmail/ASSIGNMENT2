# 13. Find the number of each type of birds in dataframe (Counts)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]


myquery = mycol.aggregate([{"$group":{"_id":"$birds","count":{"$sum":1}}}])
print(list(myquery))