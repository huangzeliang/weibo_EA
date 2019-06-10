# -*- coding: utf-8 -*-
"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""
import os,sys
import jieba


from .model import TrieNode
from .utils import get_stopwords, load_dictionary, generate_ngram, save_model, load_model
from .config import basedir

sys.path.append(basedir)


root_name = basedir + "/data/root.pkl"
print (root_name)
stopwords = get_stopwords()
if os.path.exists(root_name):
    print ("os.path.exists(root_name)")
    root = load_model(root_name)
else:
    dict_name = basedir + '/data/dict.txt'
    word_freq = load_dictionary(dict_name)
    root = TrieNode('*', word_freq)
    save_model(root, root_name)


def get_hot_words(text=''):

    # 加载新的文章
    # filename = basedir+'/data/demo.txt'
    data = load_data(text, stopwords)
    # 将新的文章插入到Root中
    load_data_2_root(data)

    # 定义取TOP5个
    topN = 10
    result, add_word = root.find_word(topN)
    # 如果想要调试和选择其他的阈值，可以print result来调整
    # print("\n----\n", result)
    # print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
    # print('#############################')
    newdata={}
    for word, score in add_word.items():

        print(word + ' ---->  ', score)
        if score>0.08:
            newdata[word]=score

    # print('#############################')

    # 前后效果对比
    test_sentence=text
    # test_sentence = '想听教授说话啊李诞不是来调节气氛的 而是不断展示自己的无知。教授都不想理你 你还在那撒泼 真的想听教授多说一些希望下次李诞不要再打断教授说话了特别想听听薛教授说什么，' \
    #                 '被李诞反复粗暴打乱，太讨厌了！这节奇葩说最讨厌李诞，薛教授说话他一直在打断，想完整的听一下教授的见解都没办法进行，很讨厌，真想堵住他的嘴！'
    # print('添加前：')
    # print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))

    for word in add_word.keys():
        jieba.add_word(word)
    # print("添加后：")
    # print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))

    # [x if add_word[x]>0.5 else None for x in add_word]
    return newdata



def load_data(text, stopwords):
    """

    :param filename:
    :param stopwords:
    :return: 二维数组,[[句子1分词list], [句子2分词list],...,[句子n分词list]]
    """
    data = []

    word_list = [x for x in jieba.cut(text, cut_all=False) if x not in stopwords]
    data.append(word_list)
    return data


def load_data_2_root(data):
    print('------> 插入节点')#['你', '是', '一只', '狗', '吗']

    for word_list in data:
        # tmp 表示每一行自由组合后的结果（n gram）
        # tmp: [['它'], ['是'], ['小'], ['狗'], ['它', '是'], ['是', '小'], ['小', '狗'], ['它', '是', '小'], ['是', '小', '狗']]
        ngrams = generate_ngram(word_list, 3)
        for d in ngrams:
            root.add(d)
    print('------> 插入成功')



# if __name__ == "__main__":
#     root_name = basedir + "/data/root.pkl"
#     stopwords = get_stopwords()
#     if os.path.exists(root_name):
#         root = load_model(root_name)
#     else:
#         dict_name = basedir + '/data/dict.txt'
#         word_freq = load_dictionary(dict_name)
#         root = TrieNode('*', word_freq)
#         save_model(root, root_name)
#
#     # 加载新的文章
#     filename = basedir+'/data/demo.txt'
#     data = load_data(filename, stopwords)
#     # 将新的文章插入到Root中
#     load_data_2_root(data)
#
#     # 定义取TOP5个
#     topN = 10
#     result, add_word = root.find_word(topN)
#     # 如果想要调试和选择其他的阈值，可以print result来调整
#     # print("\n----\n", result)
#     print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
#     print('#############################')
#     for word, score in add_word.items():
#         print(word + ' ---->  ', score)
#     print('#############################')
#
#     # 前后效果对比
#     test_sentence = '想听教授说话啊李诞不是来调节气氛的 而是不断展示自己的无知。教授都不想理你 你还在那撒泼 真的想听教授多说一些希望下次李诞不要再打断教授说话了特别想听听薛教授说什么，'\
#                     '被李诞反复粗暴打乱，太讨厌了！这节奇葩说最讨厌李诞，薛教授说话他一直在打断，想完整的听一下教授的见解都没办法进行，很讨厌，真想堵住他的嘴！'
#     print('添加前：')
#     print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))
#
#     for word in add_word.keys():
#         jieba.add_word(word)
#     print("添加后：")
#     print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))
