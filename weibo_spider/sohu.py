import requests
import chardet
from lxml import etree
import html
import re

from sohu_content import page_paser
# print (html.unescape('&#x6BCD;'))#乱码
from db import insert_json

# print (chardet.detect(b'&#24052;&#40654;&#22307;&#27597;&#38498;&#22823;&#28779;&#261'.decode('utf-8')))

url="https://weibo.com/?category=7"
urlsinanews='https://www.weibo.com/login.php?url=http%253A%252F%252Fvip.weibo.com%252F'
urlsohusrc='http://news.sohu.com'
urlsohu='http://www.sohu.com/a/308268948_260616?_f=index_chan08news_1'

xpatchmodule=[
    '//div[@class="main-left left"]//a[@title]',#左侧新闻
    '//div[@class="news"]//a',#置顶文
    '//div[@class="list16"]//li/a',#热文
     '//div[@class="choice-list"]//li/a',#搜狐精选
]




#http://apiv2.sohu.com/api/comment/list?callback=jQuery&page_size=10&topic_id=14760210&page_no=&source_id=mp_308268948&_=1555409054478
#callback-no  page_size-10  topic_id-no page_no-页数！！！！！ source_id-唯一指定  _session

html_text = requests.get(urlsohusrc).content

selector = etree.HTML(html_text,parser=etree.HTMLParser(encoding='utf-8'))

news_list=selector.xpath(xpatchmodule[0])
list=[[x.xpath('./@href')[0],x.xpath('@title')[0]] for x in news_list if x]
news_list=selector.xpath(xpatchmodule[1])
list.extend([[x.xpath('./@href')[0],x.xpath('@title')[0]] for x in news_list])


news_list=selector.xpath(xpatchmodule[2])
list.extend([[x.xpath('./@href')[0],x.xpath('@title')[0]] for x in news_list])


news_list=selector.xpath(xpatchmodule[3])
list.extend([[x.xpath('./@href')[0],x.xpath('@title')[0]] for x in news_list])
#
for i in list:
    print (i)

for i in list:
    if '//www.sohu.com/a/' in i[0]:
        a = page_paser(i[0])
        try:
            title, article = a.get_content()
            comments=a.get_comments()
            result={'url':i[0],
                    'title':i[1],
                    'article':article,
                    'comments':comments
                    }
            insert_json(result)
            #{"title": title, "article": text, "comments": comments}

        except  Exception as e:
            print (e)
    # print (result)
#
# print (list)





# print (chardet.detect(html))
# print (html.decode('utf-8'))