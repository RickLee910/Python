import tensorflow.compat.v1 as tf
import numpy as np
import os
tf.disable_eager_execution()
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'

#save to file
#remember to define the same dtype and shape when restore
# W = tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name='weight')
# bias = tf.Variable([[1,2,3]],dtype=tf.float32,name='bias')
#
# init = tf.initialize_all_variables()
#
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess,'my_net/save_net.ckpt')
#     print('Save to path:',save_path)

#神经网络目前还不能保存框架，所以需要重新定义框架然后把变量存进来
#restore varibles
# rededine the same shape and same type for your variables
W = tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name='weight')
bias = tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name='bias')

#do not need init step
saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess,'my_net/save_net.ckpt')
    print('weight',sess.run(W))
    print('bias',sess.run(bias))