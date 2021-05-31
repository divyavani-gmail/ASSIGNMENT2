# 4. Print all the rows with only 'birds' and 'age' columns from the dataframe  
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.find({},{"_id":0,"birds":1,"age":1})
print("Birds and age columns:\n",list(myquery))