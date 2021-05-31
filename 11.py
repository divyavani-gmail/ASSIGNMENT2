# 11. Calculate the mean age for each different birds in dataframe.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.aggregate([
    {
        "$group":
        {
        "_id":"$birds",
        # "Toatal age":{"$sum":1},
        "average age":{"$avg":"$age"}
        }
    } 

])
print(list(myquery))