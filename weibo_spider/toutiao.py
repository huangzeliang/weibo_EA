import requests
import time
import json
import os
from hashlib import md5

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3486.0 Safari/537.36'}

path = os.getcwd()

def main():
    flag = 0
    offset = 0  # 页数
    while flag == 0:
        try:
            # 构造第一个URL
            url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E8%A1%97' \
                  '%E6%8B%8D%E7%BE%8E%E5%9B%BE&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synth' \
                  'esis&timestamp={}'.format(offset, int(round(time.time() * 1000)))
            # int(round(time.time() * 1000)) 获取13位时间戳
            response = requests.get(url=url, headers=header)
            json_text = json.loads(response.text)  # 将已编码的 JSON 字符串解码为 Python 对象
            data = json_text['data']

            # 结束判断
            if data == None:
                flag = 1

            for i in data:
                try:
                    info = {'title': '', 'pic': []}   # 数据信息字典

                    # 数据写成字典
                    info['title'] = i['title']
                    for k in i['image_list']:
                        info['pic'].append(k)

                    # 创建标题文件夹
                    if not os.path.exists(path + '\picture\{}'.format(info['title'])):
                        os.mkdir(path + '\picture\{}'.format(info['title']))

                    # 图片路径
                    pic_file = path + '\picture\{}'.format(info['title'])

                    # 下载图片
                    for j in info['pic']:
                        # print(j['url'])
                        pic_2 = requests.get(j['url'])
                        # 图片名字设为md5值
                        pic_path = path + '\picture\{}'.format(info['title']) + '\{}'.format(md5(pic_2.content).hexdigest()) + '.jpg'
                        print(pic_path)
                        if not os.path.exists(pic_path):
                            with open(pic_path, 'wb') as f:
                                f.write(pic_2.content)

                    print(info['title'], 'is finished！')
                except:
                    pass
            print(url, ' succeed!')
            offset += 20
        except:
            flag = 1
    print('succ main()')


if __name__ == '__main__':
    main()