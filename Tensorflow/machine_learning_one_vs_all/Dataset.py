import scipy.io as sc
import numpy as np
def load_data(path):
    data = sc.loadmat(path)
    X = data['X']
    y = data['y']
    return X,y

X, y = load_data('ex3data1.mat')
print(np.unique(y))  # 看下有几类标签
# [ 1  2  3  4  5  6  7  8  9 10]

# ((5000, 400), (5000, 1))