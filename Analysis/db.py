import pymongo
conn = pymongo.MongoClient(host="127.0.0.1",port=27017,tz_aware=False)
print (conn.database_names())
db = conn.get_database("weibo_EA")
print(db.collection_names())
account = db.get_collection("weibo")
account.find_one()
# account.insert({"name": "mike", "active_time": "20130408"})
with open ('./test.txt','r')as f:
    text=f.read()

# account.insert({"title":"李诞","article": text, "comments": text})
for a in account.find({"title":'李诞'}):
    print (a)