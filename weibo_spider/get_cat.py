from get_category.get_category_mongo import *
from db import *
import bson

#
# print (get_category("我是一个机器人"))

news=get_news_iter()
for x in news:
    news=bson.decode_all(x)[0]
    if (not news.__contains__('category')):
        category=get_category(news['article'])
        change_data({'url':news['url']},{'$set':{'category':category}})
