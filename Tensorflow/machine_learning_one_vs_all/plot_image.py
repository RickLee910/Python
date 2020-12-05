import scipy.io as sc
import numpy as np
import matplotlib.pyplot as plt

def load_data(path):
    data = sc.loadmat(path)
    X = data['X']
    y = data['y']
    return X,y

def plot_1_image(X,y):
    pick_one = np.random.randint(0,5000)
    image = X[pick_one,:]
    fig,ax = plt.subplots(figsize= (2,2))#小图的大小
    ax.matshow(image.reshape((20,20)), cmap='gray_r') #cmap:热力图颜色
    plt.xticks([]) # 去除刻度，美观
    plt.yticks([])
    plt.show()
    print('This should be {}'.format(y[pick_one]))

def plot_100_image(X):
    sample_idx = np.random.choice(np.arange(X.shape[0]),100)
    sample_images = X[sample_idx,:]
    fig,ax_array = plt.subplots(nrows=10,ncols=10,sharey=True,sharex=True,figsize = (8,8))#sharex,sharey：布尔值或者{'none','all','row','col'}，默认：False
                    #控制x(sharex)或y(sharey)轴之间的属性共享：
                        #1.True或者'all'：x或y轴属性将在所有子图(subplots)中共享.
                        #2.False或'none'：每个子图的x或y轴都是独立的部分
                        #3.'row'：每个子图在一个x或y轴共享行(row)
                        #4.'col':每个子图在一个x或y轴共享列(column)
    for row in range(10):
        for col in range(10):
            ax_array[row,col].matshow(sample_images[10*row + col].reshape((20,20)),cmap = 'gray')
    plt.xticks([])  # 去除刻度，美观
    plt.yticks([])
    plt.show()
X,y = load_data('ex3data1.mat')
plot_100_image(X)

