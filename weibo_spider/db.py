import pymongo
import bson
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



def get_news(page=1,number=10):
    cursor_iter=account.find_raw_batches(skip=(page-1)*number,max_scan=page*number)
    #跳过x个->直到 max_scan个

    for batch in cursor_iter:
        result =bson.decode_all(batch)
    for i in result:
        i.pop('_id')
    return result


def get_news_iter():
    cursor_iter=account.find_raw_batches(batch_size=1)
    return cursor_iter

def change_data(search={},set={}):
    account.update(search,set);


#find_raw_batches(filter=None, projection=None,
# skip=0, limit=0, no_cursor_timeout=False, cursor_type=CursorType.NON_TAILABLE,
# sort=None, allow_partial_results=False, oplog_replay=False, modifiers=None, batch_size=0,
# manipulate=True, collation=None, hint=None, max_scan=None, max_time_ms=None, max=None, min=None,
# return_key=False, show_record_id=False, snapshot=False, comment=None)




# >> > import bson
# >> > cursor = db.test.find_raw_batches()
# >> > for batch in cursor:
#     ...
#     print(bson.decode_all(batch))
#
# from bson.objectid import ObjectId
#
# # The web framework gets post_id from the URL and passes it as a string
# def get(post_id):
#     # Convert from string to ObjectId:
#     document = client.db.collection.find_one({'_id': ObjectId(post_id)})