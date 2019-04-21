#!/usr/bin/python
#coding: utf-8
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import base64

from snownlp import SnowNLP
#测试用
def  emotionParser_from_str(strs):
    '''传入list'''
    comments=strs
    sentimentslist = []
    for item in comments:
        try:
            sentimentslist.append(SnowNLP(item).sentiments)
        except ZeroDivisionError as e:
            print (e)


    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor="#4F8CD6")

    plt.savefig("./Analysis/test.png")

    # plt.show()

    plt.close()
    with open("./Analysis/test.png", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    f.close()
    return s


#从数据库中读取
def emotionParser(*names):
    conn = conn = sqlite3.connect("./Analysis/deal_data.db")
    conn.text_factory = str
    cursor = conn.cursor()
    likeStr = ""
    for i in range(0, len(names)):
        likeStr = likeStr +  "like \"%" + names[i] + "%\" "
        if i + 1 < len(names):
            likeStr = likeStr + " or "
    print (likeStr)


    #get sentiments
    cursor.execute("select content from realData where content " + likeStr)
    values = cursor.fetchall()
    sentimentslist = []
    for item in values:
        # print SnowNLP(item[0].decode("utf-8")).words
        sentimentslist.append(SnowNLP(item[0]).sentiments)



    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor="#4F8CD6")
    # plt.xlabel("Sentiments Probability")
    # plt.ylabel("Quantity")
    # plt.title("Analysis of Sentiments for Lidan")
    plt.savefig("./Analysis/test.png")

    # plt.show()

    cursor.close()
    conn.close()
    plt.close()

    with open("./Analysis/test.png", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    f.close()
    return s

if __name__ == '__main__':
    emotionParser("李诞")