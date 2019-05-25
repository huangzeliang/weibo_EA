# -*- coding: utf-8 -*-

"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""
import pickle
from .config import basedir

def get_stopwords():
    with open(basedir+'/data/stopword.txt', 'r') as f:
        stopword = [line.strip() for line in f]
    return set(stopword)


def generate_ngram(input_list, n):
    result = []
    for i in range(1, n+1):#[1.2.3] [list]中的123个词的随机组合
        result.extend(zip(*[input_list[j:] for j in range(i)]))
    return result


def load_dictionary(filename):
    """
    加载外部词频记录
    :param filename:
    :return:
    """
    word_freq = {}
    print('------> 加载外部词集')
    with open(filename, 'r') as f:
        for line in f:
            try:
                line_list = line.strip().split(' ')
                # 规定最少词频
                if int(line_list[1]) > 2:
                    word_freq[line_list[0]] = line_list[1]
            except IndexError as e:
                print(line)
                continue
    return word_freq


def save_model(model, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(model, fw)


def load_model(filename):
    with open(filename, 'rb') as fr:
        model1 = pickle.load(fr)
    return model1
