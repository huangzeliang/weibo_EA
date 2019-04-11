from flask import Flask, render_template, url_for, request, json,jsonify
from Analysis.Analysis import TR4,get_keyword,get_all_text,get_emotion,get_summary,get_hot_word
app = Flask(__name__)
import sys
sys.path.append("./venv/lib/python3.7/site-packages/")

a=""

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/test',methods=['get'])
def test():
    print("===============test=================")
    Scientific={"xAxis": {"type":"category","data":["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
          "yAxis": {"type":"value"},"series": [{"data": [800, 932, 901, 90, 1290, 1330, 1390],
                                                "type": "line"}],
          "test":[{"name":"ad","value":"1212"},
                  {"name":"adsds","value":"1212"},
                  {"name":"adsdsd","value":"1212"}]}
    return render_template('test.html', name = Scientific)


@app.route('/keywords', methods=['post'])
def keywords(name='sdfs'):
    # a=request.get_data()
    # return json.dumps({"test":[{"name":"ad","value":"1212"}]})
    print ("==================keywords_wordcloud===================")
    # print (get_keyword())
    return json.dumps(get_keyword())


@app.route('/alltext', methods=['post'])
def all_text(name='sdfs'):
    # a=request.get_data()
    print ("=================alltext=============================")
    return json.dumps(get_all_text())


@app.route('/emotion', methods=['post'])
def emotion(name='sdfs'):
    print ('===================get_emotion=======================')

    a=get_emotion()
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
    a=get_summary()
    print(a)
    return json.dumps(a)

@app.route('/hotwords', methods=['post'])
def hotwords(name='sdfs'):
    print ("==================hotwords======================")
    a=get_hot_word()
    # print(a)
    return json.dumps([x for x in a.keys() ])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
