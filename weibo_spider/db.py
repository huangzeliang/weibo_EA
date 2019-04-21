import pymongo
conn = pymongo.MongoClient(host="127.0.0.1",port=27017,tz_aware=False)
print (conn.database_names())
db = conn.get_database("weibo_EA")
print(db.collection_names())
account = db.get_collection("weibo")
account.find_one()
# account.insert({"name": "mike", "active_time": "20130408"})

def insert_json(dict):
    account.insert(dict)

def insert(title,text,comments):
    account.insert({"title":title,"article": text, "comments": comments})
