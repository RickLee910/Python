import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()
def narmalize(X):
    mean = np.mean(X)
    std = np.std(X)
    X = (X - mean) / std
    return X

boston = tf.compat.v1.contrib