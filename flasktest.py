# -*- coding: utf-8 -*-
"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""


from flask import Flask, render_template, url_for, request, json,jsonify
from Analysis.Analysis import TR4,get_keywords,get_all_text,get_emotion,get_summary,get_hot_word,get_news_list,get_category_count
app = Flask(__name__)
import sys
sys.path.append("/Users/zel/PycharmProjects/weibo_EA/venv/lib/python3.7/site-packages")

a=""

@app.route('/')
def root():
    return render_template('news_list.html')

@app.route('/list',methods=['post'])
def get_list():
    '''获取新闻列表'''
    page = int(request.form['page'])
    number = int(request.form['number'])
    keyword=str(request.form['keyword'])
    result=get_news_list(page,number,keyword)
    for x in result:
        # print (x)
        if len(x['article'])>100:
            x['article']=x['article'][0:100]
        x['comments']=x['comments'][0:5]
        if(isinstance(x['comments'],list)):
            print ("isinstance")
            for i in range(len(x['comments'])):
                if(len(x['comments'][i])>20):
                    x['comments'][i]=x['comments'][i][0:20]

    # print (result)
    return json.dumps(result)

@app.route('/testget',methods=['get'])
def testget(name='sdfs'):
    get = request.args['name']
    return render_template('demo2.html', name=get)


@app.route('/a',methods=['get'])
def a():

    return render_template('a.html')

@app.route('/test',methods=['get'])
def test():
    return render_template('index.html')

@app.route('/demo2',methods=['get'])
def demo2():
    return render_template('demo2.html')

@app.route('/categorycount',methods=['get'])
def categorycount():
    data=[]
    # count={'体育': 0, '财经': 1, '房产': 2, '家居': 3, '教育': 4, '科技': 5, '时尚': 6, '时政': 7, '游戏': 8, '娱乐': 9}
    count=get_category_count()


    for name, value  in count.items():
        data.append({'value':value,'name':name})
    category=list(count.keys())

    result={'data':data,'category':category}
    return json.dumps(result)




# @app.route('/test',methods=['get'])
# def test():
#     print("===============test=================")
#     Scientific={"xAxis": {"type":"category","data":["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
#           "yAxis": {"type":"value"},"series": [{"data": [800, 932, 901, 90, 1290, 1330, 1390],
#                                                 "type": "line"}],
#           "test":[{"name":"ad","value":"1212"},
#                   {"name":"adsds","value":"1212"},
#                   {"name":"adsdsd","value":"1212"}]}
#     return render_template('test.html', name = Scientific)


@app.route('/keywords', methods=['post'])
def keywords(name=''):
    # a=request.get_data()
    # return json.dumps({"test":[{"name":"ad","value":"1212"}]})
    print ("==================keywords_wordcloud===================")
    title = request.form['name']
    return json.dumps(get_keywords(title))


@app.route('/alltext', methods=['post'])
def all_text(name='sdfs'):
    # a=request.get_data()
    print ("=================alltext=============================")
    title = request.form['name']
    return json.dumps(get_all_text(title))


@app.route('/emotion', methods=['post'])
def emotion(name='sdfs'):
    print ('===================get_emotion=======================')
    title = request.form['name']
    data=[]
    basestr,scores=get_emotion(title)


    score_count = {'正向': 0, '中向': 0, '负向': 0}
    for x in scores:
        if x > 0.6:
            score_count['正向'] = score_count['正向'] + 1
        else:
            if x < 0.4:
                score_count['负向'] = score_count['负向'] + 1
            else:
                score_count['中向'] = score_count['中向'] + 1

    print(score_count)
    data = []
    for name, value in score_count.items():
        data.append({'value': value, 'name': name})
    category=list(score_count.keys())

    result={'data':data,'category':category}
    print('===================show_emotion_png=======================')
    emotion = {'img': basestr, 'result': result}
    return json.dumps(emotion)

# @app.route('/s', methods=['get'])
# def sosuo(name='sdfs'):
#     keyword = request.values.get('keyword')
#
#     name= {"xAxis": {"type":"category","data":["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},"yAxis": {"type":"value"},"series": [{"data": [800, 932, 901, 90, 1290, 1330, 1390],"type": "line"}]}
#
#     name=json.dumps(name)
#
#     return render_template('index.html', name=name, keyword=keyword)

@app.route('/summary', methods=['post'])
def summary(name='sdfs'):
    print ("==================summary======================")
    title = request.form['name']
    a=get_summary(title)

    return json.dumps(a)

@app.route('/hotwords', methods=['post'])
def hotwords(name='sdfs'):
    print ("==================hotwords======================")
    title = request.form['name']
    hotwords=get_hot_word(title)
    return json.dumps(hotwords)





if __name__ == '__main__':
    app.run(host='0.0.0.0')
