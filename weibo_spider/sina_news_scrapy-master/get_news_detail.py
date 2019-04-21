import requests
from bs4 import BeautifulSoup

url  = 'http://news.sina.com.cn/c/nd/2018-06-30/doc-iheqpwqz3614031.shtml'
def get_news_details(news_details_url):
    web_data = requests.get(news_details_url)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('.main-title')[0].text
    #print(title)
    article = []
    for p in  soup.select('.article > p')[:-1]:
        article.append(p.text.strip())
    print('\n'.join(article))
    key_words = []
    for key_word in soup.select('.keywords > a'):
        key_words.append(key_word.text)
    print(key_words)
    data = {
        'title' : title,
        'article' : '\n'.join(article),
        'key_words' : ','.join(key_words)
    }
    return data

get_news_details(url)

