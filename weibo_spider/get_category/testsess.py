# -*- coding: utf-8 -*-
"""
# @Time    : 2019/4/26 下午5:03
# @Author  : huangzeliang
# @File    : model.py
# @Software: PyCharm
"""

import tensorflow as tf
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
print (c)
with tf.Session():
  # We can also use 'c.eval()' here.
  print(c.eval())
