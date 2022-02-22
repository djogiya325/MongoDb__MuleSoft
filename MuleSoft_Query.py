import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")  #Connecting with localhost

mydb = conn["MuleSoft"]  #Created a database

myColl = mydb["Movies"]  #created a collection


# Insert One Record
# rec1 = myColl.insert_one("name":"Pushpa","actor":"Allu Arjun","actress":"Mandanna","Director":"Rajkumar","year_of_release": 2021)


#Inserting data in Collection

mydict = [ 
    {"name": "Veer", "actor": "Salman Khan",    "actress": "Zareen Khan",   "Director": "Anil Sharma",       "year_of_release": 2010},
    {"name": "Bhuj", "actor": "Ajay Devagan",   "actress": "Sonakshi Sinha","Director": "Abhishek Dudhaiya", "year_of_release": 2021},
    {"name": "PK",   "actor": "Aamir Khan",     "actress": "Anushka Sharma","Director": "Rajkumar Hirani",   "year_of_release": 2014},
    {"name": "Raees","actor": "Shah Rukh Khan", "actress": "Mahira Khan",   "Director": "Rahul Dholakia",    "year_of_release": 2017}
]
datas = myColl.insert_many(mydict)

#To print first record
#x = mycol.find_one()

#print(x)
#Printing data in list
for data in myColl.find():
    print(data)
    
    
 # shows movies name with actor name only
for actor in myColl.find({},{ "name": 1, "actor": 1 }):
  print(actor)
    
#to sort data     
#mydoc = myColl.find().sort("name", -1)

#To delete collection
#myColl.drop()

#Update given record
#prevRec = {"actor":"Aamir Khan"} 
#recUpdate ={"$set":  {"acotor":"Sushant Singh Rajput"} }
      
myColl.update_one(prevRec,recUpdate)
# print(datas.inserted_ids)
# print(conn.list_database_names())
