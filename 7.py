# 7 select the rows with columns ['birds', 'visits'] where the age is missing i.e NaN


import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find({"age":None},{"birds":1,"visits":1,"_id":1})
print(list(myquery))

