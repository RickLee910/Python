import tensorflow as tf
tf.compat.v1.disable_eager_execution()
a = tf.Variable(tf.compat.v1.random_normal([4,5],stddev=2))
b = tf.Variable(tf.compat.v1.random_normal([4,5],stddev=2))

A = a * b

#Multiplication with a scalar 2
B = tf.scalar_mul(2,A)
#Elementwise division, its result is
C = tf.compat.v1.divide(a,b)
#Elementwise remainder of division
D = tf.compat.v1.mod(a,b)

init_op = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    writer = tf.compat.v1.summary.FileWriter('graphs', sess.graph)
    a,b,A_R,B_R,C_R,D_R=sess.run([a,b,A,B,C,D])
    print('a\n',a,'\nb\n',b,'\nA_R\n',A_R,'\nB_R\n',B_R,'\nC_R\n',C_R,'\nD_R\n',D_R)
writer.close()

