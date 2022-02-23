import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/") # Make connection in MongoDB

mydb = conn["MuleSoft"] # Create Database

# print(conn.list_database_names()) # Check Existing Database
    
myColl = mydb["Movies"] # Create Collection
   
# print(mydb.list_collection_names()) #Check Existing Collections



#          **********          Insert One Record          **********          
# rec1 = {"name":"Pushpa","actor":"Allu Arjun","actress":"Rashmika Mandanna","Director":"Rajkumar","year_of_release": 2021}
# newRec = myColl.insert_one(rec1)
# print(newRec.inserted_id)



#          **********          Insert Many Records          **********          
mydict = [ 
    {"name": "Veer", "actor": "Salman Khan",    "actress": "Zareen Khan",   "Director": "Anil Sharma",       "year_of_release": 2010},
    {"name": "Bhuj", "actor": "Ajay Devagan",   "actress": "Sonakshi Sinha","Director": "Abhishek Dudhaiya", "year_of_release": 2021},
    {"name": "PK",   "actor": "Aamir Khan",     "actress": "Anushka Sharma","Director": "Rajkumar Hirani",   "year_of_release": 2014},
    {"name": "Raees","actor": "Shah Rukh Khan", "actress": "Mahira Khan",   "Director": "Rahul Dholakia",    "year_of_release": 2017}
]
datas = myColl.insert_many(mydict)
print(datas.inserted_ids)




#          **********          Find first Record          **********          
# x = myColl.find_one()

# print(x)



#          **********          Print all records in the collection          **********          
for data in myColl.find():
# for data in myColl.find().limit(2):

    # print(data)
    
    
    
#          **********          Print only selected records          **********          
# for actor in myColl.find({},{ "name": 1, "actor": 1 }):
#   print(actor)



#          **********          Find With particular data          **********          
# myquery = {"name":"Raees"}
# moydoc = myColl.find(myquery)
# for x in moydoc:
#   print(x)



#          **********          Sort the data          **********          
# mydoc = myColl.find().sort("actor")
# for x in mydoc:
#   print(x)



#          **********          Delete particular Data          **********          

# myquery = {"name":"Raees"}
# myquery = {"year_of_release" : {"$gt":2017}}

# myColl.delete_one(myquery)



#          **********          Delete all documents in collection          **********          

# x = myColl.delete_many({})
# print(x.deleted_count,"Documents Deleted...")



#          **********          Update given record          **********          
# prevRec = {"actor":"Aamir Khan"} 
# recUpdate = {"$set": {"actor":"Sushant Singh Rajput"}}
      
# myColl.update_one(prevRec,recUpdate)

# prevRec = {"actor" : { "$regex" : "^S"}  }
# recUpdate = { "$set" : { "actor" : "Ram Pothineni" } }
      
# x = myColl.update_many(prevRec,recUpdate)

# print(x.modified_count, "Document Updated !!")



#          **********          Drop Collection          **********          
# myColl.drop()
