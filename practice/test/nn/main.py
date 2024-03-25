# !usr/bin/env python
# -*- coding:utf-8 _*-
from tqdm import tqdm

from NN import *
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

x = np.arange(0, 2 * np.pi, 0.01)
x = x.reshape((len(x), 1))
y = (np.sin(x) + 1.0) / 2.0

yt = np.array(y).ravel()
xs = np.array(x).ravel()

'''
绘制三角函数曲线，然后根据x和y值来来训练该网络
'''

layer1 = LinearLayer(input_shape=1, output_shape=10)
layer2 = LinearLayer(input_shape=10, output_shape=10)
layer3 = LinearLayer(input_shape=10, output_shape=10)
layer4 = LinearLayer(input_shape=10, output_shape=1)

'''
4个线性层组成的很简单全连接神经网络
'''

network = NetWork([layer1,
                   Sigmoid(),
                   layer2,
                   Sigmoid(),
                   layer3,
                   Sigmoid(),
                   layer4,
                   Sigmoid()
                   ])

for i in tqdm(range(100000)):
    flag = i
    i = i % len(x)

    predict = network.Forward(x[i])
    network.Backward(predict=predict[0], label=yt[i], loss_grad_fn=MSELossGrad)
    network.Update()

    if flag % 10000 == 0:
        print(predict[0] - yt[i])

y = [network.Forward([_])[0][0] for _ in x]

plt.plot(x, y)
plt.plot(x, yt)
plt.show()

