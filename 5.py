# 5. select [2, 3, 7] rows and in columns ['birds', 'age', 'visits']
# select [2,4,6]

import pymongo
import pandas as pd
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)

for i in [2,4,6]:
    myquery = mycol.find({},{"_id":1,"birds":1,"age":1,"visits":1}).skip(i).limit(1)
    print(list(myquery))
