import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])

product = tf.matmul(matrix1,matrix2) #matrix multiply  np.dot(m1,m2)

# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()
# with tf.Session() as sess:
#     res = sess.run(product)
#     print(res)

state = tf.Variable(0,name='counter') #必须定义是变量才是变量
#print(state.name)
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)
init = tf.initialize_all_variables() #must have if define variable
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))