import requests
import json
import time
from get_news_detail import get_news_details
import pandas
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def get_news_details_urls(url):
    res = requests.get(url, headers=header)
    jd = json.loads(res.text)
    newsdetails = []
    for ent in jd['result']['data']:
        links = ent['url']
        print(links)
        newsdetails.append(get_news_details(links))
    print(newsdetails)
    return newsdetails


def get_more_news_details_urls(start, end):
    news_total = []
    for one in range(start, end):
        print('page: ', one)
#       print(url.format(one))
        newsary = get_news_details_urls(url.format(one))
        news_total.extend(newsary)
        time.sleep(2)
    print(len(news_total))
    df = pandas.DataFrame(news_total)
    df.to_excel('sina_news12.xlsx')

#get_more_news_details_urls(1,30)
get_news_details_urls(url)
