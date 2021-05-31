# 10. Find the total number of visits of the bird Cranes

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]


myquery = mycol.aggregate([
    {
        "$match":{"birds":{"$eq":"Cranes"}}
    },
    {
        "$group":{    
            "_id":"visits",
            "Total Number":{"$sum":"$visits"}
        }
    }
])
print(list(myquery))
