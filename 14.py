# 14. Sort dataframe (birds) first by the values in the 'age' in decending order, then by the value in the 'visits' column in ascending order.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

# age column in decending order
myquery = mycol.find().sort("age",-1)
print(list(myquery))

# visits column in ascending order
myquery = mycol.find().sort("visits",1)
print(list(myquery))

