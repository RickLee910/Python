import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_eager_execution()
# 加上以下两句才可以使用matplot,不知为何
import matplotlib

matplotlib.use('TkAgg')
# 加上以上两句才可以使用matplot,不知为何

import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):  # None即没有激活函数即表示线性函数
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))  # 变量矩阵，行列分别是in_size,out_size
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)  # 不推荐biases为0，因此加上一个0.1
    Wx_plus_b = tf.matmul(inputs, Weights) + biases  # 这时候，Wx_plus_b存储着没有被激活的结果
    if activation_function is None:  # None表示他现在是线性关系
        outputs = Wx_plus_b  # 既然是线性关系，则没有必要加上激活函数,保持现状就ok
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  # -1到1的区间，有300行，后面是维度
noise = np.random.normal(0, 0.05, x_data.shape)  # 人为制造噪点，使之看起来更像真实数据，mean值是0，方差是0.05，格式与x_data是一样的格式
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 第一个隐藏层
prediction = add_layer(l1, 10, 1, activation_function=None)  # 输出层

# 开始预测
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))  # 对每个粒子的差值求平方，再求和，再求平均
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 0.1是学习率(通常小于1)。此句表示以0.1的效率对误差进行更正，然后下一次就会有更好的结果

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)  # 只有run以后才开始执行

fig = plt.figure()  # 生成一个图片框
ax = fig.add_subplot(2,2,2)
ax.scatter(x_data, y_data)
plt.ion()  # 可以使得plt暂停后继续往下运行，而不是停住
plt.show()

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 20 == 0:
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))#每50步打印一次
        try:
            ax.lines.remove(lines[0])  # 抹除刚刚画出的这一条线
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r_', lw=2)  # 红色，线宽5
        plt.pause(0.1)  # 暂停一下。由于上面已经有plt.ion，所以这里不会一直暂停下去

