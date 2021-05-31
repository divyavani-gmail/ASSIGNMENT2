# 19 Replace the Nan values in Age column by taking median values of all the age of birds

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["divya_db"]
mycol = mydb["vani_data"]

myquery = mycol.aggregate([
    {
    "$match": {
      "age": {
        "$exists": True
      }
    }
  },
  { 
    "$group": {
      "_id": None, 
      "count": { 
        "$sum": 1 
      }, 
      "values": { 
        "$push": "$age" 
      } 
    } 
  }, 
  { 
    "$unwind": "$values" 
  },
  { 
    "$sort": { 
      "values": 1
    } 
  }, 
  {
    "$project": { 
      "count": 1, 
      "values": 1, 
      "midpoint": { 
        "$divide": [
          "$count", 
          2 
        ] 
      }
    }
  },
  {
    "$project": {
      "count": 1,
      "values": 1,
      "midpoint": 1,
      "high": { 
        "$ceil": "$midpoint"
      },
      "low": {
        "$floor": "$midpoint"
      }
    }
  },
  {
    "$group": {
      "_id": None,
      "values": {
        "$push": "$values"
      }, 
      "high": {
        "$avg": "$high"
      },
      "low": {
        "$avg": "$low"
      }
    }
  }, 
  {
    "$project": {
      "beginValue": {
        "$arrayElemAt": ["$values" , "$high"]
        } ,
      "endValue": {
         "$arrayElemAt": ["$values" , "$low"]
      }
    }
  },
  {
    "$project": {
      "median": {
        "$avg": ["$beginValue" , "$endValue"]
      }      
    }
  }
  
])

for i in list(myquery):
    print(i['median'])

myquery = {"age":None}
newvalue = {"$set":{"age":4.0}}
result = mycol.update_one(myquery,newvalue)
print(list(mycol.find({},{"age":1,"_id":0})))