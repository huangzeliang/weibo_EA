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

# print (type(get_hot_word()))

# dict={'a':'b','c':"d"}
# print (dict)
# c=['1','2']
# print (type(get_summary()))
#
# print (json.dumps([2*x for x in dict.keys() ]))
# print (json.dumps(get_summary()))
a=get_news_list_by_keyword('')
print (type(a))
print (a)

print ([ x['title'] for x in a])