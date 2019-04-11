import os,sys
print(sys.path[0])
import json
from Analysis.Analysis import TR4,get_keyword,get_all_text,get_emotion,get_summary,get_hot_word

# print (type(get_hot_word()))

dict={'a':'b','c':"d"}
print (dict)
c=['1','2']
print (type(get_summary()))

print (json.dumps([2*x for x in dict.keys() ]))
print (json.dumps(get_summary()))