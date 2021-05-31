# 20.How many unique birds are present in data?

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find().distinct('birds')
print(len(list(myquery)))