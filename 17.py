# 17 What is the average age of Cranes given priority is yes.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.aggregate([
    {
        "$match":{"birds":{"$eq":"Cranes"}}
    },
    {
        "$match":{"priority":{"$eq":"yes"}}
    },
    {
        "$group":
        {
        "_id":"$birds",
        "Toatal age":{"$sum":"$age"},
        "average age":{"$avg":"$age"}
        }
    } 

])    
  
print(list(myquery))

