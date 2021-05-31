# 1. Create a DataFrame birds from this dictionary
import pymongo
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)

print(df)

# x= mycol.insert_one({"birds":"spoonbills","age":None,"visits":4,"priority":"yes"})
x=mycol.insert_many([
    {"_id": 0,"birds":"Cranes","age":3.5,"visits":2,"priority":"yes"},
    {"_id": 1,"birds":"Cranes","age":4.0,"visits":4,"priority":"yes"},
    {"_id": 2,"birds":"plovers","age":1.5,"visits":3,"priority":"no"},
    {"_id": 3,"birds":"spoonbills","age":None,"visits":4,"priority":"yes"},
    {"_id": 4,"birds":"spoonbills","age":6.0,"visits":3,"priority":"no"},
    {"_id": 5,"birds":"Cranes","age":3.0,"visits":4,"priority":"no"},
    {"_id": 6,"birds":"plovers","age":5.5,"visits":2,"priority":"no"},
    {"_id": 7,"birds":"Cranes","age":None,"visits":2,"priority":"yes"},
    {"_id": 8,"birds":"spoonbills","age":8.0,"visits":3,"priority":"no"},
    {"_id": 9,"birds":"spoonbills","age":4.0,"visits":2,"priority":"no"}
    ])                                              

print(list(mycol.find()))
