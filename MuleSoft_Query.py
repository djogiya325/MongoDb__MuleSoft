import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = conn["MuleSoft"]

myColl = mydb["Movies"]

mydict = [ 
    {"name": "Veer", "actor": "Salman Khan",    "actress": "Zareen Khan",   "Director": "Anil Sharma",       "year_of_release": 2010},
    {"name": "Bhuj", "actor": "Ajay Devagan",   "actress": "Sonakshi Sinha","Director": "Abhishek Dudhaiya", "year_of_release": 2021},
    {"name": "PK",   "actor": "Aamir Khan",     "actress": "Anushka Sharma","Director": "Rajkumar Hirani",   "year_of_release": 2014},
    {"name": "Raees","actor": "Shah Rukh Khan", "actress": "Mahira Khan",   "Director": "Rahul Dholakia",    "year_of_release": 2017}
]
datas = myColl.insert_many(mydict)

for data in myColl.find():
    print(data)
    
for actor in myColl.find({},{ "name": 1, "actor": 1 }):
  print(actor)
    

# print(datas.inserted_ids)
# print(conn.list_database_names())