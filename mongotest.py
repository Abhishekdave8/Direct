import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.lr7ulw4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {"name": "sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test1']
coll.insert_one(d)