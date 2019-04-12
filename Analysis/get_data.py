import pymongo
conn = pymongo.MongoClient(host="127.0.0.1",port=27017,tz_aware=False)
db = conn.get_database("weibo_EA")
print(db.collection_names())
account = db.get_collection("weibo")
# {"title":"李诞","article": text, "comments": text}


def get_name(title):
    return account.find({"title": title})
    pass

def get_article(title):
    article=[x['article'] for x in account.find({"title": title})]
    return article


def get_comments(title):
    comments=[x['comments'] for x in  account.find({"title": title})]
    return comments