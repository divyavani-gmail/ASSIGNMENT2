# 2. Display a summary of the basic information about birds DataFrame and its data. I want information like mean variance,std-dev,min,max and percentiles
import pymongo
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)
         
myquery = mycol.aggregate([
    {
        "$group":
        {
        "_id":"age",
        "average age":{"$avg":"$age"}
        }
    } 

])
print(list(myquery))