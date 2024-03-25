# !usr/bin/env python
# -*- coding:utf-8 _*-
import math
import numpy as np

'''定义神经元，这是网络层参数的一个单元，就是简单的一个数值加上这个数值对应的梯度值'''


class Neuron(object):
    def __init__(self, value: float = 1.0, grad: float = 1.0):
        self.value = value
        self.grad = grad


'''定义Layer的基类，其实正常的线性层，卷积层，这样的有参数的层以及激活函数这样的无参数的层都可以继承这个基类'''


class Layer(object):
    def __init__(self, input_shape, output_shape, pre_layer, next_layer):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.pre_layer = pre_layer
        self.next_layer = next_layer
        self.input = []
        self.output = []

    def ForwardOperator(self, *args, **kw):
        pass

    def PropagateOperator(self, *args, **kw):
        pass


'''无参数层'''


class NoParaLayer(Layer):
    def __init__(self, input_shape=None, output_shape=None, pre_layer=None, next_layer=None):
        super(NoParaLayer, self).__init__(input_shape, output_shape, pre_layer, next_layer)
        self.propagate_grad = None
        self.propagate_shape = None


'''有参数层'''


class ParaLayer(Layer):
    def __init__(self, input_shape, output_shape, pre_layer=None, next_layer=None):
        super(ParaLayer, self).__init__(input_shape, output_shape, pre_layer, next_layer)
        self.neurons = None
        self.neurons_shape = None
        self.propagate_grad = None
        self.propagate_shape = None

    def NeuronUpdateOperator(self, *args, **kw):
        pass


'''线性层，该层有三个方法：
ForwardOperator——————计算正向传播的值
NeuronUpdateOperator——————计算反向传播时线性层的参数梯度
PropagateOperator——————计算反向传播时传递到下一层的梯度值'''


class LinearLayer(ParaLayer):
    def __init__(self, input_shape: int, output_shape: int, pre_layer=None, next_layer=None):
        super(LinearLayer, self).__init__(input_shape, output_shape, pre_layer, next_layer)
        self.neurons_shape = [input_shape, output_shape]
        self.neurons = [[Neuron(value=np.random.rand(1)[0], grad=0) for _ in range(output_shape)] for _ in
                        range(input_shape)]

    def ForwardOperator(self, input: list):
        self.input = input
        self.output = []
        for i in range(self.output_shape):
            tem = 0
            for j in range(self.input_shape):
                tem += self.input[j] * self.neurons[j][i].value
            self.output.append(tem)
        return self.output

    def NeuronUpdateOperator(self, grad_output: list):
        for i in range(self.input_shape):
            for j in range(self.output_shape):
                self.neurons[i][j].grad = grad_output[j] * self.input[i]

    def PropagateOperator(self, grad_output: list):
        self.propagate_grad = []
        for i in range(self.input_shape):
            tem = 0
            for j in range(self.output_shape):
                tem += grad_output[j] * self.neurons[i][j].value
            self.propagate_grad.append(tem)
            self.propagate_shape = self.input_shape
        return self.propagate_grad


'''激活函数层，自身没有参数，所以只需要定义正向传播的方法以及需要传递给下一层的梯度即可'''


class Sigmoid(NoParaLayer):
    def __init__(self):
        super(Sigmoid, self).__init__()

    def ForwardOperator(self, input):
        self.input = input
        self.input_shape = len(input)
        self.output = []
        for num in input:
            self.output.append(1.0 / (1.0 + np.power(np.e, -num)))
        return self.output

    def PropagateOperator(self, grad_output):
        self.propagate_grad = []
        for i, num in enumerate(grad_output):
            self.propagate_grad.append(
                (np.power(np.e, -self.input[i]) / np.power(1 + np.power(np.e, -self.input[i]), 2)) * num)
        self.propagate_shape = self.input_shape
        return self.propagate_grad


'''返回mseloss的梯度，注意不是计算损失值而是返回梯度'''


def MSELossGrad(predict: float, label: float):
    return 2 * (predict - label)


class NetWork(object):
    def __init__(self, layers: list):
        self.layers = layers
        for i, layer in enumerate(self.layers):
            if i != 0:
                layer.pre_layer = self.layers[i - 1]
            if i != len(self.layers) - 1:
                layer.next_layer = self.layers[i + 1]

    def Forward(self, input):
        # 正向传播，没什么说的，一层一层传就好
        layer = self.layers[0]
        x = input
        while (layer != None):
            x = layer.ForwardOperator(x)
            layer = layer.next_layer
        return x

    def Backward(self, predict, label, loss_grad_fn):
        # 反向传播，将每一层输出对于输入的偏导数传递到上一层，并更新线性层的梯度值
        grad = [loss_grad_fn(predict, label)]
        layer = self.layers[-1]
        while (layer != None):
            try:
                layer.NeuronUpdateOperator(grad)
            except:
                pass

            grad = layer.PropagateOperator(grad)
            layer = layer.pre_layer

    def Update(self):
        # 更新梯度参数
        for layer in self.layers:
            if hasattr(layer, 'neurons'):
                for i in range(len(layer.neurons)):
                    for j in range(len(layer.neurons[0])):
                        layer.neurons[i][j].value -= (layer.neurons[i][j].grad * 0.05)
