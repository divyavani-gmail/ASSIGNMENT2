# 12. Append a new row to dataframe with your choice of values for each column. Then delete that row to return the original DataFrame.

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

insert_row  = mycol.insert_one({"birds":"parrot","age":3,"visits":4,"priority":"yes"})

print(list(mycol.find()))
myquery = {"birds":"parrot"}

mycol.delete_one(myquery)

print(list(mycol.find()))