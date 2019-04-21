import requests
import chardet
from lxml import etree
import html
import json
import re



# http://www.sohu.com/a/308307157_260616
# http://www.sohu.com/a/308267578_428290?code=229c65dcb7c0cd3bf416a2b9f5aa238e
# //www.sohu.com/a/308334451_463728
#url='//www.sohu.com/a/308334451_463728'




class page_paser():
    url=''
    mid=''
    def __init__(self, url):
        self.url=url
        if(re.search('http', url)==None):
            self.url='http:'+url
        else :
            self.url=url
        #获取mid
        it = re.finditer(r"(?<=a\/).*(?=\_)", self.url)
        for match in it:
            self.mid=match.group()
            print(match.group())
        html_text = requests.get(self.url).content
        self.selector = etree.HTML(html_text, parser=etree.HTMLParser(encoding='utf-8'))

    def get_content(self):
        '''返回str:title   and str:content'''
        news_list = self.selector.xpath('//article[@class="article"]//p')
        contents=[ x.text for x in news_list]
        content=''
        for x in contents:
            if x!=None:
                content = content+x

        return contents[0],content
    # 评论
    # http://apiv2.sohu.com/api/comment/list?callback=jQuery&page_size=10&topic_id=14760210&page_no=1&source_id=mp_308267578&_=1555409054478
    # callback-no  page_size-10  topic_id-no page_no-页数！！！！！ source_id-唯一指定  _session
    def get_comments(self):
        a=1
        page=0
        page_size=30#最大就是30
        all_commits=[]
        while a==1:
            page=page+1
            commentsajax='http://apiv2.sohu.com/api/comment/list?callback=jQuery&page_size={0}&topic_id=14760210&page_no={1}&source_id=mp_{2}&_=1555409054478'.format(page_size,page,self.mid)
            # print(commentsajax)
            html_text = requests.get(commentsajax).content
            it=re.finditer(r"(?<=jQuery\().*(?=\);)",html_text.decode('utf-8'))

            for match in it:
                commits = match.group()
                # print(json.loads(commits)['jsonObject']['comments'][0]['content'])
                if json.loads(commits)['jsonObject']['comments']==[]:
                    a=0
                for x in json.loads(commits)['jsonObject']['comments']:
                    all_commits.append(x['content'])
        return all_commits


if __name__=="__main__":
    a=page_paser("http://www.sohu.com/a/308267578_428290?code=229c65dcb7c0cd3bf416a2b9f5aa238e")
    title,content=a.get_content()
    print(title,content)
    print (a.get_commits())
