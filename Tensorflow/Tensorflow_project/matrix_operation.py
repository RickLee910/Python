import tensorflow as tf
tf.compat.v1.disable_eager_execution()
#Start an Interactive Session
sess = tf.compat.v1.InteractiveSession()

#Define a 5*5 Identity matrix
I_matrix = tf.eye(5)
#print it
print(I_matrix.eval())

#Define a Variable initialized to a 10 * 10 identity matrix
X = tf.Variable(tf.eye(10))
X.initializer.run()
print(X.eval())

A = tf.Variable(tf.compat.v1.random_normal([5,10]))
A.initializer.run()
print('A = ',A.eval())
#Muti two matrices
product = tf.matmul(A,X)
print('product = ',product.eval())
#create a random matrix of 1s and 0s,size 5*10
b = tf.Variable(tf.compat.v1.random_uniform([5,10], 0 , 2, dtype=tf.int32))
b.initializer.run()
print(b.eval())
b_new = tf.cast(b, dtype=tf.float32)
print('b_new\n',b_new.eval())
#Cast to float32 dtype

#Add two matrix
t_sum = tf.add(product, b_new)
t_sub = product - b_new
print("A*X + b\n", t_sum.eval())
print("A*X - b\n", t_sub.eval())