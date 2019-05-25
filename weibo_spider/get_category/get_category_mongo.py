#!/usr/bin/python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""

from __future__ import print_function
import os
import tensorflow.contrib.keras as kr
import tensorflow as tf
import numpy as np
from get_category.cnn_model import TCNNConfig, TextCNN


base_dir = os.path.abspath(os.path.dirname(__file__))
val_dir=os.path.join(base_dir,'cnews.val.txt')

vocab_dir=os.path.join(base_dir,'cnews.vocab.txt')
model_path=os.path.join(base_dir,'textcnn/best_validation')


#获取字典的分类

config = TCNNConfig()
model=TextCNN(config)

def get_category(str):
    print('Configuring CNN model...')


    words, word_to_id = read_vocab(vocab_dir)
    # word_to_id  dict 我：1 你：2
    cat_to_id=read_category()

    print("loading model")
    # 创建会话
    session = tf.Session()
    # print (tf.global_variables_initializer())
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=model_path)
    x_test, y_test = process_file(str,val_dir, word_to_id, cat_to_id, 600)

    #sess里 有两个dict用作feed

    batch_eval = batch_iter(x_test, y_test, 128)
    for x_batch, y_batch in batch_eval:
        batch_len = len(x_batch)
        feed_dict = feed_data(x_batch, y_batch, 1.0)
        # 预测结果
        loss, acc, category = session.run([model.loss, model.acc, model.y_pred_cls], feed_dict=feed_dict)
        print("预测结果", category)
        category_dict = {'体育': 0, '财经': 1, '房产': 2, '家居': 3, '教育': 4, '科技': 5, '时尚': 6, '时政': 7, '游戏': 8, '娱乐': 9}
        cat=list(category_dict.keys())[category[0]]


    return cat


def read_category():
    categories = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
    cat_to_id=dict(zip(categories,range(len(categories))))
    # print ("cat",cat_to_id)
    return cat_to_id


def read_vocab(vocab_dir):
    """读取词汇表"""
    # words = open_file(vocab_dir).read().strip().split('\n')
    with open(vocab_dir,"r") as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [a.strip() for a in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id

def process_file(str,filename, word_to_id, cat_to_id, max_length=600):
    #contents, labels = read_file(filename)  #获取标签 文章
    labels=['娱乐']

    #预测文本
    contents=[str]
    #cat {'体育': 0, '财经': 1, '房产': 2, '家居': 3, '教育': 4, '科技': 5, '时尚': 6, '时政': 7, '游戏': 8, '娱乐': 9}
    data_id, label_id = [], []

    for i in range(len(contents)):
        data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
        label_id.append(cat_to_id[labels[i]]) #转换成0，1
    #将语句按顺序从大到小按字拆分然后拼接 截取前600个
    x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
    y_pad = kr.utils.to_categorical(label_id, num_classes=len(cat_to_id))  # 将标签转换为one-hot表示

    return x_pad, y_pad




def evaluate(sess, x_, y_):
    batch_eval = batch_iter(x_, y_, 128)
    for x_batch, y_batch in batch_eval:

        batch_len = len(x_batch)
        feed_dict = feed_data(x_batch, y_batch, 1.0)
        #预测结果
        loss, acc,category= sess.run([model.loss, model.acc,model.y_pred_cls], feed_dict=feed_dict)

        print ("预测结果",category)
        category_dict={'体育': 0, '财经': 1, '房产': 2, '家居': 3, '教育': 4, '科技': 5, '时尚': 6, '时政': 7, '游戏': 8, '娱乐': 9}



def batch_iter(x, y, batch_size=64):
    """生成批次数据"""
    data_len = len(x)
    num_batch = int((data_len - 1) / batch_size) + 1

    indices = np.random.permutation(np.arange(data_len))
    x_shuffle = x[indices]
    y_shuffle = y[indices]

    for i in range(num_batch):
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]


def feed_data(x_batch, y_batch, keep_prob):
    feed_dict = {
        model.input_x: x_batch,
        model.input_y: y_batch,
        model.keep_prob: keep_prob
    }
    return feed_dict

