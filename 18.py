# 18.What is the average age of each bird given that their no. of visits is 2 and priority is yes.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.aggregate([
    {
        "$match":{"visits":{"$eq":2}}
    },
    {
        "$match":{"priority":{"$eq":"yes"}}
    },
    {
        "$group":
        {
        "_id":"$visits",
        "Toatal age":{"$sum":"$age"},
        "average age":{"$avg":"$age"}
        }
    } 

])    
  
print(list(myquery))