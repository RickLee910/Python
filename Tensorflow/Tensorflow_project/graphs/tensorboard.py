'''
TensorFlow 使用 TensorBoard 来提供计算图形的图形图像。这使得理解、
调试和优化复杂的神经网络程序变得很方便。TensorBoard 也可以提供有关网
络执行的量化指标。它读取 TensorFlow 事件文件，其中包含运行 TensorFlow
会话期间生成的摘要数据。

'''
import numpy as np
a = np.arange(10)
a = a.reshape([2,5])
print(a)