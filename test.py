# -*- coding: utf-8 -*-
"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""


import os,sys
print(sys.path[0])
import json
from Analysis.Analysis import TR4,get_keywords,get_all_text,get_emotion,get_summary,get_hot_word,get_news_list_by_keyword
from Analysis.get_data import *

# print (type(get_hot_word()))

# dict={'a':'b','c':"d"}
# print (dict)
# c=['1','2']
# print (type(get_summary()))
#
# print (json.dumps([2*x for x in dict.keys() ]))
# print (json.dumps(get_summary()))
# a=get_news_list_by_keyword('')
# print (type(a))
# print (a)
#
# print ([ x['title'] for x in a])
a,b=get_emotion("徐克再拍武侠，金庸的棺材板恐怕压不住了丨毒药推荐")
result={'正向':0,'中向':0,'负向':0}
for x in b:
    if x>0.6:
        result['正向']=result['正向']+1
    else:
        if  x<0.4:
            result['负向'] = result['负向'] + 1
        else:
            result['中向'] = result['中向'] + 1

print (result)
data=[]
for name, value in result.items():
    data.append({'value': value, 'name': name})
    print (data)
