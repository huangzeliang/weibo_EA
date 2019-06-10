import pymongo
conn = pymongo.MongoClient(host="127.0.0.1",port=27017,tz_aware=False)
db = conn.get_database("weibo_EA")
print(db.collection_names())
account = db.get_collection("weibo")

import bson
# {"title":"李诞","article": text, "comments": text}


def get_name(title):
    return account.find({"title": title})
    pass

def get_article(title):
    """返回 article str"""
    article=[x['article'] for x in account.find({"title": title})]
    return article[0]

def get_article_list(title):
    article = [x['article'] for x in account.find({"title": title})]
    return article[0]

def get_news_by_keyword(page=1,limit=10,keyword=""):
    '''{"tname": {$regex: '测试', '''
    news = [x for x in account.find({"title":{'$regex': keyword}},skip=page*limit, limit=limit)]
    for i in news:
        i.pop('_id')
    return news


def get_comments(title):
    '''获取comments 返回list'''
    # comments=[x['comments'] for x in  account.find({"title": title})]
    comments=account.find({"title": title})[0]['comments']
    return comments

def get_news(page=1,number=10):
    '''返回list'''
    cursor_iter=account.find_raw_batches(skip=(page-1)*number,max_scan=page*number)

    for batch in cursor_iter:
        result =bson.decode_all(batch)
    for i in result:
        i.pop('_id')
    return result


def category_count_from_mongo():

    key = ['category']
    # condition = {
    #     'time': {
    #         '$gte': start_time,
    #         '$lte': end_time,
    #     }
    # }

    func = '''
            function(obj,prev)
            {
                prev.count++;
            }'''

    initial = {'count': 0}
    # reducer = Code("""
    #  function(obj, prev) {
    #  prev.count = prev.count + obj.amount
    #  }
    # """)

    ret = account.group(key,None, initial,func)
    result={x['category']:x['count'] for x in ret   }
    return result