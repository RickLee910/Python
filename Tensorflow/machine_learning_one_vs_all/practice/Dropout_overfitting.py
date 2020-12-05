import tensorflow.compat.v1 as tf
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split #从.cross_validaion 迁移到 .model_selection
tf.disable_eager_execution()
#load data
digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y) #表示成二进制数位
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)

def add_layer(inputs, in_size, out_size,layer_name,activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))#从符合指定正态分布的曲线中随机取值
    bias = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs,Weights) + bias #Dropout 随机去除50%的值
    Wx_plus_b = tf.nn.dropout(Wx_plus_b,keep_prob)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    tf.summary.histogram(layer_name+'/outputs',outputs)
    return outputs


keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32,[None,64]) #8*8 的空间
ys = tf.placeholder(tf.float32,[None,10]) #10 空间，对应123456789
#add outlayer
l1 = add_layer(xs,64,50,'l1',activation_function=tf.nn.tanh)
prediction = add_layer(l1,50,10,'l2',activation_function=tf.nn.softmax)


cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
tf.summary.scalar('loss',cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.6).minimize(cross_entropy)

sess = tf.Session()
merged = tf.summary.merge_all()


#summary writer goes in here
train_writer = tf.summary.FileWriter('logs/train',sess.graph)
test_writer = tf.summary.FileWriter('logs/test',sess.graph)
sess.run(tf.initialize_all_variables())
for i in range(500):
    sess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:0.5}) #保留一半的值
    if i % 50==0:
        #record loss
        train_res = sess.run(merged,feed_dict={xs:X_train,ys:y_train,keep_prob:1}) #保留所有的res
        test_res = sess.run(merged,feed_dict={xs:X_test,ys:y_test,keep_prob:1})
        train_writer.add_summary(train_res,i)
        test_writer.add_summary(test_res,i)
