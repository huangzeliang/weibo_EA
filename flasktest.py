from flask import Flask, render_template, url_for, request, json,jsonify
from Analysis.Analysis import TR4,get_keywords,get_all_text,get_emotion,get_summary,get_hot_word
app = Flask(__name__)
import sys
sys.path.append("/Users/zel/PycharmProjects/weibo_EA/venv/lib/python3.7/site-packages")

a=""

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/testget',methods=['get'])
def testget(name='sdfs'):
    get = request.args['name']
    return render_template('test.html', name=get)


@app.route('/test',methods=['get'])
def test(name='sdfs'):
    get = request.args['name']
    return render_template('a.html', name=get)



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

    a=get_emotion(title)
    print('===================show_emotion_png=======================')
    return json.dumps(a)

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
