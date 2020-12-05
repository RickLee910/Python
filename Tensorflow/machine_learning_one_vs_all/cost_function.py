import numpy as np
import sigmoid as sg
def regularized_cost(theta, X,y,l):
    thetaReg = theta[1:]
    first = (-y*np.log(sg.sigmoid(X@theta))) + (y - 1)*np.log(1 - sg.sigmoid(X@theta))
    reg = (thetaReg@thetaReg) * l / (2 * len(X))
    return np.mean(first) + reg

def regularized_gradient(theta, X, y, l):
    """
    don't penalize theta_0
    args:
        l: lambda constant
    return:
        a vector of gradient
    """
    thetaReg = theta[1:]
    first = (1 / len(X)) * X.T @ (sg.sigmoid(X @ theta) - y)
    # 这里人为插入一维0，使得对theta_0不惩罚，方便计算
    reg = np.concatenate([np.array([0]), (l / len(X)) * thetaReg])
    return first + reg