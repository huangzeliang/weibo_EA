from textrank4zh import TextRank4Keyword, TextRank4Sentence
from snownlp import SnowNLP
from Analysis.LiDanEmotionParser import emotionParser
import sqlite3
import sys
from Analysis.hot_word_find.demo_run import get_hot_words

summary_lenth=3000
sumary_number=3

class TR4:
    try:
        sys.setdefaultencoding('utf-8')
    except:
        pass

    def res_format(self,res):
        resformat = []
        for i in res:
            resformat.append({'name': i['word'], 'value': int(i['weight'] * 10000)})
        return resformat

    def tr_word(self,text=''):
        #tr4w = TextRank4Keyword(stop_words_file='./stopword.data')
        tr4w = TextRank4Keyword(stop_words_file='./Analysis//stopword.data')

        tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

        return self.res_format(tr4w.get_keywords(200, word_min_len=1))




def get_keyword():

    with open('./Analysis/a.txt', 'r') as f:
        text = f.read()
        # print (text)
        f.close()


    s =  TR4().tr_word(text)
    return s

def get_all_text():
    with open('./Analysis/a.txt', 'r') as f:
        text = f.read()
        f.close()
    return text



def sql_to_text():
    conn = conn = sqlite3.connect("deal_data.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("select content from realData where content like '%薛教授%'" )
    values = cursor.fetchall()
    sentimentslist = []
    f = open('a.txt', 'a')
    for item in values:
        print (item)
        f.write(item[0])
        print (type(item))
        # print SnowNLP(item[0].decode("utf-8")).words
        #sentimentslist.append(SnowNLP(item[0].decode("utf-8")).sentiments)
    cursor.close()
    conn.close()
    f.close()

def get_emotion():
    return emotionParser('薛教授')



def get_summary():
    with open('./Analysis/a.txt', 'r') as f:
        text = f.read()
        f.close()

    return SnowNLP(text[0:3000]).summary(3)

def get_hot_word():
    hot_words=get_hot_words()
    return hot_words



if __name__ =='__main__':
    print (get_hot_word())