from scipy.optimize import minimize
import numpy as np
import cost_function as cf
import sigmoid as sg
import Dataset as dt
def one_vs_all(X, y, l, K):
    """generalized logistic regression
    args:
        X: feature matrix, (m, n+1) # with incercept x0=1
        y: target vector, (m, )
        l: lambda constant for regularization
        K: numbel of labels
    return: trained parameters
    """
    all_theta = np.zeros((K, X.shape[1]))  # (10, 401)

    for i in range(1, K + 1):
        theta = np.zeros(X.shape[1])
        y_i = np.array([1 if label == i else 0 for label in y])

        ret = minimize(fun=cf.regularized_cost, x0=theta, args=(X, y_i, l), method='TNC',
                       jac=cf.regularized_gradient, options={'disp': True})
        all_theta[i - 1, :] = ret.x

    return all_theta


def predict_all(X, all_theta):
    # compute the class probability for each class on each training instance
    h = sg.sigmoid(X @ all_theta.T)  # 注意的这里的all_theta需要转置
    # create array of the index with the maximum probability
    # Returns the indices of the maximum values along an axis.
    h_argmax = np.argmax(h, axis=1)
    # because our array was zero-indexed we need to add one for the true label prediction
    h_argmax = h_argmax + 1

    return h_argmax

raw_X, raw_y = dt.load_data('ex3data1.mat')
X = np.insert(raw_X, 0, 1, axis=1) # (5000, 401)
y = raw_y.flatten()  # 这里消除了一个维度，方便后面的计算 or .reshape(-1) （5000，）

all_theta = one_vs_all(X, y, 1, 10)
 # 每一行是一个分类器的一组参数
y_pred = predict_all(X, all_theta)
accuracy = np.mean(y_pred == y)
print ('accuracy = {0}%'.format(accuracy * 100))