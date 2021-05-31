# 3. Print the first 2 rows of the birds dataframe

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

print("Two rows of the Database:\n",list(mycol.find().limit(2)))
    

